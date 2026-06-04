from insightface.app import FaceAnalysis


def load_face_model():
    """
    Initialize and load the InsightFace model.
    This script is used to prepare the face recognition model.
    """

    face_app = FaceAnalysis(name="buffalo_l")

    # Use CPU for compatibility
    face_app.prepare(
        ctx_id=-1,
        det_size=(640, 640)
    )

    print("Face model loaded successfully.")

    return face_app


if __name__ == "__main__":
    load_face_model()