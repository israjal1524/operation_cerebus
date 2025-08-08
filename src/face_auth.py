import cv2
import face_recognition
import pickle
from config.settings import FACE_DATA_PATH, FACE_ENCODINGS_FILE, FACE_MATCH_THRESHOLD

def verify_face():
    # Load known face encodings
    try:
        with open(FACE_ENCODINGS_FILE, "rb") as f:
            known_encodings, known_names = pickle.load(f)
    except FileNotFoundError:
        print("[ERROR] Face encodings not found. Train first.")
        return False

    # Start webcam
    cap = cv2.VideoCapture(0)
    print("[FACE SCAN] Looking for your face...")

    success = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]
        faces_loc = face_recognition.face_locations(rgb_frame)
        faces_enc = face_recognition.face_encodings(rgb_frame, faces_loc)

        for face_encoding in faces_enc:
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=FACE_MATCH_THRESHOLD)
            if True in matches:
                print("[FACE MATCH] Identity confirmed.")
                success = True
                break

        cv2.imshow("Face Verification", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or success:
            break

    cap.release()
    cv2.destroyAllWindows()
    return success
