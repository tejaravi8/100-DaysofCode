from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="FastAPI Calculator")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def calculator_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@app.post("/calculate", response_class=HTMLResponse)
def calculate(request: Request, num1: float = Form(...), num2: float = Form(...), operation: str = Form(...)):
    result = None

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = "Error: Cannot divide by zero" if num2 == 0 else num1 / num2
    else:
        result = "Invalid operation"

    return templates.TemplateResponse("calculator.html", {
        "request": request,
        "result": result,
        "num1": num1,
        "num2": num2,
        "operation": operation
    })
