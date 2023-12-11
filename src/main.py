"""package Working Point #3"""
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder


app = FastAPI(
    docs_url='/api/docs',
    title='Working point #3'
)


@app.get("/")
async def root() -> dict:
    """router root"""
    return jsonable_encoder(
        {
            "message": "this is the root directory"
        }
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
