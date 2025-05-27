from AltinoLite import *
import speech_recognition as sr

Open("COM3")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("\n🎤 '사과'라고 말해보세요...")
    recognizer.adjust_for_ambient_noise(source, duration=0.3)
    try:
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=1.5)
        result = recognizer.recognize_google(audio, language="ko-KR")
        print("🗣️ 인식된 단어:", result)

        if "사과" in result:
            print("✅ 정답! 전진")
            Go(500, 500)
            delay(1000)
            Stop()
        else:
            print("❌ 오답. 후진")
            Go(-500, 300)
            delay(1000)
            Stop()

    except sr.WaitTimeoutError:
        print("⏰ 시간 초과: 말을 시작하지 않았습니다.")
    except sr.UnknownValueError:
        print("❌ 음성을 이해할 수 없습니다.")
    except sr.RequestError as e:
        print(f"❌ Google API 오류: {e}")
    except Exception as e:
        print("❌ 음성 인식 중 오류 발생:", e)

Close()
