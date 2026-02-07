# RHCSA을 향하여
* [참고 문서: RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 03 - User grep and regular expressions to analyze text

* 활용 도구: Microsoft Copilot
    - 단어 선택
    - 기입 제안
    - 문서 검토

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - grep과 정규 표현식
#### 학습 목표
1. grep 명령어 학습
2. 정규 표현식 학습

#### 특징
* grep 명령어는 정규표현식 기반의 파일 내부 탐색기이다.

#### 주요 명령
* grep
    - 파일 전역에서 정규 표현식을 사용해 일치하는 줄을 출력한다.
* echo
    - 사용자의 문자열 입력을 메아리처럼 그대로 내보낸다.
* ps
    - 동작 중인 프로세스의 상태를 목록화하여 출력한다.

***

## ㄴ. 본문
### grep
* grep [옵션] [단어] [파일]
    - Global Regular Expression Print
    - 옵션: 생략 가능, 일반 단어만 보고 싶을때 생략 가능하다.
    - 단어: 필수, grep 사용의 목적이며 문자 또는 열을 입력해야 한다.
    - 파일: 생략 가능, 특정 파일을 전달 받으면 생략 가능하다.
* 실행
    - 파일과 옵션을 생략
        ```bash
        grep --help | grep case
            -i, --ignore-case         대소문자 구분을 무시합니다
                --no-ignore-case      대소문자 구분을 유지합니다(기본값)
        ```
    - 일치하는 문자열 줄을 제외하고 출력
        ```bash
        grep -v 'nologin' /etc/passwd 
        root:x:0:0:root:/root:/bin/bash
        sync:x:5:0:sync:/sbin:/bin/sync
        ```
    - 일치하는 문자열의 갯수 출력
        ```bash
        grep -c 'root' /etc/passwd
            2
        ```
    - 일치하는 문자열의 줄 앞에 행 번호 출력
        ```bash
        grep -n 'sshd' /etc/ssh/sshd_config	
        1:#	$OpenBSD: sshd_config,v 1.104 2021/07/02 05:11:21 dtucker Exp $
        3:# This is the sshd server system-wide configuration file.  See
        ```

---

### 정규 표현식(Regular Expression)
* 정규 표현식
    - 문자 또는 문자열의 패턴을 정의하고 이를 검색·출력·변환 등을 수행하기 위한 특수한 표현 방식이다.
    - [GNU BRE&GRE](https://www.gnu.org/software/grep/manual/html_node/Basic-vs-Extended.html)
* 정규 표현식
    - Regex(Regular Expressions)
        + . \, \! \$ \^ \* \+ \- \= \: \? \( \) \{ \} \[ \] \\ \| \\A \\Z \\G ... 
* BRE(Basic Regular Expressions)
    - BRE(Basic Regular Expressions)
    - 기본 정규식: 특수 문자를 사용하려면 이스케이프\(\\\)와 함께 사용하여야 한다.
        ```bash
        grep 'ro\+t' /etc/passwd
        root:x:0:0:root:/root:/bin/bash
        operator:x:11:0:operator:/root:/sbin/nologin
        ```
* ERE(Extended Regular Expressions)
    - ERE(Extended Regular Expressions)
    - 확장 정규식: 특수 문자가 기본으로 활성화되어 있다.
        ```bash
        grep -E 'ro+t' /etc/passwd
            root:x:0:0:root:/root:/bin/bash
            operator:x:11:0:operator:/root:/sbin/nologin
        ```
* \.
    - .   --> 한 문자
    - ..  --> 두 문자
    - ... --> 세 문자
    ```bash
    echo -e "hello\nworld" > regex_test.txt 

    grep '.ello' regex_test.txt 

    hello
    ```
* \*
    - 한 문자가 0개 이상 일치
    ```bash
    grep -E ".*d" regex_test.txt 

    world
    Regex: <>\d\D\w\W\s\S
    ```
* \^
    - 한 줄의 시작 지점에서 부터 일치
    ```bash
    grep '^root' /etc/passwd

    root:x:0:0:root:/root:/bin/bash
    ```
* \$
    - 한 줄의 끝 지정
    ```bash
    grep '/bin/bash$' /etc/passwd

    root:x:0:0:root:/root:/bin/bash
    rocky:x:1000:1000:rocky:/home/rocky:/bin/bash
    ExamUser:x:1004:1004::/ExamUser:/bin/bash
    examuser:x:10001:10001::/home/examuser:/bin/bash
    ```
* \[ \]
    - 대괄호 안의 어느 문자이던 일치
    ```bash
    grep '[r]' /etc/passwd

    root:x:0:0:root:/root:/bin/bash
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    ...
    ```
* \\
    - grep, BRE에서 특수 문자를 사용하기 위해 필요한 이스케이프 문자
    - grep -E, ERE에서 이스케이프 문자 또는 일반 문자화
    - grep 은 한 줄씩 읽는다. 때문에 '\\n'을 읽을 수 없다.
    ```bash
    grep '\n' regex_test.txt
    grep '\*' regex_test.txt 

    Regex: .,!$^*+-=:?(){}[]\|
    ```
    ```bash
    grep '\\A' regex_test.txt 

    \A\Z\G
    ```

---

### 다른 명령어와 조합
* ps + grep
    - Process Status
    - 동작 중인 프로세스의 상태를 목록화하여 출력한다.
    ```bash
    ps aux | grep 'sshd'
        root        1095  0.0  0.3  19748 10916 ?        Ss   17:25   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        root        3469  0.0  0.0 221820  2676 pts/1    S+   18:09   0:00 grep --color=auto sshd
    ```

* grep + head
    ```bash
    grep -r 'error' /var/log | head
        /var/log/tuned/tuned.log:2025-09-28 14:10:17,915 ERROR    tuned.utils.commands: Executing 'modprobe -r cpufreq_conservative' error: modprobe: FATAL: Module cpufreq_conservative is builtin.
    ```

### egrep
* grep -E 와 같은 ERE(Extended Regular Expressions)
    - 입력 예시: grep \-E '문자열' 파일
    - \| 이 특수 문자는 정규 표현식이며, 파이프가 아니다.
        + '또는(OR)'의 뜻
        + sshd|ftp --> sshd 또는 ftp
    - 각 CLI, 프로그램, 언어 마다 정규 표현식 기능이 다름
    ```bash
    egrep 'sshd|ftp' /etc/services
        ftp-data        20/tcp
        ...

    grep -E 'sshd|ftp' /etc/services | head
        ftp-data        20/tcp
    ```

***