import serial
import time

ports = ['COM4', 'COM5']  # 블루투스 직렬 포트 목록
baudrates = [9600, 115200]  # Altino 통신 속도 후보
commands = [b'F\n', b'f\n', b'1\n', b'F', b'f', b'1']  # 다양한 명령 조합

for port in ports:
    for speed in baudrates:
        for cmd in commands:
            try:
                print(f"\n🔍 포트: {port}, 속도: {speed}, 명령: {cmd}")
                altino = serial.Serial(port, speed, timeout=1, write_timeout=1)
                time.sleep(2)
                print("🚗 전진 명령 전송 중...")
                altino.write(cmd)
                time.sleep(1)
                print("🛑 정지 명령 전송 중...")
                altino.write(b'S\n')
                print(f"✅ 전송 성공: {port}, {speed}, 명령: {cmd}")
                altino.close()
                break
            except Exception as e:
                print(f"❌ 실패: {port} @ {speed}bps with {cmd} → {e}")