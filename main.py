from src.face_auth import verify_face
from src.voice_auth import verify_voice
from src.liveness import check_liveness
from config.settings import PASSWORD_PHRASE

def main():
    print("[OPERATION CERBERUS] Initializing security protocols...")

    # Step 1: Face Verification
    if not verify_face():
        print("[ACCESS DENIED] Unauthorized face detected.")
        return

    # Step 2: Liveness Check
    if not check_liveness():
        print("[ACCESS DENIED] Liveness test failed.")
        return

    # Step 3: Voice Authentication
    if not verify_voice(PASSWORD_PHRASE):
        print("[ACCESS DENIED] Incorrect voice/password.")
        return

    print("[ACCESS GRANTED] Welcome, operative.")

if __name__ == "__main__":
    main()

