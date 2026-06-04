import cv2
import numpy as np
from insightface.app import FaceAnalysis

# Load model once when the file is imported
face_app = FaceAnalysis(name="buffalo_l")
face_app.prepare(ctx_id=-1)


def cosine_similarity(vector1, vector2):
    """
    Calculate cosine similarity between two face embeddings.
    """

    return np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) *
        np.linalg.norm(vector2)
    )


def verify_faces(image1_path, image2_path):

    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None:
        return {
            "error": "Unable to read first image"
        }

    if image2 is None:
        return {
            "error": "Unable to read second image"
        }

    faces_in_image1 = face_app.get(image1)
    faces_in_image2 = face_app.get(image2)

    if len(faces_in_image1) == 0:
        return {
            "error": "No face detected in first image"
        }

    if len(faces_in_image2) == 0:
        return {
            "error": "No face detected in second image"
        }

    embedding1 = faces_in_image1[0].embedding
    embedding2 = faces_in_image2[0].embedding

    similarity_score = float(
        cosine_similarity(
            embedding1,
            embedding2
        )
    )

    verification_result = (
        "same person"
        if similarity_score > 0.60
        else "different person"
    )

    return {
        "verification_result": verification_result,
        "similarity_score": round(similarity_score, 4),
        "bounding_box_image1":
            faces_in_image1[0].bbox.tolist(),
        "bounding_box_image2":
            faces_in_image2[0].bbox.tolist()
    }