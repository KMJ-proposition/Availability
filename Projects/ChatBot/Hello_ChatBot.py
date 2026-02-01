from getpass import getuser as gu
from random import choice as rc
import re



dict_ext_01 = ['안녕', '좋은 아침', '굿모닝', '반가워']
dict_ext_02 = ['Hello', 'Hi', 'ntm', 'bro', 'sis', 'Hey', 'i\'m greeting you']
        
class ChatBot:
    def __init__(self, username):
        self.response_user = {
                "ko": {
                        "hello": ('안녕하세요', '반갑습니다', '안녕하세요?', '반가워요'),
                        "main" : ['사용자', username],
                        "title": [['님'], ['형', '오빠']],
                        "empha": ['!', '~', '.']
                    },
                "en": {
                        "hello": ('Hi there', 'Hello', 'Nice to meet you', 'Good to see you'),
                        "main" : ['Sir', username],
                        "title": [['Dear', 'you'], ['Sis', 'Bro']],
                        "empha": ['!', '~', '!!!']
                    }
            }

        self.response_ai = {
                "ko": {
                        "dict": dict_ext_01,
                        "title": ('제게', '저에게')
                    },
                "en": {
                        "dict": dict_ext_02,
                        "title": ('I')
                    }
            }


    def ai_dict_ko(self):
        return self.response_ai["ko"]["dict"]
    def ai_dict_en(self):
        return self.response_ai["en"]["dict"]


    def ai_title_ko(self):
        return rc(self.response_ai["ko"]["title"])
    def ai_title_en(self):
        return rc(self.response_ai["en"]["title"])
    
    def r_user_ko(self):
        return rc(self.response_user["ko"]["main"])
    def r_title_ko(self):
        return rc(rc(self.response_user["ko"]["title"]))    
    def r_hello_ko(self):
        return rc(self.response_user["ko"]["hello"])    
    def r_empha_ko(self):
        return rc(self.response_user["ko"]["empha"])
    
    def r_user_en(self):
        return rc(self.response_user["en"]["main"])
    def r_title_en(self):
        return rc(rc(self.response_user["en"]["title"]))    
    def r_hello_en(self):
        return rc(self.response_user["en"]["hello"])    
    def r_empha_en(self):
        return rc(self.response_user["en"]["empha"])


class say:
    def __init__(self, lang):
        if lang == "ko":
            self.username = ("당신")
            self.botname = ("챗봇")
        else:
            self.username = ("You")
            self.botname = ("Chat Bot")
            
    def bot(self, message):
        print("* %s: %s" %(self.botname, message))
        return message

class error:
    def __init__(self):
        self.name = ("* 오류")
        
    def err01(self, message):
        print("%s: %s" %(self.name, message))
        return message

username = gu()

chat = ChatBot(username)

while True:
    print("-----------------------------------------------------------------------------------")
    print("| * 인사하는 챗봇 Ver.1 (Greeting ChatBot Ver.1)")
    print("| 종료는 '종료'를 입력해주세요. Type 'quit' or 'exit' if you want to stop this.")
    print("| 한/영 중 아무 문자나 입력해주세요. Please input any letters.")
    print("| 입력 문자에 맞는 대화가 가능합니다. You can choose with your letter with language")
    print("| * 종료 입력: 종료, quit, exit")
    print("-----------------------------------------------------------------------------------")
    menu_input = input(">>> ").strip()
    user_input = ""

    if re.fullmatch(r"^(quit|exit|종료)$", menu_input):
        break 

    elif menu_input == "":
         continue

    elif re.search(r"[ㄱ-ㅎㅏ-ㅣ가-힣]", menu_input):        
        print("[한글] 메뉴로 돌아가려면 '잘있어'를 입력하세요.")
        narrator = say("ko")
        korean = chat.ai_dict_ko()
        narrator.bot("%s%s %s%s" %(chat.r_user_ko(), chat.r_title_ko(), chat.r_hello_ko(), chat.r_empha_ko()))
        
        while True:
            print("* 당신: ", end="")
            user_input = input().strip()
            u_title_ko = chat.r_title_ko()
                
            if user_input == "잘있어":
                 break
            if any(word in user_input for word in korean):
                narrator.bot("%s%s" %(chat.r_hello_ko(), chat.r_empha_ko()))                
            elif u_title_ko in chat.response_user["ko"]["title"][0]:
                narrator.bot("%s%s, %s 반갑게 인사해주시면 좋겠어요." %(chat.r_user_ko(), u_title_ko, chat.ai_title_ko()))                
            elif u_title_ko in chat.response_user["ko"]["title"][1]:
                narrator.bot("%s %s%s" %(u_title_ko, chat.r_hello_ko(), chat.r_empha_ko()))            
            else:
                narrator.bot("이모티콘, 특수기호, 문자 등 입니다.")

                    
    elif re.search(r"[A-Za-z]", menu_input):
        print("[ENG] If you want to go menu, type 'goodbye'")
        narrator = say("en")
        english = chat.ai_dict_en()
        print("%s %s %s%s" %(chat.r_user_en(), chat.r_title_en(), chat.r_hello_en(), chat.r_empha_en()))

        while True:                
            u_title_en = chat.r_title_en()
            print("* You: ", end="")
            user_input = input().strip()
                
            if user_input.lower() == "goodbye":
                break
            if any(word.lower() in user_input.lower() for word in english):
                narrator.bot("%s%s" %(chat.r_hello_en(), chat.r_empha_en()))                
            elif u_title_en in chat.response_user["en"]["title"][0]:
                narrator.bot("%s, %s appreciate if you greet me." %(chat.r_user_en(), chat.ai_title_en()))                
            elif u_title_en in chat.response_user["en"]["title"][1]:
                narrator.bot("Ssup my %s%s" %(u_title_en, chat.r_empha_en()))            
            else:
                narrator.bot("привет")
            
    else:
        err = error()
        err.err01("#*(%&Y#@)(*^&!)( 저는 당신의 말을 이해할 수 없어요. I cannot understand your word")
