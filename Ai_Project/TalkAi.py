import speech_recognition as sr
import pyttsx3
import pywhatkit
import threading

# 텍스트 음성 변환 초기화
engine = pyttsx3.init()

# 전역 변수
is_waiting = False  # 대기 상태를 나타내는 플래그
is_running = True   # 프로그램이 실행 중인지 나타내는 플래그

def talk(text):
    """텍스트를 음성으로 출력"""
    print(f"GPT 출력: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """사용자 음성을 텍스트로 변환"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("듣는 중...")
        try:
            recognizer.adjust_for_ambient_noise(source)  # 배경 소음 조정
            voice = recognizer.listen(source, timeout=10)  # 10초 대기
            command = recognizer.recognize_google(voice, language='ko-KR')
            print(f"사용자: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return ""  # 아무 동작도 하지 않음
        except sr.RequestError as e:
            print(f"음성 인식 서비스에 문제가 있습니다: {e}")
            return ""

def play_song(command):
    """명령에서 노래 제목을 추출하고 재생"""
    if "틀어 줘" in command or "재생" in command:
        song = command.replace("틀어 줘", "").replace("재생", "").strip()
        if song:
            try:
                talk(f"{song}을 재생합니다.")
                print(f"재생할 노래: {song}")
                pywhatkit.playonyt(song)  # YouTube에서 노래 재생
            except Exception as e:
                print(f"노래 재생 중 오류 발생: {e}")
                talk("노래를 재생하는 중 문제가 발생했습니다.")
        else:
            talk("노래 제목을 말씀해 주세요.")
    else:
        talk("무슨 노래를 틀어드릴지 말씀해 주세요.")

def wait_for_jarvis():
    """대기 상태에서 '자비스' 호출을 감지"""
    global is_waiting
    while is_waiting:
        print("대기 상태: '자비스'를 기다리는 중...")
        command = listen()
        if command:  # 빈 명령이 아닌 경우에만 처리
            if "자비스" in command:
                talk("네, 무엇을 도와드릴까요?")
                is_waiting = False  # 대기 상태 해제
                return True  # 자비스 호출 확인
            elif "종료" in command or "그만" in command:
                return False  # 종료 명령어 확인
    return True

if __name__ == "__main__":
    while is_running:
        user_command = listen()
        if not user_command:
            continue
        if "종료" in user_command or "그만" in user_command:
            talk("프로그램을 종료합니다.")
            is_running = False
            break
        if "대기" in user_command:
            talk("대기 상태에 들어갑니다. '자비스'라고 호출하세요.")
            is_waiting = True
            jarvis_called = wait_for_jarvis()
            if not jarvis_called:  # 종료 명령어 처리
                is_running = False
                break
            continue  # 대기 상태 해제 후 다시 명령을 받을 준비
        play_song(user_command)