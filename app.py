from fastapi import FastAPI, UploadFile, File
import tempfile

from test import verify_faces

app = FastAPI(
    title="Face Authentication API",
    description="Face verification service using InsightFace",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Face Authentication API Running"
    }


@app.post("/verify")
async def verify(
    image1: UploadFile = File(...),
    image2: UploadFile = File(...)
):

    # Save first uploaded image
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp_file1:

        temp_file1.write(
            await image1.read()
        )

        image1_path = temp_file1.name

    # Save second uploaded image
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp_file2:

        temp_file2.write(
            await image2.read()
        )

        image2_path = temp_file2.name

    result = verify_faces(
        image1_path,
        image2_path
    )

    return result