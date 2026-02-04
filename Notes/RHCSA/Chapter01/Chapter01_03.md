# RHCSA (EX200) Exam Preparation Guide
* https://rhcsa.github.io/

## ㄱ. 개요
### Chapter 01 - 01. Understand and user essential tools
#### 03 - User grep and regular expressions to analyze text
* grep 명령어 학습

#### 목표
* grep 명령어 입력을 숙달하고 원리를 이해한다.

#### 주요 명령
    - GREP(BRE, ERE)
        - https://www.gnu.org/software/grep/manual/html_node/Basic-vs-Extended.html
        - BRE(Basic Regular Expressions)
            - 기본 정규식: 특수 문자를 사용하려면 이스케이프\(\\\)와 함께 사용하여야 한다.
        - ERE(Extended Regular Expressions)
            - 확장 정규식: 특수 문자가 기본으로 활성화되어 있다.
    - Regex(Regular Expressions)
        - . \, \! \$ \^ \* \+ \- \= \: \? \( \) \{ \} \[ \] \\ \| \\A \\Z \\G ...
    - grep
        - Global Regular Expression Print
        - 파일 전역에서 정규 표현식을 사용해 일치하는 줄을 출력한다.
    - echo
        - 메아리
        - 사용자의 문자열 입력을 메아리처럼 그대로 내보낸다.
    - ps
        - Process Status
        - 동작 중인 프로세스의 상태를 목록화하여 출력한다.

## ㄴ. 특징
* grep 명령어는 정규 표현식 기반 파일 내용 탐색기이다.

## ㄷ. 본문

### 1. Basic grep Usage
#### grep 명령어를 써보자.
* grep
    ```
    root# grep --help | grep case
        -i, --ignore-case         대소문자 구분을 무시합니다
            --no-ignore-case      대소문자 구분을 유지합니다(기본값)
    ```

### 2. Using Regular Expressions with grep
#### 정규 표현식을 써보자.
* .
    - .   --> 한 문자
    - ..  --> 두 문자
    - ... --> 세 문자
    ```
    root# echo -e "hello\nworld" > regex_test.txt 

    root# grep '.ello' regex_test.txt 
        hello
    ```

* \*
    - 한 문자가 0개 이상 일치
    ```
    root# grep -E ".*d" regex_test.txt 
        world
        Regex: <>\d\D\w\W\s\S
    ```

* \^
    - 한 줄의 시작 지점에서 부터 일치
    ```
    root# grep '^root' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
    ```

* \$
    - 한 줄의 끝 지정
    ```
    root# grep '/bin/bash$' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        rocky:x:1000:1000:rocky:/home/rocky:/bin/bash
        ExamUser:x:1004:1004::/ExamUser:/bin/bash
        examuser:x:10001:10001::/home/examuser:/bin/bash
    ```

* \[ \]
    - 대괄호 안의 어느 문자이던 일치
    ```
    root# grep '[r]' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        adm:x:3:4:adm:/var/adm:/sbin/nologin
        ...
    ```

* \\
    - grep, BRE에서 특수 문자를 사용하기 위해 필요한 이스케이프 문자
    - grep -E, ERE에서 이스케이프 문자 또는 일반 문자화
    ```
    root# grep '\n' regex_test.txt
    root# grep '\*' regex_test.txt 
        Regex: .,!$^*+-=:?(){}[]\|
    root# grep '\\A' regex_test.txt 
        \A\Z\G

    # grep 은 한 줄씩 읽는다. 때문에 \\n을 읽을 수 없으므로 아무 결과 없음
    ```

### 3. Using Wildcards and Quantifiers
#### 와일드 카드\(.\)의 수를 변경해보며 사용해보자.
* 와일드 카드\(.\) 3개
    ```
    root# grep 'root...' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        operator:x:11:0:operator:/root:/sbin/nologin
    ```

* BRE(Basic Regular Expressions) 방식
    - \\\+
    - BRE는 이스케이프\(\\\)를 추가해 사용한다.
    ```
    root# grep 'ro\+t' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        operator:x:11:0:operator:/root:/sbin/nologin
    ```

* ERE(Extended Regular Expressions) 방식
    - \+
    - ERE는 특수 문자가 기본적으로 활성화되어 있다.
    ```
    root# grep -E 'ro+t' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        operator:x:11:0:operator:/root:/sbin/nologin
    ```

### 4. Combining grep with Other Commands
#### 다른 명령어와 조합해 사용해보자.
* ps \+ grep
    - Process Status
    - 동작 중인 프로세스의 상태를 목록화하여 출력한다.
    ```
    root# ps aux | grep 'sshd'
        root        1095  0.0  0.3  19748 10916 ?        Ss   17:25   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        root        3469  0.0  0.0 221820  2676 pts/1    S+   18:09   0:00 grep --color=auto sshd
    ```
* grep \+ head
    ```
    root# grep -r 'error' /var/log | head		# -r --> recursively
        /var/log/tuned/tuned.log:2025-09-28 14:10:17,915 ERROR    tuned.utils.commands: Executing 'modprobe -r cpufreq_conservative' error: modprobe: FATAL: Module cpufreq_conservative is builtin.
    ```

### 5. Inverse Matching with grep
#### 일치하는 문자열 줄을 제외하고 출력
* \-v 옵션
    - 입력 예시: grep \-v '문자열' 파일
    ```
    root# grep -v 'nologin' /etc/passwd 
        root:x:0:0:root:/root:/bin/bash
        sync:x:5:0:sync:/sbin:/bin/sync
    ```

### 6. Counting Matches with grep
#### 일치하는 문자열의 갯수 출력
* \-c 옵션
    - 입력 예시: grep \-c '문자열' 파일
    ```
    root# grep -c 'root' /etc/passwd
        2
    ```

### 7. Display Line Numbers with Matches
#### 일치하는 문자열의 줄 앞에 행 번호 출력
* 맨 앞에 행 번호 표시
    - 입력 예시: grep \-n '문자열' 파일 
    ```
    root# grep -n 'sshd' /etc/ssh/sshd_config	
        1:#	$OpenBSD: sshd_config,v 1.104 2021/07/02 05:11:21 dtucker Exp $
        3:# This is the sshd server system-wide configuration file.  See
    ```

### 8. Advanded Regular Expressions with egrep
#### egrep을 써보자.
* grep -E 와 같은 ERE(Extended Regular Expressions)
    - 입력 예시: grep \-E '문자열' 파일
    - \| 이 특수 문자는 정규 표현식이며, 파이프가 아니다.
        - '또는(OR)'의 뜻
        - sshd|ftp --> sshd 또는 ftp
    - 각 CLI, 프로그램, 언어 마다 정규 표현식 기능이 다름
    ```
    root# egrep 'sshd|ftp' /etc/services
        ftp-data        20/tcp
        ...

    root# grep -E 'sshd|ftp' /etc/services | head
        ftp-data        20/tcp
    ```

## ㄹ. 기록
* History
    ```
    1009  grep 'root' /etc/passwd
    1010  tail -n 5 /etc/passwd
    1011  grep --help | grep case
    1012  ls
    1013  pwd
    1014  echo -e "hello\nworld" > regex_test.txt 
    1015  grep .ello regex_test.txt 
    1016  echo -e 'TESTline\nRegex: .,!$^*+-=:?(){}[]\|\n' >> regex_test.txt 
    1017  cat regex_test.txt 
    1018  echo -e 'Regex: <>\d\D\w\W\s\S\t\n\A\Z\G' >> regex_test.txt 
    1019  cat regex_test.txt 
    1020  grep -E ".*d" regex_test.txt 
    1021  grep '^root' /etc/passwd
    1022  grep '/bin/bash$' /etc/passwd
    1023  grep '[r]' /etc/passwd
    1024  grep '\n' /etc/passwd
    1025  grep -E '\n' /etc/passwd
    1026  grep '\n' regex_test.txt 
    1027  grep -P '\n' regex_test.txt 
    1028  grep -P '\n' /etc/passwd
    1029  grep '\A' regex_test.txt 
    1030  grep '\\A' regex_test.txt 
    1031  grep '\*' regex_test.txt 
    1032  grep 'root...' /etc/passwd
    1033  grep grep 'root\+' /etc/passwd
    1034  grep 'ro\+t' /etc/passwd
    1035  grep -E 'ro+t' /etc/passwd
    1036  ps aux | grep 'sshd'
    1037  grep -r 'error' /var/log
    1038  grep -r 'error' /var/log | head
    1039  grep -v 'nologin' /etc/passwd
    1040  grep -c 'root' /etc/passwd
    1041  grep -n 'sshd' /etc/ssh/sshd_config
    1042  egrep 'sshd|ftp' /etc/services 
    1043  grep -E 'sshd|ftp' /etc/services | head
    1044  history
    ```