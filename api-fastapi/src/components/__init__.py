from fastapi import FastAPI #, Request, HTTPException, File, UploadFile
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from constants import setting

app = FastAPI(**setting.api_description)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

from components import routes
handler = Mangum(app)
