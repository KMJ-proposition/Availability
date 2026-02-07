# RHCSA을 향하여
* [참고 문서: RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
   - Chapter 01) Understand and user essential tools
   - 01 - Access a shell prompt and issue commands with correct syntax

* 활용 도구: Microsoft Copilot
    - 단어 선택
    - 기입 제안
    - 문서 검토

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - Shell의 기본 명령어
#### 학습 목표
1. 기본 명령어 학습

#### 특징
* 자주 사용되는 기본 명령어

#### 주요 명령
* tty
   - 사용중인 셸 확인
* ssh
   - 원격 접속
* sudo
   - 관리자 권한으로 명령어 실행
* cat
   - 파일의 내용 확인
* History
   - 명령줄 실행 기록
* 편집기(Editor)
   - vim, nano, emacs

***

## ㄴ. 본문
### 명령어 입력
* 명령어란
   - 명령을 시스템에 전달하는 역할을 하는 프로그램

* 사용자$ \[명령어] \[옵션] \[인자]
   ```
   cd --                            # 바로 이전 경로로 이동
   grep -v hello /var/log/secure    # hello를 제외한 문자열 출력
   ```

### 터미널 확인
* 현재 사용중인(입력중인) 터미널을 확인한다.
   ```bash
   tty
   /dev/pts/1
   ```

### 계정 생성과 암호 변경
* useradd
   - 새로운 계정의 생성
   - useradd [계정]

* passwd
   - 계정의 암호 변경
   - passwd [암호]

* 실행:
   ```bash
   useradd examuser
   passwd examuser
      examuser 사용자의 비밀 번호 변경 중
   새 암호:
      잘못된 암호: 암호에 사용자 이름이 들어 있습니다
   새 암호 재입력:
      passwd: 모든 인증 토큰이 성공적으로 업데이트 되었습니다.
   ```

### 원격 접속
* ssh
   - 원격 접속 명령어
   - ssh [계정]@[주소]

* 실행:
   ```bash
   ssh examuser@localhost
   examuser@localhost\'s password:
      Last failed login: xxx xxx xx x2:4x:x6 KST 202x from ::x on ssh:notty
      There were x failed login attempts since the last successful login.
   ```

### 명령줄 실행
* cd
   - Change Directory
   - 현재 경로를 변경한다.

* ls
   - List
   - 파일 목록을 출력
   - '-a' 옵션: --all, 모든 파일(숨김 파일까지) 확인

* 실행:
   ```bash
   cd /var/log
      ls -a
      .     cron-202xxxxx     mail     secure-202xxxxx      vmware-network.x.log
      ...
   ```

### 디렉터리 생성 및 삭제
* mkdir
   - 디렉터리 생성

* rmdir
   - 디렉터리 삭제

* 실행:
   ```bash
   mkdir ~/testdir
   rmdir ~/testdir
   ```

### 파일 복사, 이동, 삭제
* copy
   - 일반 파일은 내용을 복사한다.
   - 문자/블록 디바이스의 경우 디바이스 노드 정보를 복사해 새로이 생성한다.
   - 단, 복사 불가능 또는 의미 없는 경우:
   - 파일 시스템, 하드링크 구조(inode), 특수 파일(IPC, Socket), 고유 플래그(..attr)

* move
   - 파일을 이동한다.
   - 리눅스는 모든 것이 파일이다.
   - 때문에 디렉터리 또한 파일로 취급하여 mv 명령어로 이동 가능하다.

* remove
   - 파일을 삭제한다.

### 와일드카드(*)
* m이 0개 이상이므로 m을 포함한 모든 문자열을 출력한다.
   ```
   ls /var/log/m\*
   /var/log/maillog     /var/log/maillog-202xxxxx     /var/log/messages-202xxxxx    /var/log/messages-202xxxxx
   ...
   ```

### 관리자 권한으로 실행
* sudo
   ```
   sudo yum install httpd

      로컬 시스템 관리자에게 일반적인 지침을 받았으리라 믿습니다.
      보통 세가지로 요약합니다:

            #1) 타인의 사생활을 존중하십시오.
            #2) 입력하기 전에 한 번 더 생각하십시오.
            #3) 막강한 힘에는 상당한 책임이 뒤따릅니다.

      [sudo] examuser의 암호:
         examuser은(는) sudoers 설정 파일에 없습니다.  이 시도를 보고합니다.
            # sudoers에 등록되지 않은 사용자는 사용할 수 없다.
   ```
   
### 파일의 내용 출력
* cat
   - concatenate
   - File Descriptor 1번인 일반 출력으로 파일의 내용을 출력한다. 0번은 입력, 2번은 에러(표준)

* 실행:
   ```bash
   cat /etc/passwd
      ...
      tester:x:10000:10000:테스트용 계정:/home/tester:/bin/sh
      nginx:x:984:984:Nginx web server:/var/lib/nginx:/sbin/nologin
      examuser:x:10001:10001::/home/examuser:/bin/bash
   ```

* less, more
   - 파일의 내용을 화면 단위로 보여주며 화면 이동·검색과 같은 기능이 있다.

### 명령어 실행 기록
* history
   - 입력한 명령어의 실행 기록
   - 기록을 검색해 재사용 하거나 갯수 제한 등 설정 가능

* \!\!
   - 가장 최근 명령줄을 실행한다.
   
* \!23
   - 목록의 23번 명령줄을 읽어옴.


### Editor(편집기)
* Editor(편집기)
   - 기본 4개가 있다.
      + vi by Bill Joy
      + vim by Bram Moolenaar
      + nano by Chris Allegretta
      + emacs by Richard Matthew Stallman

* 실행:
   ```bash
   vi ./vi_test.txt
   vim ~/vim_test.md
   nano /nano_test.log
   emacs /tmp/emacs_test
   ```

***