#  Copyright (c) 2024 Crono Wise.
#
#  All rights reserved.
#
#  This code is protected by copyright and may not be used,
#  distributed, or reproduced in any form without the written permission of the author.
#
#  DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN
#  AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION
#  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.dto.entryDTO import EntryCoordDTO, EntryStringDTO
from app.services.general_service import GeneralService
from app.views import address_views, fuel_views, industry_views, truck_views

# Core of the application

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    from pip._vendor.colorama import Fore, Style
    print(Fore.GREEN + "CORE: Application started")
    print(Style.RESET_ALL)
    yield
    # Shutdown event
    print(Fore.MAGENTA + "CORE: Stopping application")


# Create FastAPI instance
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send/coord")
async def send_coord(raw_data: EntryCoordDTO):
    return GeneralService().execute(raw_data.latitude, raw_data.longitude, raw_data.tons)


@app.post("/send/address")
async def send_address(raw_data: EntryStringDTO):
    from app.services.external.opencage_service import OpenCageService
    coords = OpenCageService().get_location(raw_data.address)
    return GeneralService().execute(coords[0], coords[1], raw_data.tons)


app.include_router(address_views.router, tags=["address"])
app.include_router(fuel_views.router, tags=["fuel"])
app.include_router(industry_views.router, tags=["industry"])
app.include_router(truck_views.router, tags=["truck"])


# Basic route Hello World to test the application
@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello World"}
