# RHCSA을 향하여
* [RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 05 - Log in and switch users in multiuser targets

TODO:
1. 세션
2. 인증 구조
3. ...

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - 다중 사용자와 인증
#### 학습 목표
1. 다중 사용자의 개념 학습
2. 리눅스의 인증 구조 학습

#### 특징
* 서버의 구동 환경에 따라 로그인 가능한 사용자 수가 달라진다.
* 운영 목적에 따라 대상을 달리하여 로그인 수를 제한할 수 있다.
* 서브커맨드 입력에 따라 서비스가 제한될 수 있다.

#### 주요 명령
* su
    - Switch User
    - 특정 사용자로 셸 프로세스 실행

* sudo
    - Super User Do
    - root 권한으로 특정 명령어나 프로그램을 실행한다.
    - 실행이 기록된다.

* visudo
    - vi 편집기로 sudo 설정 파일에 접근

* systemctl
    - systemd를 기반으로 모든 서비스의 동작 여부를 관리

* passwd
    - password
    - 사용자의 상태·암호·암호의 사용 기한 등 인증 토큰을 변경
        + 인증 토큰: 사용자 암호 및 계정 잠금/만료 상태를 의미한다.
        + PAM이 관리하는 사용자 인증 정보 전체를 의미한다.

* w, who
    - 현재 접속중인 사용자를 출력

* exit, logout
    - 입력하는 창(세션) 종료

***

## ㄴ. 본문
### 사용자 변경과 root 권한
* su [사용자]
    - 입력한 사용자로 새로운 셸 프로세스를 실행한다.
    - '-'를 옵션으로 지정해 해당 사용자의 셸 환경을 불러온다.

* sudo [명령어 또는 프로그램]
    - root 권한으로 명령어 또는 프로그램을 실행한다.
    - 권한 유무와 관계없이 실행하면 기록된다.
        + 기록 장소: /var/log/secure
    - '-i' 옵션을 지정해 관리자의 환경 변수를 불러온다. 
    - 요청할 수 있는 범위 등을 관리자가 미리 지정해주어야 한다.

* 실행: 
    - su - examuser
        + 사용자의 모든 설정을 탑재하여 examuser로써 접속한다.
            ```bash
            su - examuser
            암호:
            마지막 로그인: 수  2월  4 15:48:42 KST 2026 일시 pts/1
            ```

    - sudo systemctl restart sshd
        + root 권한으로 ssh 데몬을 재실행 한다.
            ```bash
            sudo systemctl restart sshd
            [sudo] examuser의 암호:
            ```

    - 권한이 부족할 경우의 기록
        ```bash
        tail /var/log/secure
        Feb  4 16:22:32 RHCSA polkitd[849]: Unregistered Authentication Agent for unix-process:11434:855278 (system bus name :1.513, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale ko_KR.UTF-8) (disconnected from bus)
        ```

---

### root 권한 접근 설정
* visudo
    - vi + sudo(편집 + sudo)
    - sudoers 설정 파일을 편집하기 위해 접근하는 명령어이다.
    - 안전을 위해 편집된 파일의 기본 검증이나 문법 오류를 검사한다.
        ```bash
        visudo
        경고: /etc/sudoers:124:23: Cmnd_Alias "WOW"을(를) 참조했지만 정의하지 않았습니다
        ```

* sudoers
    - sudo의 보안 정책 플러그인
        + 플러그인: plugin, 
    - sudo를 통해 사용할 수 있는 명령어 접근 정책을 설정한다.

* 실행:
    - visudo
        + sudoers 설정을 변경한다.
        + 맨 아랫줄에 내용을 추가한다.
        + examuser에게 모든(ALL) 행위를 관리자 권한으로 실행할 수 있게 허가한다.
            ```bash
            ## Custom
            examuser    ALL=(ALL)   ALL
            ```
    - systemctl restart sshd
        + 설정 전
            ```bash
            sudo systemctl restart sshd
            [sudo] examuser의 암호: 
            examuser은(는) sudoers 설정 파일에 없습니다.  이 시도를 보고합니다.
            ```
        + 설정 후
            ```bash
            sudo systemctl restart sshd 
            [sudo] examuser의 암호: 
            ```

---

### 서비스 조작
* systemctl
    - systemd를 기반으로 모든 서비스를 관리하는 명령어이다.
    - 시스템 데몬(systemd)과 각종 시스템 및 서비스를 관리·설정한다.
    - systemctl [서브커맨드] [대상]
    - 서브커맨드:
        + get-default
        + 현재 지정된 runlevel을 출력한다.
        + isolate [대상]
            + runlevel을 대상으로 지정하며, 대상에 포함되지 않은 실행중인 모든 서비스를 즉시 종료한다.
        + set-default [대상]
            + runlevel을 대상으로 지정한다.

* target(runlevel의 확장)
    - systemd는 runlevel 대신 target 개념을 사용한다.
    - target은 runlevel을 확장한 서비스 그룹이다.
        + runlevel: 각 단계에 따라 서버의 구동 환경이 달라진다.
    - 하나의 서버에 접속 가능한 수를 제한할 수 있음
    - multi-user.target
        + 다중 사용자(multi user)가 하나의 서버에 접속하게 한다.
        + 기본값은 runlevel 3
    - graphical.target
        + 다중 사용자가 접근 가능하면서 UI와 같은 그래픽 환경을 사용할 수 있게 한다.


* 실행:
    - systemctl get-default
        ```bash
        systemctl get-default
        graphical.target
        ```

    - systemctl set-default
        ```bash
        sudo systemctl set-default multi-user.target 
        [sudo] examuser의 암호: 
        Removed "/etc/systemd/system/default.target".
        Created symlink /etc/systemd/system/default.target → /usr/lib/systemd/system/multi-user.target.
        ```

    - systemctl isolate
        ```bash
        sudo systemctl isolate multi-user.target 
        [sudo] examuser의 암호: 
        ```
        + CLI 환경으로 바뀐다.
            ```bash
            Rocky Linux 9.7 (Blue Onyx)
            Kernel ...

            Activate ...

            RHCSA login: 
            ```

---

### 사용자 암호
* passwd
    - 사용자의 암호, 사용 가능 상태 등 인증 토큰을 변경한다.
    - 보통 사용자의 계정 암호만 변경 가능하다.
    - 관리자는 모든 계정의 암호나 상태 등을 변경할 수 있다.
    - RHEL9 기본 정책 기준에 따른다.
        + 암호는 최소 8자 이상, 대문자/소문자/숫자/특수문자 중 3종류를 포함해야 한다.
        + 이를 '암호의 복잡성을 만족한다'고 한다.
        + 사용자 계정명 또는 사전에 포함된 단어는 금지한다.

* passwd [계정명]
    - 옵션 없음: 사용자의 암호를 변경한다.
        + 관리자
            ```bash
            passwd examuser
            examuser 사용자의 비밀 번호 변경 중
            새 암호:
            새 암호 재입력:
            passwd: 모든 인증 토큰이 성공적으로 업데이트 되었습니다.
            ```
        + 사용자
            ```bash
            passwd
            examuser 사용자의 비밀 번호 변경 중
            Current password: 
            새 암호:
            새 암호 재입력:
            passwd: 모든 인증 토큰이 성공적으로 업데이트 되었습니다.
            ```

    - -l: 사용자의 계정을 잠근다.
        + 관리자
            ```bash
            passwd -l examuser
            examuser 사용자의 비밀 번호를 잠급니다
            passwd: 성공
            ```
        + 사용자
            ```bash
            telnet -4 localhost -l examuser
            Trying 127.0.0.1...
            Connected to localhost.
            Escape character is '^]'.
            Password: 
            Login incorrect
            ```

    - -u: 사용자의 계정 잠금을 해소한다.
        + 관리자
            ```bash
            passwd -u examuser
            examuser 사용자의 비밀 번호 잠금 해제 중
            passwd: 성공
            ```
        + 사용자
            ```bash
            telnet -4 localhost -l examuser
            Trying 127.0.0.1...
            Connected to localhost.
            Escape character is '^]'.
            Password: 
            Last failed login: Wed Feb  4 16:57:54 KST 2026 from localhost on pts/2
            There were 2 failed login attempts since the last successful login.
            Last login: Wed Feb  4 16:56:21 from ::1
            [examuser]$
            ```

    - -e: 사용자의 암호 토큰을 폐기하고 변경을 요청한다.
        + 관리자
            ```bash
            passwd -e examuser
            사용자 examuser의 비밀 번호를 만료 중.
            passwd: 성공
            ```
        + 사용자
            ```bash
            telnet -4 localhost -l examuser
            Trying 127.0.0.1...
            Connected to localhost.
            Escape character is '^]'.
            Password: 
            You are required to change your password immediately (administrator enforced).
            Current password: 
            New password: 
            Retype new password: 
            Last login: Wed Feb  4 17:01:39 from localhost
            
            ```

---

### w, who
* w
    - 현재 접속중인 사용자의 접속 환경과 상태를 대략적으로 출력한다.
    - USER
        + 접속중인 사용자
    - TTY
        + tty: 로컬 환경에서 접속(서버 node를 통해 접속)
        + pts: 원격 환경에서 접속(다른 node를 통해 접속)
    - LOGIN@
        + 접속 시간
    - JCPU
        + 해당 TTY에서 실행된 모든 프로세스의 CPU 사용량 합계
    - PCPU
        + 현재 실행 중인 WHAT 프로세스 하나의 CPU 사용량

* who
    - 접속중인 사용자 계정, 사용 환경, 접속 일자, 접속 유지시간을 출력한다.

* 실행:
    - w
        + seat0: GDM이 사용하는 세션이며, 좌석으로 표현한다.
        + tty2: 2번째 가상 콘솔(Ctrl+Alt+F2)
            ```bash
            w
            17:15:48 up  3:15,  3 users,  load average: 0.00, 0.03, 0.01
            USER     TTY        LOGIN@   IDLE   JCPU   PCPU  WHAT
            root     seat0      15:08    0.00s  0.00s  0.00s /usr/libexec/gdm-wayland-session --register-session gnome-session
            root     tty2       15:08    3:21m  0.03s  0.03s /usr/libexec/gnome-session-binary
            ```

    - who
        + seat0: GDM이 사용하는 세션이며, 좌석으로 표현한다.
        + tty2: 2번째 가상 콘솔(Ctrl+Alt+F2)
            ```bash
            who
            root     seat0        2026-02-04 15:08 (login screen)
            root     tty2         2026-02-04 15:08 (tty2)
            ```

---

### exit, logout
* exit
    - 현재 셸 세션을 종료한다.

* logout
    - 현재 셸 세션을 종료한다.
    - 로그인 셸에만 제공하는 명령어이다.
    - GUI 터미널은 로그인 셸이 아니다. 따라서 이 명령어가 없다.

* 실행:
    - exit
        ```bash
        exit
        ```
    - logout
        ```bash
        logout
        ```

***

## ㄷ. 기록
* History
    ```
    1016  2026-02-04 16:41:55 man passwd
    1017  2026-02-04 16:54:05 passwd examuser
    1018  2026-02-04 16:56:04 passwd -l examuser
    1019  2026-02-04 17:01:16 passwd -u examuser
    1020  2026-02-04 17:03:02 passwd -e examuser
    1021  2026-02-04 17:11:25 w
    1022  2026-02-04 17:15:02 man w
    1023  2026-02-04 17:15:34 w
    1024  2026-02-04 17:16:11 man
    1025  2026-02-04 17:16:13 who
    1026  2026-02-04 17:21:57 history
    ```