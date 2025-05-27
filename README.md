<p align="center">
  <img src="images/banner.png" alt="Altino Banner" width="800"/>
</p>

# 🎤 Altino 음성 인식 제어 시스템 (Python + Toga)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Toga](https://img.shields.io/badge/Toga-GUI-blueviolet?style=flat&logo=python)
![Altino](https://img.shields.io/badge/Altino-Robot-yellow?style=flat)
![Windows](https://img.shields.io/badge/Platform-Windows-blue)

**Altino 자동차**를 음성 명령으로 제어하는 Python 기반 데스크탑 앱입니다.  
음성 인식(`speech_recognition`)과 GUI 프레임워크인 `Toga`를 활용하여 `"사과"`라고 말하면 전진하는 구조입니다.

---

## 📸 실행 화면

<p align="center">
  <img src="images/demo_ui.gif" alt="Altino UI 데모" width="500"/>
</p>

> 🎥 영상은 `.gif`로 변환하여 `images/demo_ui.gif`로 저장한 상태입니다.

---

## 🧠 주요 기능

- 마이크로부터 5초간 음성 녹음
- `"사과"`라는 음성 인식 시 Altino 자동차 전진
- `AltinoLite.py` 연동을 통한 블루투스 시리얼 제어
- Toga 기반 GUI 앱 (버튼 클릭 → 음성 인식)

---

## 🛠 실행 환경

| 항목        | 내용                                      |
|-------------|-------------------------------------------|
| OS          | Windows 10 이상                           |
| Python      | 3.9.x                                     |
| 라이브러리  | `toga`, `sounddevice`, `speech_recognition`, `pyaudio`, `scipy` 등 |
| 장치        | Altino Lite (Bluetooth 연결 필요)         |

---

## ▶️ 실행 방법

```bash
# 1. 저장소 클론
git clone https://github.com/leeseoyang/Altino.git
cd Altino

# 2. 필수 패키지 설치
pip install -r requirements.txt

# 3. 앱 실행
python app.py
````

> ⚠️ `AltinoLite.py`에 Altino가 연결된 포트를 `"COM5"` 또는 실제 포트로 설정해주세요.

---

## 📁 프로젝트 구조

```
Altino/
├── AltinoLite.py        # Altino 제어를 위한 시리얼 코드
├── app.py               # GUI 앱 실행 코드 (Toga 기반)
├── voice_altino.py      # CLI 기반 음성 인식 예제
├── go_test.py           # Altino 전진 테스트용 코드
├── requirements.txt     # 설치 라이브러리 목록
├── README.md            # 설명 문서
└── images/
    ├── altino_banner.png
    └── demo_ui.gif      # 실행 데모 GIF
```

---

## 👨‍💻 개발자

| 이름  | 깃허브                                                     |
| --- | ------------------------------------------------------- |
| 이서경 | [@leeseoyang](https://github.com/leeseoyang)            |
| 이메일 | [23615038@konyang.ac.kr](mailto:23615038@konyang.ac.kr) |

---

## 📜 라이선스

이 프로젝트는 [MIT License](https://opensource.org/licenses/MIT)를 따릅니다.
학습·실습·연구 목적 사용은 자유이며, 출처를 남겨주시면 감사하겠습니다.

---

> 🚗 Altino 프로젝트가 도움이 되었다면 `⭐ Star`를 눌러주세요!
