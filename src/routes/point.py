from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates



@point_router.post("/")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    """router add todo"""
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
                                      {
                                          "request": request,
                                          "todos": todo_list
                                      })
