import serial
import time

altino = serial.Serial("COM3", 9600)  # USB 연결 포트 확인

print("🚗 전진 명령 전송 중...")
altino.write(b'F\n')
time.sleep(1)

print("🛑 정지 명령 전송 중...")
altino.write(b'S\n')

altino.close()
print("✅ 명령 전송 완료")