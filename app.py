import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, JUSTIFY
import threading
import os
import time
import sounddevice as sd
import soundfile as sf  # ✅ PCM 형식 저장용
import speech_recognition as sr
from AltinoLite import *  # ✅ Altino 연동

class VoiceCoding(toga.App):
    def startup(self):
        self.recording = False
        self.fs = 44100
        self.duration = 5

        # CSS 스타일 정의
        text_style = Pack(padding=10, text_align='center', alignment=CENTER)
        textW_style = Pack(padding=10, text_align='center', alignment=CENTER, color="#FFFFFF")
        Missionbox_style = Pack(width=200, height=50, padding=20, direction=COLUMN, justify_content=CENTER, alignment=CENTER, background_color="#FFF59D")
        line_style = Pack(height=1, width=250, background_color="gray")
        nav_style = Pack(width=250, height=40, padding=10, direction=ROW, alignment=CENTER, background_color="#D0D0D0")
        top_style = Pack(width=250, height=40, padding=10, direction=COLUMN, justify_content=CENTER, alignment=CENTER, background_color="#F29F8D")

        # 콘텐츠 구성
        self.Mission_label = toga.Label("🍊사과🍊를 말해주세요", style=text_style)
        self.Mission_box = toga.Box(children=[self.Mission_label], style=Missionbox_style)
        self.status = toga.Label("버튼을 눌러 시작하세요", style=Pack(padding_top=30, padding_bottom=10))
        self.button = toga.Button("🎙️녹음 시작🎙️", on_press=self.voice_coding, style=Pack(padding_bottom=30))

        self.content_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, background_color="#FFFEF5"))
        self.content_box.add(self.Mission_box)
        self.content_box.add(toga.Box(style=line_style))
        self.content_box.add(self.status)
        self.content_box.add(self.button)

        self.nav_bar = toga.Box(style=nav_style)
        for label in ["🏠홈", "🚗게임", "🗓️기록", "⚙설정"]:
            self.nav_bar.add(toga.Button(label, on_press=lambda w: None, style=Pack(padding=5)))

        self.nav_line = toga.Box(style=line_style)
        self.top_bar = toga.Box(style=top_style)
        self.top_bar.add(toga.Label("🚗 Test_version 🚗", style=textW_style))
        self.top_line = toga.Box(style=line_style)

        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        main_box.add(self.top_bar)
        main_box.add(self.top_line)
        main_box.add(self.content_box)
        main_box.add(self.nav_line)
        main_box.add(self.nav_bar)

        self.main_window = toga.MainWindow(title="Voice coding", size=(100, 450))
        self.main_window.content = main_box
        self.main_window.show()

    def voice_coding(self, widget):
        if self.recording:
            self.status.text = "듣고 있습니다. 잠시만 기다려 주세요."
        else:
            self.recording = True
            self.status.text = ". . . . . . 인식중 . . . . . ."
            threading.Thread(target=self.record).start()

    def record(self):
        try:
            audio = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=1)
            sd.wait()

            app_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(app_dir, "..", ".."))
            record_dir = os.path.join(project_root, "voice_save")
            os.makedirs(record_dir, exist_ok=True)

            timestamp = time.strftime("%Y_%m%d_%H%M")
            filename = os.path.join(record_dir, f"Voice_{timestamp}.wav")

            # ✅ 반드시 PCM 포맷으로 저장
            sf.write(filename, audio, self.fs, format='WAV', subtype='PCM_16')

            # 음성 인식
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audio_data = r.record(source)
                result = r.recognize_google(audio_data, language="ko-KR")
                self.status.text = f"🎉 인식 완료: {result}"

                if "사과" in result:
                    Open("COM3")
                    Go(500, 500)
                    delay(1000)
                    Stop()
                    Close()
        except Exception as e:
            self.status.text = f"인식 실패: {e}"
        finally:
            self.recording = False

def main():
    return VoiceCoding("Voice coding test", "com.example.testapp")

if __name__ == '__main__':
    app = main()
    app.main_loop()