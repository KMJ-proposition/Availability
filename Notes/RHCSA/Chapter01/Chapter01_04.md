# RHCSA (EX200) Exam Preparation Guide
- https://rhcsa.github.io/

## ㄱ. 개요
### Chapter 01
#### 04 - Access remote systems using SSH
- SSH 명령어 학습

#### 목표
- 시스템 관리에 필수적인 원격 접속 도구인 SSH 원리를 이해한다.

#### 주요 명령
- ssh
    - Secure Shell, 네트워크 전송이 암호화 된 원격 접속 도구
- ssh-keygen
    - 인증키 생성
- ssh-copy-id
    - 식별용 공개키 복사 및 전송
- ssh-agent
    - 개인키를 메모리에 할당하는 백그라운드 프로그램
- ssh-add
    - 개인키를 ssh-agent에 등록해준다.
- scp
    - Secure Copy, 파일 전송 내용을 암호화해줌

## ㄴ. 특징
- 공개키, 개인키 관리의 이해
- ssh-copy-id vs ssh-agent
    - ssh-copy-id: 공개키를 호스트에 배포해 호스트에서 나를 검증
    - ssh-agent: 개인키를 클라이언트 메모리에 올려 검증 일부를 생략

## ㄷ. 본문

### SSH 접속
#### 1. 소개
- ssh: SSH 클라이언트용 명령어
- sshd: ssh 데몬에 의해 구동되는 시스템
- 기본적으로 포트 22번 사용

#### 2. 사용
- ssh [계정]@[호스트]
    - 계정: 호스트(접속할 곳)에 존재하는 계정
    - 호스트: IP(자기 자신일 경우 localhost)

- 원격 접속은 집 문을 여는 행위와 같다. 때문에 암호를 요구한다.
    ```
    [root]# ssh examuser@192.168.1.100
    examuser@192.168.1.100's password:
    ```

#### 3. 결과
- 접속 시도
    ```
    [root]# ssh examuser@localhost
    examuser@localhost's password:
    Last login: Fri Apr 13 15:27:35 2017
    [examuser]$
    ```

#### 4. 추가
- 접속 포트가 다를 경우: 옵션을 이용한다.
- ssh [계정]@[호스트] -p [포트 번호]
    ```
    [root]# ssh examuser@192.168.1.100 -p 2525

    # 설명: 이 예시는 접속 포트 번호가 2525일 경우이다.
    ```

### SSH 인증
#### 1. 소개
- 인증이란
    - 사람끼리는 주민등록증 또는 면허증(개인을 식별 가능한 공공 증서)
        - ssh-keygen
    - 호스트와 클라이언트 간 통신을 주고 받겠다는 행위의 근간
        - ssh
    - 공개키를 복사해 호스트로 전송하면 클라이언트 인증을 우회 가능
        - ssh-copy-id
    - 저장 경로
        - 개인키: ~/.ssh/id_rsa
        - 공개키: ~/.ssh/id_rsa.pub
        - 허용 목록: ~/.ssh/authrozied_keys

- SSH의 인증 방식
    - 공개키 암호화 방식으로 인증
    - 정체를 밝히는 공개키와 실제 행위용 개인키가 따로 존재한다.
        ```
        예시) 동네 슈퍼마켓에서 아르바이트하는 국정원 직원
        ```

- SSH의 인증 과정
    - 1. 클라이언트 -> 호스트: 접속 요청
    - 2. 호스트 -> 클라이언트: 공개키 목록 요청
    - 3. 클라이언트 -> 호스트: 공개키 목록 전송
    - 4. 호스트 -> 클라이언트: 공개키 탐색, 서명 요청
    - 5. 클라이언트 -> 호스트: 응답, 개인키로 서명
    - 6. 호스트 -> 클라이언트: 서명을 공개키로 검증
    - 7. 클라이언트: 대기
    - 8. 호스트: 접속 허가

#### 2. 사용
- ssh-keygen -t [dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]
- 옵션 '-t': Type, 타입은 대부분 rsa 또는 ed25519를 사용한다.
- 엔터만 입력시 모두 기본값으로 설정된다.
    ```
    [root]# ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/root/.ssh/id_rsa):
    ```

- ssh-copy-id [사용자]@[호스트]
    ```
    [root]# ssh-copy-id examuser@192.168.1.100
    examuser@192.168.1.100's password:
    ```

- ssh -i [비밀키] [사용자]@[호스트]
    ```
    [root]# ssh -i ~/.ssh/id_rsa examuser@192.168.10.100
    Last login: Tue Feb  3 13:44:49 2026 from ::1
    [examuser]$
    ```

#### 3. 결과
- 공개키를 먼저 복사하여 전송하고 원격 접속을 시도
    - 공개키 복사
        ```
        [root]# ssh-copy-id examuser@192.168.1.100
        /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
        /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
        examuser@192.168.1.100's password:

        Number of key(s) added: 1

        Now try logging into the machine, with:   "ssh 'examuser@192.168.10.130'"
        and check to make sure that only the key(s) you wanted were added.
        ```

    - 접속
        ```
        [root]# ssh examuser@192.168.1.100
        Last login: Thu Mar  7 21:36:25 2005 from ::1
        [examuser]$
        ```

### SSH 설정
#### 1. 소개
- 기본 경로: /etc/ssh/sshd_config
- 사용 권한은 최고 관리자 권한이다.      
- 설정 변경시 항상 데몬을 재시작해주어야 한다.
    - 설정은 보통 동기화되지 않는다.
- 예)
    - 접속에 암호 입력을 차단하고 인증키로만 식별하도록 제한한다.
    - 접속 가능한 계정을 제한한다.

#### 2. 사용
- 설정 변경: 편집기 사용(vi,vim,nano,emacs,gedit...)
- 행 시작 부분의 주석(#)을 반드시 제거해야 설정을 적용할 수 있다.
    ```
    [root]# vim /etc/ssh/sshd_config
    ```

- 설정 후 SSH 데몬 재시작
    ```
    [root]# systemctl restart sshd
    [root]# systemctl status sshd
    ● sshd.service - OpenSSH server daemon
    ...
    ```

#### 3. 결과
- 암호 입력 제한
    - PasswordAuthentication 행 설정
    - 결과: PasswordAuthentication no
        ```
        [root]# ssh examuser@192.168.10.100
        examuser@192.168.10.100: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
        ```

- 공개키로만 식별하도록 제한 
    - PubkeyAuthentication 행 설정
    - 결과: PubkeyAuthentication yes
        ```
        [root]# ssh examuser@192.168.10.100
        examuser@192.168.10.100: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
        ```

- 접속 계정 제한
    - AllowUsers 행 설정
    - 결과: AllowUsers tester
        ```
        [root]# ssh examuser@localhost
        examuser@localhost's password: 
        Permission denied, please try again.

        [root]# ssh tester@localhost
        tester@localhost's password: 
        Last login: Tue Feb  3 14:11:07 2026 from ::1
        [tester]$
        ```

### SSH-AGENT
#### 1. 소개
- 비밀번호를 일일이 입력하지 않아도 된다.
- 위에서 'SSH의 인증 과정'의 4~6번 과정을 생략할 수 있다.
    - 예) 반복 작업에서 내게 필요한 것을 말하지 않아도 건네주는 유능한 사수
    - 내게 필요한 것을 말하는 과정을 생략해준다.
- 상세: 개인키를 확인하려고 소켓을 생성해 불러오는 과정을 생략해준다.

#### 2. 사용
- 조건: 공개키가 공유된 상태와 ssh-add 명령어

- 공개키 확인(클라이언트/호스트)
    ```
    cat ~/.ssh/id_rsa.pub
    ```

- ssh-agent 실행 확인
    ```
    [root]# ssh-agent
    ```

- 개인키 등록
    ```
    [root]# ssh-add ~/.ssh/id_rsa
    Identity added: /root/.ssh/id_rsa (root@RHCSA)
    ```

#### 3. 결과
- 접속
    ```
    [root]# ssh examuser@192.168.10.100
    Last login: Thu Mar  7 21:36:25 2005 from ::1
    [examuser]$
    ```

### SCP
#### 1. 소개
- Secure Copy

#### 2. 사용
- scp [파일] [계정]@[호스트]:[파일]
    ```
    [root]# scp examuser@192.168.10.100:/home/examuser/file /home/test/file

    # 192.168.10.100 호스트의 examuser 계정 file을
    # 나에게 file이라는 이름으로 저장
    ```
    ```
    [root]# scp example.txt examuser@192.168.10.100:/home/examuser/

    # 나의 example.txt 파일을
    # 192.168.10.100 호스트의 examuser 계정 홈 디렉터리에 저장
    ```

#### 3. 결과
- 나의 파일을 다른 곳으로 전송
    ```
    scp pubkey_test examuser@localhost:/home/examuser/
    pubkey_test                                                                        100%  564   299.1KB/s   00:00
    ```

### SSH 오류
- 원인: 데몬 실행 여부, 방화벽 설정, SELinux 설정 등
- 오류시 참조:
    - /var/log/secure
    - /var/log/auth.log

## ㄹ. 기록
- History
    ```
    1032  man ssh-keygen 
    1033  ssh-keygen -t rsa
    1034  ssh examuser@localhost
    1035  ssh-copy-id examuser@localhost
    1036  ssh-keygen
    1037  ssh-copy-id examuser@localhost
    1038  ssh examuser@localhost
    1039  vi ~/.ssh/authorized_keys 
    1040  vi /etc/ssh/sshd_config
    1041  cd /etc/ssh/
    1042  ls
    1043  ll
    1044  date
    1045  date +%y
    1046  date +%Y
    1047  date +%Y%m%d
    1048  date +%Y%m%d\_
    1049  date +%Y%m%d\_+%H%M%S
    1050  date +%Y%m%d\_+%H%M
    1051  date +%Y%m%d\_%H%M
    1052  #cp sshd_config sshd_config.bak_$(date +%Y%m%d\_%H%M)
    1053  pwd
    1054  cp sshd_config sshd_config.bak_$(date +%Y%m%d\_%H%M)
    1055  ll
    1056  cp sshd_config sshd_config.bak_$(date +%Y%m%d%H%M)
    1057  ll
    1058  vi sshd_config
    1059  systemctl restart sshd
    1060  systemctl status sshd
    1061  ssh examuser@localhost
    1062  man ssh-agent 
    1063  eval
    1064  eval $(ssh-agent)
    1065  man eval
    1066  ssh-agent
    1067  man ssh-agent 
    1068  ssh-add --help
    1069  man ssh-add
    1070  echo $SSH_AGENT_PID
    1071  echo $SSH_AUTH_SOCK
    1072  ssh examuser@localhost
    1073  vi /etc/ssh/sshd_config
    1074  systemctl restart sshd && systemctl status sshd
    1075  ssh examuser@localhost
    1076  ssh-add ~/.ssh/id_rsa
    1077  ssh examuser@localhost
    1078  echo $SSH_AGENT_PID 
    1079  echo $SSH_AUTH_SOCK
    1080  ssh-agent
    1081  ssh examuser@localhost
    1082  vi /etc/ssh/sshd_config
    1083  systemctl restart sshd && systemctl status sshd
    1084  ssh examuser@localhost
    1085  vi /etc/ssh/sshd_config
    1086  wc ~/.ssh/id_rsa.pub 
    1087  vi ~/.ssh/id_rsa.pub 
    1088  vi /etc/ssh/sshd_config
    1089  systemctl restart sshd && systemctl status sshd
    1090  cat ~/.ssh/id_rsa.pub > ~/pubkey_test
    1091  diff ~/.ssh/id_rsa.pub ~/pubkey_test
    1092  pwd
    1093  cd
    1094  cat pubkey_test >> /home/examuser/.ssh/authorized_keys 
    1095  vi /etc/ssh/sshd_config
    1096  systemctl restart sshd && systemctl status sshd
    1097  ssh examuser@localhost
    1098  systemctl stop sshd
    1099  ssh-agent
    1100  systemctl start sshd
    1101  docker images
    1102  man scp
    1103  man ssh\
    1104  man ssh
    1105  ssh -i ~/.ssh/id_rsa examuser@localhost
    1106  vi /etc/ssh/sshd_config
    1107  systemctl start sshd
    1108  systemctl restart sshd
    1109  last
    1110  last -s1 -n
    1111  last -n1
    1112  last -s+2days
    1113  last -s-2days
    1114  ssh tester@localhost
    1115  ssh examuser@localhost
    1116  ll
    1117  scp pubkey_test examuser@localhost:/home/examuser/
    1118  vi /etc/ssh/sshd_config
    1119  systemctl restart sshd
    1120  scp pubkey_test examuser@localhost:/home/examuser/
    1121  getenforce
    1122  compgen -c | grep context
    1123  history
```