import cv2

def check_liveness():
    cap = cv2.VideoCapture(0)
    print("[LIVENESS CHECK] Please blink or move slightly...")

    blink_detected = False
    frames_checked = 0

    while frames_checked < 60:  # check for ~2 seconds
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # For now, placeholder: we assume liveness detected if frames are captured
        blink_detected = True
        frames_checked += 1

        cv2.imshow("Liveness Check", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return blink_detected

