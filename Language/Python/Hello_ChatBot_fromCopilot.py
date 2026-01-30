from getpass import getuser as gu
from random import choice as rc
import re

KO_HELLOS = ['안녕', '좋은 아침', '굿모닝', '반가워']
EN_HELLOS = ['hello', 'hi', 'ntm', 'bro', 'sis', 'hey', "i'm greeting you"]

def bot(name, msg):
    print(f"* {name}: {msg}")

username = gu()

while True:
    print("-" * 80)
    print("| 인사하는 챗봇 (Greeting ChatBot)")
    print("| 종료: 종료 / quit / exit")
    print("-" * 80)
    menu = input(">>> ").strip()

    if re.fullmatch(r"(종료|quit|exit)", menu, re.I):
        break
    if menu == "":
        continue

    # 한글
    if re.search(r"[ㄱ-ㅎㅏ-ㅣ가-힣]", menu):
        bot("챗봇", f"{username}님 안녕하세요!")
        print("[한글] 메뉴로 돌아가려면 '잘있어'를 입력하세요.")
        while True:
            user = input("* 당신: ").strip()
            if user == "잘있어":
                break
            if any(w in user for w in KO_HELLOS):
                bot("챗봇", rc(["안녕하세요!", "반가워요!", "좋은 하루예요!"]))
            else:
                bot("챗봇", "무슨 말인지 잘 모르겠어요.")

    # 영어
    elif re.search(r"[A-Za-z]", menu):
        bot("Chat Bot", f"{username}, Hello!")
        print("[ENG] Type 'goodbye' to go back to menu.")
        while True:
            user = input("* You: ").strip()
            if user.lower() == "goodbye":
                break
            if any(w in user.lower() for w in EN_HELLOS):
                bot("Chat Bot", rc(["Hi!", "Nice to meet you!", "Good to see you!"]))
            else:
                bot("Chat Bot", "I don't understand.")

    else:
        print("* 오류: 저는 당신의 말을 이해할 수 없어요.")