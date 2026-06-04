# Face Authentication API

This project is a simple face authentication system built using FastAPI and InsightFace.

The API accepts two images, detects faces in both images, generates face embeddings, and compares them using cosine similarity. Based on the similarity score, it determines whether the faces belong to the same person.

## Tech Stack

* Python
* FastAPI
* InsightFace
* OpenCV
* NumPy
* ONNX Runtime

## Project Structure

```text
FaceAuthentication/
│
├── app.py
├── train.py
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the API

Start the server using:

```bash
uvicorn app:app --reload
```

Once the server starts, open:

```text
http://127.0.0.1:8000/docs
```

to access the Swagger UI and test the endpoints.

## Endpoint

### POST /verify

Upload two face images and the API will return:

* Verification result (same person / different person)
* Similarity score
* Bounding box coordinates for detected faces

## Sample Response

```json
{
  "verification_result":“same person” or “different person”
  "similarity_score": 0.7505,
  "bounding_box_image1": [],
  "bounding_box_image2": []
}