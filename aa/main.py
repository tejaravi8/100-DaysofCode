from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# fake database
students = {
    1: {"name": "Teja", "age": 21, "course": "Python"},
    2: {"name": "Ravi", "age": 22, "course": "SQL"},
}

# 🏠 Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# 📋 Student list page
@app.get("/students", response_class=HTMLResponse)
def show_students(request: Request):
    return templates.TemplateResponse("students.html", {"request": request, "students": students})

# ➕ Add student page
@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):
    return templates.TemplateResponse("add_student.html", {"request": request})

# 📤 Handle form submission
@app.post("/add")
def add_student(name: str = Form(...), age: int = Form(...), course: str = Form(...)):
    new_id = len(students) + 1
    students[new_id] = {"name": name, "age": age, "course": course}
    # redirect to student list after adding
    return RedirectResponse("/students", status_code=303)
