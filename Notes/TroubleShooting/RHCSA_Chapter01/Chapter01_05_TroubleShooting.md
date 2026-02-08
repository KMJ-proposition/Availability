# 터미널 로그인 문제 해결
* 인증의 무결성 훼손과 대책 수립
<!--
TODO(아마도):
3. tripwire 설치
4. 시각화
-->

## ㄱ. 개요
* systemctl 서브커맨드 사용 중 발생한 로그인 불가 문제를 해결
* 계정 점검 명령어를 통해 원인을 진단
* 서버의 백업 활용이 불가능 할 때, 원격으로 접속해 문제를 해결
* 점검 스케쥴링을 통한 재발 방지

### 문제
* 발생 시각
    - 2026년 02월 04일 오후 12시 30분 경

* 해결 시각
    - 2026년 02월 04일 오후 14시 30분 경

* 발생 경로
    - 명령어 입력 후 로그인 시 'login incorrect'라는 문구가 출력됨
    - 이는 로그인 불가를 의미하여 서버 로그인 시스템에 문제가 생겼음을 확인

* 주요 증상
    - 문제의 서버가 isolate multi-user 대상 시스템에서 로그인 불가
        ```bash
        [examuser]$ systemctl isolate multi-user.target
        ```
    - ![문제 발생](Chapter01_05_TroubleShooting_MainServer_01.png)

* 문제 인식
    - 동일 커널 버전 다른 릴리즈의 리눅스 서버에서 정상 로그인됨을 확인
        + 문제의 서버: Rocky 9.7(Linux RHCSA 5.14.0-611.20.1.el9_7.x86_64)
        + 실험용 서버: Rocky 9.6(Linux Rocky 5.14.0-570.17.1.el9_6.x86_64)

* 초동 대처
    - 문제가 발생한 서버를 종료하지 않고 문제 해결 시도
    - 실험용 서버에서는 정상 작동 확인
    - 문제의 서버로 원격 접속 성공하여 해결 진행

### 원인
* PAM의 설정 파일인 login 파일의 무결성이 변조된 이력이 발견되었음 

### 주요 명령어
* systemctl
    - 시스템 대부분의 서비스를 총괄하는 명령
* man
    - 명령어의 상세 설명서
* vim
    - 파일 내용 편집

### 활용 도구 등
* Microsoft Copilot(Personal)
    - 원인 탐색 및 해결책 제시
    - 문서 검토
* RedHat Rocky Linux 9.6(Linux Rocky 5.14.0-570.17.1.el9_6.x86_64)
    - 정상 동작 시스템

***

## ㄴ. 해결
### 원인
* 과거 PAM 설정에 securetty.so 파일이 삽입되었고 이를 관리하지 않았음. 이에 따라 login 파일의 무결성이 훼손되었음을 확인

### 영향
* 로컬에서 root 계정이 로그인할 수 있는 터미널을 제한한다.

### 대책
* 재발 방지를 위한 사후책
    - 설정 파일 무결성 검사를 위한 cron 스케쥴링
    - 
    ```bash
    crontab -l
    ...
    * 0 * * *	bash	/root/rec001_pam01.sh
    ```

***

## ㄷ. 대처
* 대응 절차를 시간 순서로 기술
* 실험용 환경에서 원격으로 진행
    - Linux Rocky 5.14.0-570.17.1.el9_6.x86_64

### 1. 서비스 점검
#### 서버 대조
* 정상 실행 및 로그인 가능 확인
    ```bash
    systemctl isolate multi-user.target
    ```
#### 서비스 상태 확인
* getty@tty1.service 강제 실행
    - 로그인 불가
#### 원격 접속 여부
* ssh 원격 접속 실행
    ```
    ssh root@192.168.10.130
    root@192.168.10.130's password: 
    Activate the web console with: systemctl enable --now cockpit.socket

    Last failed login: Wed Feb  4 13:58:45 KST 2026 on tty1
    There was 1 failed login attempt since the last successful login.
    Last login: Wed Feb  4 13:55:52 2026
    ```

### 2. 계정 관련 점검
#### PAM 설정 확인
* 로컬 로그인 가능 여부를 확인하였으나 기본값으로 설정되어 있었음
    ```
    vi /etc/pam.d/login
    ```
#### 계정 잠김 여부 확인
* lslogins
    - 'PWD-LOCK' 열을 확인하였으나 사용 계정이 잠기지 않았음을 확인
        - 0의 경우: 계정 잠기지 않음
        - 1의 경우: 계정 잠김
        ```
          UID USER                 PROC PWD-LOCK PWD-DENY
            0 root                    0        0        0
              ...
         1000 rocky                   0        0        0 
         1004 ExamUser                0        0        0              
        10000 tester                  0        0        0
        10001 examuser                0        0        0
        ```

---

### 3. PAM 설정 재확인
* PAM의 login 파일의 변조 기록 확인
    - rpm 명령어의 검증(-V) 옵션 사용
    - rpm -V util-linux
        ```
        rpm -V util-linux
        S.5....T.  c /etc/pam.d/login
        ```
    - 출력되면 원본 패키지에서 변조가 일어났음이 출력된 것
        + S: 파일 크기
        + 5: MD5 Checksum
        + T: 갱신일
        + .: 변조 없음

---

### 4. 패키지 재설치
* 진행
    - 패키지 재설치 시엔 설정 파일을 덮어쓰지 않기에 기존 파일을 분리 후 진행
    - 원본: /etc/pam.d/login.bak

* 실행
    ```bash
    cd /etc/pam.d/
    mv [재설치 파일] [원본]
    dnf reinstall util-linux
    ```

* 결과
    - ![문제 해결](Chapter01_05_TroubleShooting_MainServer_02.png)

---

### 5. Cron 스케쥴링


***

## ㄹ. 경과
* 약 3시간 문제 발견 또는 재발하지 않음
* 후속 조치로써 재발 방지 cron 스케쥴링을 실시함

***

## ㅁ. 후기
### 느낀점
* 시간
    1. 관련 지식이 없으면 탐색 범위가 넓어 오래 걸린다.
    2. 배울 건 널렸고, 시간은 한정되어 있다.
    3. 과거 흔적은 남아있고, 지금껏 영향을 준다.
    4. 벽 앞에서 앓지 말고, 인공지능을 활용하자.

### 배운점
* runlevel3에서는 securetty 파일을 사용하였으며, 이는 isolate multi-user에서 로그인할 수 없는 결과를 초래하였다. 반면 GDM에서는 사용하지 않으며 영향이 없었다.

* Timestamp
    - 명령어 사용 시각을 알기 위해 history에 시간 출력을 적용해두어야 한다.
        ```
        echo -e '# history timestamp\nexport HISTTIMEFORMAT="%F %T "' >> ~/.bashrc
        source ~/.bashrc
        history | tail -n 1
         1009  2026-02-04 15:11:26 history | tail -n 1
        ```

***