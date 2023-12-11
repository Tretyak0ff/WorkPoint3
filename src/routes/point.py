from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates





@point_router.get("/")
async def retrieve_todo(request: Request):
    """router get todo"""
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })