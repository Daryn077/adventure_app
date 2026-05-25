import os
import uuid
from fastapi import UploadFile


UPLOAD_DIR = "app/static/uploads"


async def save_upload_file(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    return f"/static/uploads/{unique_filename}"