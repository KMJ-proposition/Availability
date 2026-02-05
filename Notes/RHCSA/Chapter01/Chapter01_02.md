# RHCSA을 향하여
* [RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
	- Chapter 01) Understand and user essential tools
	- 02 - Use input-output redirection

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - 리다이렉션과 파이프라인
#### 학습 목표
1. 리다이렉션 학습
2. 파이프라인 학습
3. 표준 출력과 표준 오류의 학습

#### 특징
* 리다이렉션과 파이프라인은 다중 입력이 가능하다.

#### 주요 명령
* \>, \>\>, \<
	- 리다이렉션: 스트림을 파일과 연결	
* \|
	- 파이프라인: 프로세스 간 스트림을 연결
* \&\>
	- 표준 출력과 표준 오류를 동시에 파일화
* wc, head, tail, date
	- 단어 수
	- 머릿줄
	- 꼬릿줄
	- 날짜와 시간

***

## ㄴ. 본문
### 출력 리다이렉션
* \>, \>\>
	- 명령어의 내용을 파일 내용으로 '출력'한다. 쓰기 전용

* \>
	- 파일의 내용을 덮어쓴다.
	- 파일이 없으면 생성한다.

* 실행:
	```bash
	ls /etc > ~/output.txt
	```
	
* \>\>
	- 파일 내용을 추가한다.
	- 바이트 단위의 표준 출력 스트림을 파일로 방향을 전환한다.

* 실행:
	```bash
	date >> ~/output.txt
	```
	
* wc
	- word count \-\-\> 단어 갯수
	- 파일 내용의 줄·단어·문자·파일 순서로 출력

	```bash
	wc output.txt
	272  272 2589 output.txt
	```
	
* 실행:
	```bash
	wc output.txt
	273  278 2622 output.txt
	```
	
* date
	- date \-\-\> 날짜
	- 현재 일자와 시간 확인

* 실행:
	```bash
	date
	202x. 0x. 0x. (일) 1x:1x:xx KST
	```
	
* tail
	- tail \-\-\> 꼬리
	- 파일의 맨 아랫줄(꼬리) 내용을 출력

* 실행:
	```bash
	tail -n 1 output.txt
	202x. 0x. 0x. (일) 1x:1x:xx KST
	```

***

### 입력 리다이렉션
* <
	- 우측의 파일 내용을 명령어로 '입력'함. 읽기 전용
	- 파일의 바이트 단위 스트림을 명령어의 표준 입력으로 전환한다.
		+ 입력을 사용자 입력에서 파일의 내용으로

* 실행:
	```bash
	tail < output.txt
	wpa_supplicant
	xattr.conf
	xdg
	xinetd.conf
	xinetd.d
	xml
	yum
	yum.conf
	yum.repos.d
	202x. 0x. 0x. (일) 1x:1x:xx KST
	```

### 파이프라인(파이프)
* |
	- 명령어의 표준 출력 스트림을 파이프 다음 명령어의 표준 입력으로 전달한다.
	- 리다이렉션처럼 스트림의 방향을 전환시키는 것과 일맥상통한다.
	- 리다이렉션은 스트림을 파일과 연결, 파이프는 프로세스 간 스트림을 연결한다.
	- 단, 파이프는 프로세스끼리만 실행 전에 연결해 주고받을 수 있다.

* 실행:
	```bash
	ls /var/log | head
	README
	anaconda
	audit
	boot.log
	...

	ls /etc | wc -l > ~/count.txt

	cat count.txt
		272
	```

* 프로세스는 독립적이다.
	- FD는 프로세스 실행 전 스트림 방향을 결정하고 실행되는 것이 원칙이다.
	- 실행 중인 프로세스의 스트림 방향을 바꿀 수 없는 것이 원칙이다.
	- 보통은 root 권한이더라도 실행중인 프로세스는 직접 조작할 수 없다.
		+ 이것은 특수한 기술을 통한 커널 수준의 무언가가 필요하다.
		+ FD 테이블은 커널이 관리하는 프로세스 내부 구조이다.
		+ root 계정은 '사용자 공간'의 최고 권위자이다.
			* root는 파일 접근 권한을 우회할 수 있도록 커널이 허용한 계정이다.
	- FD, 루트킷에 대한 이해 공부 필요

***

### 오류 메시지
* 리다이렉션 전의 숫자 2는 FD 2번, 표준 오류를 나타낸다.
	- 2>, 2>>
	- 보통 오류라고 부른다.
	- 리다이렉션으로 오류 메시지를 파일로 전달한 것이다.

* 오류 메시지를 리다이렉션으로 출력해보자.
	- 2>
		```bash
		ls /RHCSA_EXAM/PASS_EXAM.txt 2> ~/errors.txt
		ls: cannot access '/RHCSA_EXAM/PASS_EXAM.txt': 그런 파일이나 디렉터리가 없습니다
		```
	- 2>>
		```bash
		ls /RHCSA_EXAM/EXAM_FEE.txt 2>> ~/errors.txt
		ls: cannot access '/RHCSA_EXAM/PASS_EXAM.txt': 그런 파일이나 디렉터리가 없습니다
		ls: cannot access '/RHCSA_EXAM/EXAM_FEE.txt': 그런 파일이나 디렉터리가 없습니다
		```

***

### 표준 출력과 오류의 조합
* 리다이렉션의 순서에 따라 결과가 달라질 수 있으니 주의
* &>
	- '&'와 다르다. 
		+ '&' 단독으로 실행시 프로세스를 백그라운드에서 실행한다.
	- '&>' == '출력+오류 스트림 (FD1+FD2)'
		+ 이것은 '> file 2>&1'와 같다.
		+ 명령어는 줄 단위로 실행한다. (설명은 아래 박스에)

* 실행:
	```bash
	ls /var/log /invalid/directory &> ~/combined.txt
	ls /var/log /invalid/directory > ~/combined.txt 2>&1
	```

* 실행:
	```bash
	cat combined.txt
	ls: cannot access '/invalid/directory': 그런 파일이나 디렉터리가 없습니다
	/var/log:
	README
	...
	```

* 표준 출력(\>) + 표준 오류(2\>)
	- 실행 1:
		```bash
		ls /etc /invalid/directory > ~/out.txt 2> ~/err.txt
		```
		+ 각 파일의 행 갯수 확인
			```bash
			wc out.txt err.txt
				273  273 2595 out.txt
				1    8   89 err.txt
			```
		+ 내용 확인
			```bash
			tail -n 1 out.txt err.txt
				==> out.txt <==
				yum.repos.d
				
				==> err.txt <==
				ls: cannot access '/invalid/directory': 그런 파일이나 디렉터리가 없습니다
			```
	- 실행 2:
		```bash
		ls /var/log /invalid/directory >> ~/out.txt 2>> ~/err.txt
		```
		+ wc로 확인
			```bash
			wc out.txt err.txt
				353  353 3746 out.txt
				2   16  178 err.txt
			```
		+ 파일의 내용 출력
			```bash
			tail -n 1 out.txt err.txt
				==> out.txt <==
				wtmp
				
				==> err.txt <==
				ls: cannot access '/invalid/directory': 그런 파일이나 디렉터리가 없습니다
			```

***

### 특수 장치
* /dev/null
	- 커널 기능의 가상 장치 파일이다.
	- 마치 블랙홀처럼 내용을 흡수하지만 출력은 하지 않는다.
	- 실제 하드웨어와 연결되지 않았기에 기록 과정이 없다.
	- character 파일 유형이며 바이트 스트림으로 동작한다.
	- 같은 유형: /dev/null, /dev/zero, /dev/random, /dev/urandom

* 실행:
	```bash
	ls /nothing 2> /dev/null
	(ls /nothing 2>&1) > /dev/null
	```

***

## ㄷ. 기록
* History
	```
	1000  ls /etc > ~/output.txt
	1001  cd ~
	1002  ls
	1003  wc output.txt
	1004  date >> ~/output.txt
	1005  wc output.txt
	1006  tail -n 1 output.txt
	1007  tail < output.txt
	1008  ls /var/log | head -n 10
	1009  ls /etc | wc -l > ~/count.txt
	1010  cat count.txt
	1011  ls /etc > &0 | cat
	1012  ls /etc > &0 cat
	1013  ls /RHCSA_EXAM/PASS_EXAM.txt 2> ~/errors.txt
	1014  cat ~/errors.txt 
	1015  ls /RHCSA_EXAM/EXAM_FEE.txt 2>> ~/errors.txt
	1016  cat ~/errors.txt 
	1017  ls /var/log /invalid/directory &> ~/combined.txt
	1018  cat combined.txt 
	1019  ls /nothing 2> /dev/null
	1020  ls /nothing 2>&1 > /dev/null
	1021  (ls /nothing 2>&1) > /dev/null
	1022  udevadm /dev/null
	1023  udevadm --help
	1024  man udevadm
	1025  udevadm info /dev/null
	1026  udevadm monitor /dev/null
	1027  (ls /nothing 2>&1) > /dev/null 1>&1
	1028  cat /dev/rendom
	1029  cat /dev/random 
	1030  wc /dev/random 
	1031  random
	1032  ls /dev/random 
	1033  ls -l /dev/random 
	1034  ls -l /dev/null 
	1035  ls -l /dev/zero 
	1036  ls -l /dev/sda 
	1037  ls -l /dev/urandom 
	1038  ls /etc /invalid/directory > ~/out.txt 2> ~/err.txt
	1039  ls
	1040  cat out.txt err.txt
	1041  wc out.txt err.txt
	1042  tail -n 1 out.txt err.txt
	1043  ls /var/log /invalid/directory >> ~/out.txt 2>> ~/err.txt
	1044  tail -n 1 out.txt err.txt
	1045  wc out.txt err.txt
	1046  history
	```
***