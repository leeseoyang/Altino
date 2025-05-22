import speech_recognition as sr
import serial
import time

# ✅ Altino 연결 (COM5, 9600bps)
try:
    altino = serial.Serial('COM5', 9600)
    print("✅ Altino LITE 연결 성공")
except Exception as e:
    altino = None
    print("❌ Altino 연결 실패:", e)

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
        if altino:
            altino.write(b'F\n')  # ✅ 개행 포함
            time.sleep(1)
            altino.write(b'S\n')
    else:
        print("❌ 오답. 좌회전")
        if altino:
            altino.write(b'L\n')
            time.sleep(1)
            altino.write(b'S\n')

except sr.UnknownValueError:
    print("❌ 음성을 이해할 수 없습니다.")
except sr.RequestError as e:
    print(f"❌ Google API 오류: {e}")
except Exception as e:
    print("❌ 음성 인식 중 오류 발생:", e)
