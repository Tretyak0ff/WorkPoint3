from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


point_router = APIRouter(
    tags=["Point"]
)

templates = Jinja2Templates(directory="src/templates/")


@point_router.get("/")
async def get_point(request: Request, response_class=HTMLResponse):
    """router get /point"""
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
        }
    )
