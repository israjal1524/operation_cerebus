import speech_recognition as sr

def verify_voice(expected_phrase):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("[VOICE SCAN] Speak the password phrase now...")
        audio_data = r.listen(source)

    try:
        text = r.recognize_google(audio_data).strip().lower()
        print(f"[VOICE DETECTED] {text}")
        return text == expected_phrase.lower()
    except sr.UnknownValueError:
        print("[ERROR] Could not understand audio.")
        return False
    except sr.RequestError:
        print("[ERROR] Speech recognition service unavailable.")
        return False

