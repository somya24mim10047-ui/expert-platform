from fastapi import APIRouter, UploadFile, File
import cloudinary.uploader
from backend.service.cloudinary_config import *

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    result = cloudinary.uploader.upload(
        file.file
    )

    return {
        "url": result["secure_url"]
    }