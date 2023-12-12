from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

point_router = APIRouter(
    tags=["Point"]
)

templates = Jinja2Templates(directory="src/templates/")


@point_router.get("/")
async def get_point(request: Request):
    """router get todo"""
    # graph_1 = [{'x': 0.00, 'y': 1.00},
    #            {'x': 25.11, 'y': 1.63},
    #            {'x': 37.44, 'y': 1.78},
    #            {'x': 42.88, 'y': 1.88},
    #            {'x': 47.77, 'y': 2.00},
    #            {'x': 78.90, 'y': 2.48},
    #            {'x': 80.90, 'y': 2.58}]

    # graph_2 = [{'x': 10.00, 'y': 1.00},
    #            {'x': 35.11, 'y': 1.63},
    #            {'x': 47.44, 'y': 1.78},
    #            {'x': 52.88, 'y': 1.88},
    #            {'x': 57.77, 'y': 2.00},
    #            {'x': 88.90, 'y': 2.48},
    #            {'x': 90.90, 'y': 2.58}]

    compression = [
        1.00, 1.63, 1.78, 1.88, 2.00, 2.48, 2.58]

    surge_line = [
        0.00, 22.11, 27.79, 32.31, 37.41, 64.94, 70.74]

    anti_surge_line = [
        10.00, 32.11, 37.79, 42.31, 47.41, 74.57, 80.74]

    return templates.TemplateResponse(
        "point.html", {
            "request": request,
            "y_axis": compression,
            "line_1": surge_line,
            "line_2": anti_surge_line,
            "message": "this is the point_router directory"
        }
    )
    # return templates.TemplateResponse("todo.html", {
    #     "request": request,
    #     "todos": todo_list
    # })