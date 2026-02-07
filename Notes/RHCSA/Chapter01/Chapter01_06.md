# RHCSA을 향하여
* [참고 문서: RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 06 - Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2

* 활용 도구: Microsoft Copilot
    - 단어 선택
    - 기입 제안
    - 문서 검토

***

## ㄱ. 개요
### 기본 도구의 사용과 이해 - 아카이브와 압축
#### 학습 목표
1. 아카이브와 압축 학습

#### 특징
* tar
    - 옵션을 통해 메타데이터를 완벽 보존 가능하다.
* gzip, bzip2
    - 하나의 파일만 완벽하게 압축한다.
    - 메타 데이터를 거의 저장하지 못한다.
    - 여러 파일의 압축은 tar와 함께 사용해야 한다.
* zip
    - 여러 파일의 압축이 가능해서 편리하다.
    - 메타 데이터가 저장되지 않는 경우가 많다.

#### 주요 명령
* tar
    - 파일과 그 구조를 한 데 묶어 저장하는 도구
* zip, gzip, bzip2
    - 파일 용량을 줄여 압축하는 도구

***

<!--
| 옵션 | 약어 | 설명 |
|-------|-----|------|
| -c |  Create  | 아카이브 생성 |
| -C | Change to Directory | 파일을 이 디렉터리에 추출 |
| -f | File | 아카이브의 이름을 지정
| -t | List | 아카이브의 내용 확인
| -v | Verbose | 생성 과정을 출력
| -x | Extract | 아카이브 내용을 추출

| 압축 옵션 | 설명 |
|---|---|
| -z | gz 파일로 아카이브 생성/추출 |
| -j | bz2 파일로 아카이브 생성/추출 |
| -J | xz 파일로 아카이브 생성/추출 |
-->

## ㄴ. 본문
### tar
* tape archive
* 백업을 위해 태어났다.
* 단순 포장은 용량을 줄이지 않는다.
* 파일을 디렉터리 구조까지 포장 가능하다.
* 확장 속성을 포함해 메타데이터를 완벽 보존 가능하다.
* tar, gzip, bzip2, xz 파일로 1차 압축하여 포장할 수 있다.
* 기본 옵션
    - -c: Create, 아카이브 생성
    - -C: Change to Directory, 파일을 이 디렉터리에 추출
    - -f: File, 아카이브의 이름을 지정
    - -t: List, 아카이브의 내용 확인
    - -v: Verbose, 생성 과정을 출력
    - -x: Extract, 아카이브 내용을 추출
* 압축 옵션
    - -z: gz 파일로 아카이브 생성/추출
    - -j: bz2 파일로 아카이브 생성/추출
    - -J: xz 파일로 아카이브 생성/추출
* tar [옵션] [아카이브 이름] [목적 파일]
* 실행:
    - 아카이브 생성/추출/내용 확인
        ```bash
        tar -cf Files.tar /home/examuser/
        tar: 구성 요소 이름 앞에 붙은 `/' 제거 중
        ls
        Files.tar
        
        tar -xf Files.tar -C /tmp
        ls /tmp
        home

        tar -tvf zipper.sh.tar.xz
        -rwx------ root/root       269 2000-07-25 19:11 zipper.sh
        ```
    - gzip 파일로 아카이브 생성/추출
        ```bash
        tar -czf zipper.sh.gz zipper.sh
        tar -xzf zipper.sh.gz
        ```
    - bzip2 파일로 아카이브 생성/추출
        ```bash
        tar -cjf zipper.sh.bz2 zipper.sh
        tar -xjf zipper.sh.bz2
        ```
    - xz 파일로 아카이브 생성/추출
        ```bash
        tar -cJf zipper.sh.xz zipper.sh
        tar -xJf zipper.sh.xz
        ```

---

### zip, gzip, bzip2
* zip, gzip, bzip2
    - 압축으로 크기를 축소, 압축 해제로 복원하는 명령어이다.
    - 리눅스에서는 메타데이터를 거의 보존하지 않는다.
    - gzip, bzip2
        + 하나의 파일 압축에 특화되어 있다.
        + 사본 없이 원본 파일 자체를 압축한다.
        + 압축 파일은 '원본 이름+압축명'이다.

---

* zip
    - 윈도우 표준이며, 리눅스에서는 메타데이터가 잘 저장되지 않는다.
    - 옵션 '-r': Recursively, 파일의 내부를 탐색해서 모두
        + 내부는 파일만을 가리킴, 내용이 아니다.
* zip [옵션] [압축파일 이름] [목적 파일]
    ```bash
    zip -r ZIP.zip /home/examuser/
      adding: home/examuser/ (stored 0%)
      adding: home/examuser/.mozilla/ (stored 0%)
      adding: home/examuser/.mozilla/extensions/ (stored 0%)
      adding: home/examuser/.mozilla/plugins/ (stored 0%)
      ...
    ```
* gzip
    - 기본 옵션
        + -d: decompress, 압축 해제
        + -l: 압축 파일의 정보 출력: 압축 크기/압축되지 않은 크기/압축률/압축된 파일
    - gunzip
        + gzip 압축 해제 명령어
* gzip [옵션] [목적 파일]
    ```bash
    gzip zipper.sh

    gzip -d zipper.sh.gz
    gunzip zipper.sh.gz

    gzip -l zipper.sh.gz
         compressed        uncompressed  ratio uncompressed_name
                252                 269  16.7% zipper.sh
    ```

* bzip2
    - 기본 옵션
        + -z: compress, 압축
        + -d: decompress, 압축 해제
    - bunzip2
        + bzip2 압축 해제 명령어
* bzip2 [옵션] [목적 파일]
    ```bash
    bzip2 -z zipper.sh 
    ls
    zipper.sh.bz2

    bzip2 -d zipper.sh.bz2
    bunzip2 zipper.sh.bz2
    ```

***