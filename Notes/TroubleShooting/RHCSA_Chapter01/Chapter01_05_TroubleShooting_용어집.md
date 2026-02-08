# 용어 및 특징
## cron
* 특정 시간에 명령이나 스크립트를 실행하도록 관리하는 데몬

## Framework(프레임워크)
* 양식을 토대로 작성한 무엇이 동작하게 만드는 구조 또는 틀이다.
* 개발자가 따라야 할 양식을 제공하고 그 흐름에 맞게 통제한다.

## GDM(GNOME Desktop Manager)
* 하드웨어 세션(seat0)의 기본 콘솔(tty1)을 점유하고 있다.
* systemd 기반 그래픽 환경의 리눅스에서는 보통 tty1에서만 실행되도록 설계되어 있다.

## getty
* 콘솔에서 로그인 화면을 띄우는 프로그램이다.
* 인증 전 로그인 프롬프트를 제공하고, 인증 후에는 역할이 종료된다. 
* 동작 흐름
    1. systemd가 getty 서비스 실행 --> 연결된 tty 대기
    2. 사용자명 입력 --> /bin/login 실행 및 getty 분리(역할 끝)
    3. /bin/login의 PAM 호출 --> 인증 요청 --> PAM에 설정된 모듈을 순서대로 실행
    4. 인증 성공시 /bin/login이 셸 실행

## PAM(Pluggable Authentication Modules)
* 리눅스의 인증 시스템을 모듈화한 프레임워크이다.
* 리눅스에서 사용자 인증이 필요한 거의 모든 프로그램이 PAM을 통해 인증 받는다.
* 크게 세 구조로 이루어져 있다.
    1. PAM aware Application: PAM 인증이 필요함을 알고 있는 프로그램
    2. PAM Library: 인증 수행 모듈(pam_unix.so, pam_faillock.so 등)
    3. PAM 설정 파일: 각 프로그램이 어떤 모듈을 어떤 순서로 사용할 지 정의
* 4단계 설정을 필요로 한다.
    1. auth: 암호 등으로 사용자 인증
    2. account: 사용 가능 등의 계정 상태 확인
    3. password: 암호 변경 정책
    4. session: 로그인과 로그아웃 시 실행하는 작업
* 동작 흐름(CLI)
    1. 사용자 입력 --> /sbin/agetty(=getty) --> /bin/login
    2. /bin/login --> PAM에게 인증 요청 --> PAM 설정 확인
    3. PAM이 설정된 모듈을 순서대로 실행 --> 인증 검사
    4. 인증~ 성공시 로그인 shell 실행, 실패시 오류 출력
* 동작 흐름(GUI)
    1. 사용자 입력 --> GDM이 gdm/password(PAM 설정 파일)를 참조
    2. gdm/password에 정의된 모듈을 순서대로 실행 --> PAM 인증 수행
    3. 인증 성공시 GNOME 세션 시작, 실패시 오류 출력
* 동작 비교(CLI vs GUI)
    1. CLI: getty --> login(PAM) --> shell(tty2~tty6)
    2. GUI: GDM --> PAM 인증 --> GNOME 세션(tty1)
* 동작 비교(Copilot)
    1. CLI: getty → login(PAM) → shell (tty2~tty6)
    2. GUI: GDM → PAM 인증 → GNOME 세션 (tty1)
* 중요성
    1. 로그인 실패 횟수 제한
    2. 계정 잠금
    3. OTP(2FA)
    4. LDAP/AD 인증 연동
    5. sudo 정책 강화
    6. root 로그인 제어
    7. SSH 인증 방식 제어 등

## Service(서비스)
* 시스템 기능 구성의 단위
* 컴퓨터 시스템에서 지속적으로 제공되는 기능이다.
* 백그라운드 프로세스로서 리눅스에서는 데몬, 윈도우에서는 서비스라고 부른다.
* 동작 순환
    1. 요청 대기
    2. 요청 응답
    3. 요청 처리

## session(세션)
* 상호작용이 이루어지는 시기를 의미한다.

## tty(teletypewriter)
* 옛날 전신 타자기로 단순 입출력 장치이며, 컴퓨터 등장 초기에 콘솔이라고 불렸다.
* 리눅스에서는 가상 콘솔로 구현한다.
* 텍스트 기반 로그인 환경에서는 getty가 관리한다.
* target 5(runlevel 5) 환경에서는 GDM이 tty1를 점유하고 있으므로 tty2부터 시작한다.
* target 5(runlevel 5) 환경이 비활성화 되면 텍스트 콘솔로 돌아간다.

<!--
## tripwire
-->