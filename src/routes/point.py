from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

point_router = APIRouter(
    tags=["Point"]
)

templates = Jinja2Templates(directory="src/templates/")


@point_router.get("/")
async def get_point(request: Request):
    """router get todo"""
    return templates.TemplateResponse(
        "point.html", {
            "request": request,
            "message": "this is the point_router directory"
        }
    )
    # return templates.TemplateResponse("todo.html", {
    #     "request": request,
    #     "todos": todo_list
    # })
