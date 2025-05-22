import serial
import time

altino = serial.Serial("COM3", 9600)  # 필요 시 COM 포트 수정
time.sleep(2)  # 연결 안정화 시간

# 전진
altino.write(b'F')   # 또는 b'1', b'8' 실기 자료에 따라 변경 필요
time.sleep(1)

# 정지
altino.write(b'S')
altino.close()
