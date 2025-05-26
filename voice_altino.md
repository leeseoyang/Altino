from AltinoLite import *       # ✅ AltinoLite 함수 사용
import speech_recognition as sr

Open("COM3")   # COM5는 Bluetooth SPP 포트

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("\n🎤 '사과'라고 말해보세요...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    result = recognizer.recognize_google(audio, language="ko-KR")
    print("🗣️ 인식된 단어:", result)

    if "사과" in result:
        print("✅ 정답! 전진")
        Go(500, 500)     # AltinoLite의 전진 명령
        delay(1000)
        Stop()
    else:
        print("❌ 오답. 좌회전")
        Go(-300, 300)
        delay(1000)
        Stop()

except sr.UnknownValueError:
    print("❌ 음성을 이해할 수 없습니다.")
except sr.RequestError as e:
    print(f"❌ Google API 오류: {e}")
except Exception as e:
    print("❌ 음성 인식 중 오류 발생:", e)

Close()   # AltinoLite 함수로 마무리
