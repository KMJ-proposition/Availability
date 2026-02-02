# RHCSA \(EX200\) Exam Preparation Guide
- Original: https://rhcsa.github.io/

## ㄱ\. 소개
### Chapter 01
- 01\. Understand and user essential tools
   - 01 \- Access a shell prompt and issue commands with correct syntax

### Commands \|\| Files
- tty
   - 사용중인 셸 확인
- ssh
   - 원격 접속
- sudo
   - 관리자 권한으로 명령어 실행
- cat
   - 파일의 내용 확인
- History
   - 명령줄 실행 기록
- 편집기(Editor)
   - vim, nano, emacs

## ㄴ\. 후기
- 기초와 기본을 쌓으라고들 말한다.

## ㄷ\. 본문

### 1\. Accessing the Shell Prompt
#### 현재 사용중인(입력중인) 터미널 확인
- tty
   ```
   root# tty
      /dev/pts/1
   ```

### 2\. Using the Bash Shell
#### 2\-1\. 새로운 계정 생성 및 비밀번호 변경
- useradd, passwd
   ```
   root# useradd examuser     # 새로운 계정의 생성
   root# passwd examuser      # 존재하는 계정의 비밀번호 변경
      examuser 사용자의 비밀 번호 변경 중
   새 암호:
      잘못된 암호: 암호에 사용자 이름이 들어 있습니다
   새 암호 재입력:
      passwd: 모든 인증 토큰이 성공적으로 업데이트 되었습니다.
   ```

#### 2\-2\. 새로운 계정으로 원격 접속
- ssh
   ```
   root# ssh examuser@localhost
   examuser@localhost's password:
      Last failed login: xxx xxx xx x2:4x:x6 KST 202x from ::x on ssh:notty
      There were x failed login attempts since the last successful login.
   ```

#### 2\-3\. 새로운 계정에서 명령줄 실행
- cd /var/log
   ```
   examuser$ cd /var/log		# 로그 기록 보관소
      ls -a		# list --all, 모든 파일(숨김 파일까지) 확인
      .                  cron-202xxxxx        mail               secure-202xxxxx       vmware-network.x.log
      ...
   ```
#### 2\-4\. 새로운 계정에서 디렉터리 생성 및 삭제
- mkdir, rmdir
   ```
   examuser$ mkdir ~/testdir		# 디렉터리 생성
   examuser$ rmdir ~/testdir		# 디렉터리 삭제
   ```

### 3\. Understanding Command Syntax
- 명령어 입력 순서: 사용자$ \[명령어] \[옵션] \[인자]
   ```
   examuser$ cd --                            # 바로 이전 경로로 이동
   examuser$ grep -v hello /var/log/secure    # hello를 제외한 문자열 출력
   ```

### 4\. Using Basic File Manipulation Commands
#### 4\-2\. cp
- copy
   - 일반 파일은 내용을 복사한다.
   - 문자/블록 디바이스의 경우 디바이스 노드 정보를 복사해 새로이 생성한다.
   - 단, 복사 불가능 또는 의미 없는 경우:
   - 파일 시스템, 하드링크 구조(inode), 특수 파일(IPC, Socket), 고유 플래그(..attr)
#### 4\-3\. mv
- move
   - 파일을 이동한다.
   - 리눅스는 모든 것이 파일이다.
   - 때문에 디렉터리 또한 파일로 취급하여 mv 명령어로 이동 가능하다.

#### 4\-4\. rm
- remove
   - 파일을 삭제한다.

### 5\. Using Wildcards and Special Characters
- 와일드카드\(\*\)를 사용해보자.
   ```
   examuser$ ls /var/log/m\*
      /var/log/maillog           /var/log/maillog-202xxxxx  /var/log/messages-202xxxxx  /var/log/messages-202xxxxx
      ...

   # m이 0개 이상이므로 m을 포함한 모든 문자열을 출력한다.
   ```

### 6\. Running Commands as Root (Using sudo)
- sudo
   ```
   examuser$ sudo yum install httpd

      로컬 시스템 관리자에게 일반적인 지침을 받았으리라 믿습니다.
      보통 세가지로 요약합니다:

      #1) 타인의 사생활을 존중하십시오.
            #2) 입력하기 전에 한 번 더 생각하십시오.
            #3) 막강한 힘에는 상당한 책임이 뒤따릅니다.

      [sudo] examuser의 암호:
         examuser은(는) sudoers 설정 파일에 없습니다.  이 시도를 보고합니다.
            # sudoers에 등록되지 않은 사용자는 사용할 수 없다.
   ```
   
### 7\. Viewing and Editing Files
- cat
   - concatenate
   - File Descriptor 1번인 일반 출력으로 파일의 내용을 출력한다. 0번은 입력, 2번은 에러(표준)
   ```
   examuser$ cat /etc/passwd
      ...
      tester:x:10000:10000:테스트용 계정:/home/tester:/bin/sh
      nginx:x:984:984:Nginx web server:/var/lib/nginx:/sbin/nologin
      examuser:x:10001:10001::/home/examuser:/bin/bash
   ```
#### 7\-2\. less\, more
- less, more
   - 파일의 내용을 화면 단위로 보여주며 화면 이동·검색과 같은 기능이 있다.

#### 7\-3\. Editor(편집기)
- Editor(편집기)
   ```
   - vi by Bill Joy
   - vim by Bram Moolenaar
   - nano by Chris Allegretta
   - emacs by Richard Matthew Stallman
   ```
   ```
   vi ./vi_test.txt
   vim ~/vim_test.md
   nano /nano_test.log
   emacs /tmp/emacs_test
   ```

### 8\. Using Command History and Autocompletion
- history
   - 입력한 명령어의 기록, 기록을 검색해 재사용 하거나 갯수 제한 등 설정 가능
- \!\!
   - history 목록에서 가장 최근 사용했던 명령을 실행한다.
- \!23
   - CLI가 목록에 저장된 23번 명령어를 읽어와줌. 화살표 키 위를 누르면 23번 명령어를 입력해줌.

## ㄹ. 명령줄 실행 기록
- user: examuser
   ```
   1007  tty
   1008  su - examuser
   1009  tty
   1010  ssh examuser@localhost
   1011  su - rocky
   1012  man cat
   1013  man cp
   1014  mknod /dev/mydevice b 8 0
   1015  fdisk -l
   1016  ls -l /dev/mydevice
   1017  ls -l /dev/sda
   1018  stat /dev/mydevice
   1019  stat /dev/sda
   1020  udevadm info -a -p $(udevadm info -q path -n /dev/mydevice)
   1021  udevadm --help
   1022  man udevadm
   1023  ㄱㄷㅁㅇ
   1024  read
   1025  read(fd, buf, size)
   1026  stat
   1027  stat --help
   1028  man stat
   1029  compgen -c | grep read
   1030  compgen -c | grep write
   1031  read --help
   1032  read(fd, buf, size)
   1033  su - examuser
   1034  vi /etc/hosts
   1035  su - examuser
   1036  history
   ```