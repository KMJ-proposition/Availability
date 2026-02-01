from getpass import getuser as gu
from random import choice as rc

# ai: source
# ai_self = ('제게', '저에게')

# r: response
# r_hello = ('안녕하세요', '반갑습니다', '안녕하세요?', '반가워요')
# r_main  = ['사용자', username]
# r_title = [['님', '씨'], ['형', '오빠']]
# r_empha = ['!', '~']

# p: print
# p_title = rc(rc(r_title))

# user's name
# username = gu()

# input from user
# dict_hello = {'안녕', '좋은 아침', '굿모닝'}                      

# respond from bot
# p_title = Response

# user_input = input().strip() # strip 개행

# Chat
# if any(word in user_input for word in dict_hello):
#     print("%s%s %s%s" %(rc(r_main), p_title, rc(r_hello), rc(r_empha)))
# elif p_title in r_title[0]:
#     print("%s%s, %s 반갑게 인사해주시면 좋겠어요." %(rc(r_main), p_title, rc(ai_self)))
# else:
#     print("%s%s 내게 인사해줘%s" %(p_title, rc(r_empha), rc(r_empha)))



# rc 반복 -> 구조화
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

    
    # def ai_hello(self):
    #     if any(word in user_input for word in self.response_ai["hello"]["ko"]): # 아래 분기문이 위치하는 것보다 좋아보임.
    #         return rc(self.response_ai["hello"]["ko"])
    #     else:
    #         return rc(self.response_ai["hello"]["en"]) # 다시 분리


    # 0. Dictionary
    # 0-1. Korean
    def ai_dict_ko(self):
        return self.response_ai["ko"]["dict"]
    # 0-2. English
    def ai_dict_en(self):
        return self.response_ai["en"]["dict"]


    # 1. Response AIself
    # 1-1. Korean  
    def ai_title_ko(self):
        return rc(self.response_ai["ko"]["title"])
    
    # 1-2. English  
    def ai_title_en(self):
        return rc(self.response_ai["en"]["title"])
    

    # 2. Response to User
    # 2-1. Korean
    def r_user_ko(self):
        return rc(self.response_user["ko"]["main"])
    def r_title_ko(self):
        return rc(rc(self.response_user["ko"]["title"]))    
    def r_hello_ko(self):
        return rc(self.response_user["ko"]["hello"])    
    def r_empha_ko(self):
        return rc(self.response_user["ko"]["empha"])
    
    # 2-2. English
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
            
    # def user(self, message):
    #     print("* %s: %s" %(self.username, message), end="")
    #     return message
            
    def bot(self, message):
        print("* %s: %s" %(self.botname, message))
        return message

class error:
    def __init__(self):
        self.name = ("* 오류")
        
    def err01(self, message):
        print("%s: %s" %(self.name, message))
        return message


# user's name
username = gu()

# respond from bot
chat = ChatBot(username)

while True:
    
    # input from user
    # user_input = input().strip() # strip 개행

    # if any(word in user_input for word in chat.ai_hello()):
    #     print("%s%s %s%s" %(chat.r_user(), chat.r_title(), chat.r_hello(), chat.r_empha()))
    #     # 클래스의 ai_hello 내부에 분기문을 위치함으로서 삭제
    # 이중 분기화
    # Which = input(">>> 인사 챗봇 Ver.1\n한글 또는 영어 문자를 입력해주세요: ").strip()
    print("-----------------------------------------------------------------------------------")
    print("| * 인사하는 챗봇 Ver.1 (Greeting ChatBot Ver.1)")
    print("| 종료는 '종료'를 입력해주세요. Type 'quit' or 'exit' if you want to stop this.")
    print("| 한/영 중 아무 문자나 입력해주세요. Please input any letters.")
    print("| 입력 문자에 맞는 대화가 가능합니다. You can choose with your letter with language")
    print("| * 종료 입력: 종료, quit, exit")
    print("-----------------------------------------------------------------------------------")
    menu_input = input(">>> ").strip()
    user_input = ""
    
    # if re.fullmatch(r"(quit|exit|종료)", Which):
    if re.fullmatch(r"^(quit|exit|종료)$", menu_input):
        break

        
    # elif re.search(r"[.*+!?^${}()|\[\]\\]", menu_input):
    #     print("문자를 입력해주세요. Please input letter.")
        

    elif menu_input == "":
         continue

        
    # if re.search(r"[ㄱ-ㅎㅏ-ㅣ가-힣]", Which):
    
    elif re.search(r"[ㄱ-ㅎㅏ-ㅣ가-힣]", menu_input):        
        print("[한글] 메뉴로 돌아가려면 '잘있어'를 입력하세요.")
        narrator = say("ko")
        korean = chat.ai_dict_ko()
        narrator.bot("%s%s %s%s" %(chat.r_user_ko(), chat.r_title_ko(), chat.r_hello_ko(), chat.r_empha_ko()))
        
        #while user_input not in ['잘있어']:
        while True:
            print("* 당신: ", end="")
            user_input = input().strip() # strip 개행
            u_title_ko = chat.r_title_ko()
           # language = input("[메뉴] 한글 사용이 맞습니까?(네 또는 예)\n>>> ").strip()     
            # print("korean =", korean)

        # while True:
                
            if user_input == "잘있어":
                 break
            if any(word in user_input for word in korean):
                narrator.bot("%s%s" %(chat.r_hello_ko(), chat.r_empha_ko()))                
            elif u_title_ko in chat.response_user["ko"]["title"][0]:
                narrator.bot("%s%s, %s 반갑게 인사해주시면 좋겠어요." %(chat.r_user_ko(), u_title_ko, chat.ai_title_ko()))                
            elif u_title_ko in chat.response_user["ko"]["title"][1]:
                narrator.bot("%s %s%s" %(u_title_ko, chat.r_hello_ko(), chat.r_empha_ko()))            
            else:
                narrator.bot("이모티콘, 특수기호, 문자 등 제 3의 언어입니다.")

                    
    # elif re.search(r"[A-Za-z]", Which):
    elif re.search(r"[A-Za-z]", menu_input):
        print("[ENG] If you want to go menu, type 'goodbye'")
        narrator = say("en")
        english = chat.ai_dict_en()
        print("%s %s %s%s" %(chat.r_user_en(), chat.r_title_en(), chat.r_hello_en(), chat.r_empha_en()))
        
        # while user_input.lower() not in ['goodbye']:
            # user_input = input("[MENU] Are you sure that you prefer english?(Yes or Y)\n>>> ").strip().lower()

        while True:                
            u_title_en = chat.r_title_en()
            print("* You: ", end="")
            user_input = input().strip() # strip 개행
                
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

            
    else: # 오류 처리
        err = error()
        err.err01("#*(%&Y#@)(*^&!)( 저는 당신의 말을 이해할 수 없어요. I cannot understand your word")
        # err.err01("")
        # err.err01_ko("저는 당신의 말을 이해할 수 없어요.")
        # err.err01_en("I cannot understand your word")
        # continue
