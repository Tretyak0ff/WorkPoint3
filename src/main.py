"""package Working Point #3"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from routes.point import point_router


app = FastAPI(
    docs_url='/api/docs',
    title='Working point #3'
)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(point_router,  prefix="/point")
app.mount("/static",
          StaticFiles(directory="src/templates/static"),
          name="static")


@app.get("/")
async def root() -> dict:
    """router root"""
    return RedirectResponse(url="/point/")  # type: ignore


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
