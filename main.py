from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
    )


@app.post("/")
def download_start(link: str = Form(...)):
    yt_di_opts={
        "format":"best",
        "outtmpl":os.path.join(os.getcwd(), f"test{link[-8:]}.mp4")
    }
    with yt_dlp.YoutubeDL(yt_di_opts) as ydl:
        ydl.download([link])
    return {"status": "Download Completed Successfully", "info":f"File saved as ' test{link[-8:]}.mp4 '"}


@app.get("/h")
def h():
    return {"Hello":"World"}

    
#    download_start("https://youtube.com/shorts/4t-5nlg_qPQ?si=nGCQ35-H0mQNWpke")
