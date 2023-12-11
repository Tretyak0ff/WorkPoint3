"""package Working Point #3"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.point import point_router


app = FastAPI(
    docs_url='/api/docs',
    title='Working point #3'
)

app.include_router(point_router,  prefix="/point")


@app.get("/")
async def root() -> dict:
    """router root"""
    return RedirectResponse(url="/point/")  # type: ignore


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
