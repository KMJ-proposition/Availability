# RHCSA을 향하여
* [참고 문서: RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 07 - Create and edit text files

* 활용 도구: Microsoft Copilot
    - 단어 선택
    - 기입 제안
    - 문서 검토

***

## ㄱ. 개요
- 유닉스 철학
    > M. D. McIlroy, Bell System Technical Journal, 1978
        >> 1. *Write programs that do one thing and do it well.*
        >> 2. *Write programs to work together.*
        >> 3. *Write programs to handle text streams, because that is a universal interface.*

    > 핵심 요약 및 해설
        >> - 단일 책임 원칙: 하나의 도구는 한 가지 기능만 완벽하게 수행해야 한다. (예: tar는 아카이브만, gzip은 압축만)
        >> - 상호 협력: 도구들은 독립적으로 존재하되, 서로 연결되어 더 복잡한 문제를 해결할 수 있어야 한다.
        >> - 보편적 인터페이스: 모든 데이터는 '텍스트 스트림' 형태로 전달되어야 한다. 그래야 어떤 도구라도 데이터를 주고받을 수 있기 때문이다.

    > 참고 문헌 및 출처
        >> - Original Paper: [The Bell System Technical Journal (Vol. 57, July-August 1978)](https://archive.org/details/bstj57-6-1899)
        >> - Further Reading: 《The Art of Unix Programming》 by Eric S. Raymond (2003)
        >> - AI Summary: 본 해설은 Google Gemini의 기술적 자문을 바탕으로 작성되었습니다.

### 기본 도구의 사용과 이해 - 편집기
#### 학습 목표
1. vim 편집기를 사용하여 파일 내용을 수정한다.

#### 특징
* 편집기는 화면 전환 및 수정 가능하도록 설계 되었다.

#### 주요 명령
* vim
    - 파일의 원시 데이터를 편집하는 프로그램

***

## ㄴ. 본문
### vim
#### 소개
* vim - Vi IMproved, a programmer's text editor. [Vim the editor](https://www.vim.org/)
* 최초 개발자: 브람 무레나르(Bram Moolenaar)
* 파일의 원시 데이터를 편집하는 프로램으로, 유닉스 편집기인 vi를 발전시킨 것이다.
* 파일 형식으로 메모리에 저장하는 것이 아닌, 버퍼를 이용한다.
* MIT 라이센스를 따르며, 현재는 버전 8대에 이른다.
    > Vim is charityware. Its license is GPL-compatible, so it's distributed freely, but we ask that if you find it useful you make a donation to help children in Uganda through the [Kuwasha](https://www.kuwasha.net/) charity. The full license text can be found in the documentation. Much more information about charityware on [Charityware.info.](http://charityware.info/)
* 기본 제공 패키지가 아니므로 외부에서 받아야 한다.

---

#### 사용
* 4가지 모드가 있다.
    1. Normal: 줄·화면 단위 수정
        + ESC
    2. Insert: 텍스트 삽입·수정
        + i
        + insert 버튼
    3. Visual: 텍스트 블록을 지정
        + Ctrl + V(Line)
        + Ctrl + v(Block)
    4. Command-Line: 내부 명령 실행
        + :
* 용어(일부)
    - !: force
    - a: append
    - b: back
    - c: change
    - d: delete
    - e: end
    - f: find
    - g: go
    - h: help
    - i: insert
    - j: jump
    - l: right
    - m: mark
    - o: open line
    - p: put
    - q: quit
    - r: replace
    - u: undo
    - w: write, word
    - y: yank

---

#### 실행
* 설치
    ```bash
    dnf install vim -y
    ```
* 실행
    ```bash
    vim ~/example.txt
    ```
* 설정
    ```bash
    vim ~/.vimrc
    ```
* 파일 생성, 내용 수정, 결과 확인
    ```bash
    bash$ cat > example.txt
    Hello, World!
    bash$ echo '[Notice] Take Test Text Tool' > TextFile
    ```
    ```bash
    bash$ vim example.txt
    bash$ vim TextFile
    ```
    ```bash
    bash$ head example.txt && echo '---------' && tail TextFile 
    Hello, World!
    추가 내용
    ---------
    [Notice] Take Test Text Tool
    [추가] 추가 내용
    ```

***