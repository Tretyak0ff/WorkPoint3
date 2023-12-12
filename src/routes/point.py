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

    x_axis = [1.00, 1.63, 1.78, 1.88, 2.00, 2.48, 2.58]

    graph_1 = [
        0.00, 22.11, 27.79, 32.31, 37.41, 64.94, 70.74
    ]

    graph_2 = [
        10.00, 32.11, 37.79, 42.31, 47.41, 74.57, 80.74
    ]

    return templates.TemplateResponse(
        "point.html", {
            "request": request,
            "x_axis": x_axis,
            "graph_1": graph_1,
            "graph_2": graph_2,
            # "graph_1": graph_1,
            # "graph_2": graph_2,
            "message": "this is the point_router directory"
        }
    )
    # return templates.TemplateResponse("todo.html", {
    #     "request": request,
    #     "todos": todo_list
    # })