from fastapi import FastAPI, File, UploadFile , Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
import os
import json

from OCRModel import OCRModel
from IngredientEvaluationModel import GenerateResponse

app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_images"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    # return {"message": "Welcome to the FastAPI backend!"}
    context = {"request": request, "title": "Welcome to FastAPI", "message": "This is a dynamic template."}
    return templates.TemplateResponse("index.html", context)

@app.get("/upload/")
async def upload_page(request: Request):
    context = {"request": request, "title": "Upload Page"}
    return templates.TemplateResponse("upload.html", context)

@app.post("/upload/")
async def upload_image(request: Request,file: UploadFile = File(...)):
    try:
        # print("Enterred")
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        # print("imageRecieved",file_path)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        response = OCRModel("./uploaded_images/"+file.filename)
        print("response: ",response)
        result = GenerateResponse(response)

        print("original result:\n",result)
        result = result.strip("```json\n")
        print("result:\n",result)
        result_dict = json.loads(result)
        print("result_dict:\n",result_dict)

        return templates.TemplateResponse("output.html", {"request": request, "output": result_dict})
        # return templates.TemplateResponse("output.html", context)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/contact/")
async def upload_page(request: Request):
    context = {"request": request, "title": "Upload Page"}
    return templates.TemplateResponse("contact.html", context) 