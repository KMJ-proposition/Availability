확인:
1. 템플릿 구조에 맞는가
2. 추가 또는 삭제한 구조가 깔끔한가
3. 내용에 오해의 소지나 오류가 없는가
4. 오타가 없는가

# RHCSA을 향하여
* [참고 문서: RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 08 - Create, delete, copy and move files and directories

* 활용 도구: Microsoft Copilot
    - 단어 선택
    - 기입 제안
    - 문서 검토

* 참고 문헌: []

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - 파일 조작
#### 학습 목표
1. 파일을 생성·삭제·복사·이동·이름 변경을 할 수 있다.
4. 파일의 메타데이터에 대해 이해한다.
2. 파일의 타임스탬프를 조작할 수 있다.
3. 파일의 권한을 제어할 수 있다.

#### 특징
* 
* 리눅스의 Timestamp(타임스탬프)엔 3종류가 있으며, 이는 최근(Latest)을 기준으로 한다.

    | 타임스탬프 명칭 | 전체 이름 | 설명 |
    |-|-|-|
    | atime | Access Time | 파일에 대한 접근 시간 |
    | mtime | Modify Time | 파일의 내용 수정 시간 |
    | ctime | Change Time | 파일의 상태 변경 시간 |

#### 주요 명령
| 명령어 | 전체 이름 | 설명 | 비고 |
|-|-|-|-|
| 검색 | | compgen -c \| grep 명령어 | 명령어 존재 여부 확인 |
| ls | List | 파일의 기본 정보를 목록 테이블로 출력 | List Directory Contents |
| touch | Touch | 빈 파일 생성 또는 타임스탬프 변경 | atime, mtime 변경 |
| stat | Status | 파일 또는 파일 시스템의 상태 출력 | 메타데이터 확인 |
| rm | Remove | 파일 또는 디렉터리 삭제 |  |
| rmdir | Remove Directory | 빈 디렉터리만 삭제 | |
| mv | Move (Rename) | 파일 이동 또는 이름 변경 |
| cp | Copy | 파일 복사 | 특수 파일 등 복사 불가 |
| chmod | Change File Mode Bits | |
| chown | Change File Owner and Group | |
| umask | 
| attr | Attribute | 메타데이터의 확장 속성 제어 | XFS 파일 시스템의 객체만 가능 |

***

## ㄴ. 본문
### 파일 생성
* touch
    - 파일의 메타데이터 내 시간 기록을 조작한다.
    - atime(-a), mtime(-m)을 갱신한다.
        + atime: 접근 시간, 읽기가 발생할 때 갱신
            * *단, mtime 또는 ctime보다 오래된 경우에만 갱신된다.*
            * *ext4, XFS는 읽기 횟수를 기록하지 않기에, 도구를 통해 읽기 발생을 전달받는다.*
        + mtime: 수정 시간, 내용이 변경될 때 갱신
    - touch [옵션] [파일]
- 빈 파일을 생성한다.
    ```bash
    touch A.txt

    ll
    합계 0
    -rw-r--r--. 1 root root 0  2월  7 13:50 A.txt

    stat A.txt 
    ...
    Access: 2026-02-07 13:50:17.303738325 +0900
    Modify: 2026-02-07 13:50:17.303738325 +0900
    ...
    ```
- 타임스탬프를 변경한다.
    ```bash
    touch A.txt 
    
    stat A.txt 
    ...
    Access: 2026-02-07 13:58:07.797093656 +0900
    Modify: 2026-02-07 13:58:07.797093656 +0900
    ...
    ```

---

### 파일 삭제
* rm
    - 파일을 삭제한다.
    - rm [옵션] [파일]
        ```bash
        ls
        A.txt

        rm A.txt
        rm: remove 일반 빈 파일 'A.txt'? y
        ls
        ```
* rmdir
    - 빈 디렉터리를 삭제한다.
    - rmdir [옵션] [파일]
        ```bash
        mkdir RMDIR
        ls
        RMDIR

        rmdir RMDIR/
        ls
        ```

---

### 파일 이동
* mv
    - 파일을 이동하거나 이름을 변경한다.
    - 
* 파일 이동
    ```bash
    pwd
    /root/PWD

    mv A /root/
    ls

    cd /root/
    ls
    A 
    ```    
* 이름 변경
    ```bash
    touch A
    ls
    A

    mv A B
    ls
    B
    ```

---

### 파일 복사
* cp
    - 파일을 복사한다.
    - 
* 파일 복사
    ```bash
    ls /root/PWD/

    cp A /root/PWD/
    ls /root/PWD/
    A
    ```

---

### 속성 제어
* attr
    - 

* lsattr, chattr
    ```bash
    lsattr A
    ---------------------- A
    chattr +i A

    lsattr A
    ----i----------------- A

    chattr -i +a A
    lsattr A
    -----a---------------- A
    ```


***