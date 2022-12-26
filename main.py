from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="html_templates/")

@app.get("/", response_class=HTMLResponse)
def file_up_req_page(request : Request):
    return templates.TemplateResponse("homepage.html", context={"request" : request})

@app.post("/file_status_page", response_class=HTMLResponse)
async def file_up_status(request = Request, firstname : str = Form(...), assign_file : UploadFile = File(...)):
    firstname = firstname
    assign_file_content = await assign_file.read()
    print(assign_file_content)
    return templates.TemplateResponse("file_status.html", context={"request" : request, "firstname" : firstname})

if __name__ == "__main__":
    uvicorn.run(app)