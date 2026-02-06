# RHCSA을 향하여
* [RHCSA (EX200) Exam Preparation Guide - hamid hosseinzadeh](https://rhcsa.github.io/)
    - Chapter 01) Understand and user essential tools
    - 06 - Archive, compress, unpack, and uncompress files using tar, gzip, and bzip2

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
      adding: home/examuser/.bash_logout (stored 0%)
      adding: home/examuser/.bash_profile (deflated 20%)
      adding: home/examuser/.bashrc (deflated 40%)
      adding: home/examuser/.vimrc (deflated 38%)
      adding: home/examuser/.bash_history (deflated 61%)
      adding: home/examuser/.cache/ (stored 0%)
      adding: home/examuser/myhosts (deflated 56%)
      adding: home/examuser/logfiles.txt (deflated 69%)
      adding: home/examuser/.ssh/ (stored 0%)
      adding: home/examuser/.ssh/authorized_keys (deflated 18%)
      adding: home/examuser/.viminfo (deflated 57%)
      adding: home/examuser/pubkey_test (deflated 18%)
      adding: home/examuser/.lesshst (stored 0%)
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

## ㄷ. 기록
    ```bash
     1002  2026-02-05 10:12:42 man tar
     1003  2026-02-05 10:12:59 man gzip
     1004  2026-02-05 10:13:15 man bzip2
     1005  2026-02-05 10:13:37 man zip
     1006  2026-02-05 10:13:50 man gzip
     1007  2026-02-05 10:13:56 history
     1008  2026-02-05 12:21:17 clear
     1009  2026-02-05 12:21:18 ll
     1010  2026-02-05 12:21:23 rm -f sudoers 
     1011  2026-02-05 12:21:26 rm -f pubkey_test 
     1012  2026-02-05 12:21:27 ls
     1013  2026-02-05 12:21:28 clear
     1014  2026-02-05 12:21:30 cd RHCSA/
     1015  2026-02-05 12:21:31 ls
     1016  2026-02-05 12:21:32 cd ..
     1017  2026-02-05 12:21:32 ls
     1018  2026-02-05 12:21:40 rm -rf RHCSA*
     1019  2026-02-05 12:21:41 ls
     1020  2026-02-05 12:21:43 clear
     1021  2026-02-05 12:21:49 ls -R projects/
     1022  2026-02-05 12:21:50 clear
     1023  2026-02-05 12:22:38 tar -cf Files.tar /home/examuser/
     1024  2026-02-05 12:22:45 ls
     1025  2026-02-05 12:23:52 man tar
     1026  2026-02-05 12:24:28 tar -c /home/examuser/
     1027  2026-02-05 12:24:33 ls
     1028  2026-02-05 12:24:37 rm -f Files.tar 
     1029  2026-02-05 12:24:38 tar -c /home/examuser/
     1030  2026-02-05 12:24:39 ls
     1031  2026-02-05 12:26:25 ll
     1032  2026-02-05 12:26:32 tar -cf Files.tar /home/examuser/
     1033  2026-02-05 12:26:35 ll
     1034  2026-02-05 12:26:59 #tar -xf Files.tar 
     1035  2026-02-05 12:27:00 man tar
     1036  2026-02-05 12:27:52 tar -xf Files.tar -C /tmp
     1037  2026-02-05 12:27:54 ls /tmp
     1038  2026-02-05 12:28:21 rm -rf /tmp/home/
     1039  2026-02-05 12:28:22 ll
     1040  2026-02-05 12:28:28 rm -f Files.tar 
     1041  2026-02-05 12:28:39 tar -cf Files.tar -C /home/examuser/
     1042  2026-02-05 12:28:42 ll
     1043  2026-02-05 12:28:46 man tar
     1044  2026-02-05 12:29:15 tar -C /home/examuser/ -cf Files.tar
     1045  2026-02-05 12:29:40 tar -cf Files.tar /home/examuser/ -C /home/tester/
     1046  2026-02-05 12:29:41 ll
     1047  2026-02-05 12:29:55 man tar 
     1048  2026-02-05 12:30:10 tar -tvf Files.tar 
     1049  2026-02-05 12:31:26 man zip
     1050  2026-02-05 12:36:11 zip -r ZIP.zip /home/examuser/
     1051  2026-02-05 12:38:58 man gzip
     1052  2026-02-05 12:44:22 gzip -r /home/examuser -S ThisIsGzip File.zip
     1053  2026-02-05 12:44:33 gzip -r -S ThisIsGzip /home/examuser/ File.zip
     1054  2026-02-05 12:44:39 gzip -r -S ThisIsGzip /home/examuser/
     1055  2026-02-05 12:44:39 ls
     1056  2026-02-05 12:44:43 rm -f ZIP.zip 
     1057  2026-02-05 12:44:47 rm -f Files.tar 
     1058  2026-02-05 12:44:47 ll
     1059  2026-02-05 12:44:51 gzip -r -S ThisIsGzip /home/examuser/
     1060  2026-02-05 12:44:51 ll
     1061  2026-02-05 12:44:56 ls /home/examuser/
     1062* 2026-02-05 12:45:11 
     1063  2026-02-05 12:45:47 gzip GZIP.gz -r /home/examuser/ -S ThisIsGzip
     1064  2026-02-05 12:45:48 ll
     1065  2026-02-05 12:45:52 ls /home/examuser/
     1066  2026-02-05 12:46:17 gzip -r /home/examuser/ 
     1067  2026-02-05 12:46:18 ll
     1068  2026-02-05 12:46:21 ls /home/examuser/
     1069  2026-02-05 12:46:37 ls -al /home/examuser/
     1070  2026-02-05 12:48:19 gunzip -r /home/examuser/
     1071  2026-02-05 12:48:21 ls -al /home/examuser/
     1072  2026-02-05 13:01:18 #for i in {(ls -R /home/examuser/)|wc -l}; if [[ $(grep -Rc ThisIsGzip) != 0 ]]; then mv "^(.*)ThisIsGzip$" ${BASH_REMATCH[1]}
     1073  2026-02-05 13:01:24 man realpath
     1074  2026-02-05 13:01:51 realpath /home/examuser/.bashrcThisIsGzip 
     1075  2026-02-05 13:12:29 #FAULT="ThisIsGzip";F_HOMELOC="/home/examuser";while True;grep -qR $F_HOMELOC &>/dev/null;if [[ $? -eq 0 ]]; then realpath (grep -R $FAULT $F_HOMELOC | head -n 1) |  grep mv "^(.*)$FAULT$" ${BASH_REMATCH[1]}
     1076  2026-02-05 13:12:30 man grep
     1077  2026-02-05 13:50:47 FAULT="ThisIsGzip";F_HOMELOC="/home/examuser";while true; do BASE=$(find "$F_HOMELOC" -type f -exec grep -q $FAULT {} \; -print -quit);[[ -z "$BASE" ]] && break;DIRN="$(dirname $BASE)";ONAME=$(basename "$BASE" | sed "s/$FAULT//"); mv "$BASE" $DIRN/$ONAME;done
     1078  2026-02-05 13:50:52 ls -al /home/examuser/
     1079  2026-02-05 13:51:07 find "$F_HOMELOC" -type f -exec grep -q $FAULT {} \; -print -quit
     1080  2026-02-05 13:51:11 find "$F_HOMELOC" -type f -exec grep -q $FAULT {} \;
     1081  2026-02-05 13:51:14 find "$F_HOMELOC" -type f -exec grep $FAULT {} \;
     1082  2026-02-05 13:51:42 find /home/examuser -type f -exec grep -q ThisIsGzip {} \;
     1083  2026-02-05 13:51:46 find /home/examuser -type f -exec grep -q ThisIsGzip {} \; -print
     1084  2026-02-05 13:51:51 find /home/examuser -type f -exec grep ThisIsGzip {} \;
     1085  2026-02-05 13:51:54 $?
     1086  2026-02-05 13:52:56 find /home/examuser -type f -exec grep -H ThisIsGzip {} \;
     1087  2026-02-05 13:53:06 grep -H ThisIsGzip /home/examuser
     1088  2026-02-05 13:53:10 grep ThisIsGzip /home/examuser
     1089  2026-02-05 13:53:17 grep -RH ThisIsGzip /home/examuser
     1090  2026-02-05 13:53:19 grep -qRH ThisIsGzip /home/examuser
     1091  2026-02-05 13:54:02 find /home/examuser -type f -name "*ThisIsGzip"
     1092  2026-02-05 13:55:13 find /home/examuser -type f -name "*ThisIsGzip" -print
     1093  2026-02-05 13:55:16 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1094  2026-02-05 13:55:19 find /home/examuser -type f -name "*ThisIsGzip" -quit
     1095* 2026-02-05 13:55:22 
     1096  2026-02-05 13:55:47 find /home/examuser -type f -name "*ThisIsGzip" -quit | dirname
     1097  2026-02-05 13:55:51 find /home/examuser -type f -name "*ThisIsGzip" -quit | xargs {} dirname
     1098  2026-02-05 13:55:55 find /home/examuser -type f -name "*ThisIsGzip" -quit | xargs dirname
     1099  2026-02-05 13:55:59 find /home/examuser -type f -name "*ThisIsGzip" -quit | basename
     1100  2026-02-05 13:56:05 find /home/examuser -type f -name "*ThisIsGzip" | basename
     1101  2026-02-05 13:56:43 #find /home/examuser -type f -name "*ThisIsGzip" -quit | basename
     1102  2026-02-05 13:56:44 history
     1103  2026-02-05 14:05:13 find /home/examuser -type f -name "*ThisIsGzip" -quit
     1104  2026-02-05 14:05:16 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1105  2026-02-05 14:13:54 A=$(find /home/examuser -type f -name "*ThisIsGzip" -print -quit);B=$(dirname $A);C=$(basename $A);A;B;C
     1106  2026-02-05 14:14:02 A=$(find /home/examuser -type f -name "*ThisIsGzip" -print -quit);B=$(dirname $A);C=$(basename $A);echo A;echo B;echo C
     1107  2026-02-05 14:14:07 A=$(find /home/examuser -type f -name "*ThisIsGzip" -print -quit);B=$(dirname $A);C=$(basename $A);echo $A;echo $B;echo $C
     1108  2026-02-05 14:15:15 D=$($C | sed "s/$ThisIsGzip//")
     1109  2026-02-05 14:15:41 echo $D
     1110  2026-02-05 14:15:43 $?
     1111  2026-02-05 14:15:46 echo $C
     1112  2026-02-05 14:15:56 D=$(echo $C | sed "s/$ThisIsGzip//")
     1113  2026-02-05 14:16:01 D=$(echo -e $C | sed "s/$ThisIsGzip//")
     1114  2026-02-05 14:16:14 print $C
     1115  2026-02-05 14:16:40 C=$(basename $A | sed "s/$ThisIsGzip//")
     1116  2026-02-05 14:16:47 C=$(basename $A | sed "s/ThisIsGzip//")
     1117  2026-02-05 14:16:57 ls
     1118  2026-02-05 14:17:06 history | tail
     1119  2026-02-05 14:19:47 echo $C
     1120  2026-02-05 14:21:14 for i in {ls -lR /home/examuser/ |wc -l}; do mv $A $B/$C
     1121  2026-02-05 14:21:21 for i in {$(ls -lR /home/examuser/ |wc -l)}; do mv $A $B/$C; ; done
     1122  2026-02-05 14:21:47 for i in {$(ls -lR /home/examuser/ |wc -l)}; do mv $A $B/$C; echo {i}; done
     1123  2026-02-05 14:21:51 for i in {$(ls -lR /home/examuser/ |wc -l)}; do mv $A $B/$C; echo ${i}; done
     1124  2026-02-05 14:21:54 ls
     1125  2026-02-05 14:21:58 ll /home/examuser/
     1126  2026-02-05 14:22:09 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1127  2026-02-05 14:22:33 for i in {$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do mv $A $B/$C; echo ${i}; done
     1128  2026-02-05 14:22:36 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1129  2026-02-05 14:22:39 for i in {$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do mv $A $B/$C; echo ${i}; done
     1130  2026-02-05 14:22:40 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1131  2026-02-05 14:22:59 echo $(ls -R /home/examuser/|grep -c ThisIsGzip)}
     1132  2026-02-05 14:23:01 echo $(ls -R /home/examuser/|grep -c ThisIsGzip)
     1133  2026-02-05 14:23:08 echo $(ls -lR /home/examuser/|grep -c ThisIsGzip)
     1134  2026-02-05 14:23:25 for i in {1..$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do mv $A $B/$C; echo ${i}; done
     1135  2026-02-05 14:24:06 for i in {1..$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do mv $A $B/$C; echo $i; done
     1136  2026-02-05 14:25:18 for i in {1..$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do A="find /home/examuser -type f -name "*ThisIsGzip" -print -quit" mv $A $B/$C; echo $i; done
     1137  2026-02-05 14:25:29 for i in {1..$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do A="find /home/examuser -type f -name "*ThisIsGzip" -print -quit";A;mv $A $B/$C; echo $i; done
     1138  2026-02-05 14:26:51 for i in {1..$(ls -R /home/examuser/|grep -c ThisIsGzip)}; do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname | $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))/$((basename | find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1139  2026-02-05 14:27:23 for i in $(ls -R /home/examuser/|grep -c ThisIsGzip); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname | $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))/$((basename | find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1140  2026-02-05 14:27:27 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1141  2026-02-05 14:28:24 for i in $(ls -R /home/examuser/|grep -c ThisIsGzip); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))/$((basename | find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1142  2026-02-05 14:28:39 for i in $(ls -R /home/examuser/|grep -c ThisIsGzip); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))$((basename | find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1143  2026-02-05 14:29:15 for i in $(ls -R /home/examuser/); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))$((basename | find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1144  2026-02-05 14:30:38 for i in $(ls -R /home/examuser/); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))$((basename | $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit)) | sed 's/ThisIsGzip//'); echo $i; done
     1145  2026-02-05 14:30:54 for i in $(ls -R /home/examuser/); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))$((basename | $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//')); echo $i; done
     1146  2026-02-05 14:31:37 for i in $(ls -R /home/examuser/); do mv $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) $(dirname $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit))$(basename $(find /home/examuser -type f -name "*ThisIsGzip" -print -quit) | sed 's/ThisIsGzip//'); echo $i; done
     1147  2026-02-05 14:32:14 find /home/examuser -type f -name "*ThisIsGzip" -print -quit
     1148  2026-02-05 14:34:15 ls
     1149  2026-02-05 14:34:17 gzip zipper.sh 
     1150  2026-02-05 14:34:18 ls
     1151  2026-02-05 14:34:25 gunzip zipper.sh.gz 
     1152  2026-02-05 14:34:27 ls
     1153  2026-02-05 14:35:03 man gzip
     1154  2026-02-05 14:36:42 gzip zipper.sh 
     1155  2026-02-05 14:36:45 gzip -l zipper.sh.gz 
     1156  2026-02-05 14:37:19 man gzip
     1157  2026-02-05 14:39:02 ls
     1158  2026-02-05 14:39:04 gunzip zipper.sh.gz 
     1159  2026-02-05 14:39:15 gzip zipper.sh -N gzip.gz
     1160  2026-02-05 14:39:17 ll
     1161  2026-02-05 14:39:22 gunzip zipper.sh.gz 
     1162  2026-02-05 14:39:30 gzip -N gzip.gz zipper.sh
     1163  2026-02-05 14:39:31 ll
     1164  2026-02-05 14:39:32 gunzip zipper.sh.gz 
     1165  2026-02-05 14:39:38 man gzip
     1166  2026-02-05 14:40:45 gzip zipper.sh 
     1167  2026-02-05 14:40:48 gzip -d zipper.sh.gz 
     1168  2026-02-05 14:43:30 man tar
     1169  2026-02-05 14:45:09 ls
     1170  2026-02-05 14:45:27 tar -czf zipper.sh.gz zipper.sh
     1171  2026-02-05 14:45:28 ls
     1172  2026-02-05 14:45:40 mkdir PWD
     1173  2026-02-05 14:45:41 cd PWD/
     1174  2026-02-05 14:46:06 ls
     1175  2026-02-05 14:46:07 ll
     1176  2026-02-05 14:46:12 mv ../zipper.sh.gz .
     1177  2026-02-05 14:46:13 ls
     1178  2026-02-05 14:46:34 tar -xzf zipper.sh.gz
     1179  2026-02-05 14:46:34 ll
     1180  2026-02-05 14:47:10 tar -cJf zipper.sh.xz zipper.sh
     1181  2026-02-05 14:47:15 man tar
     1182  2026-02-05 14:47:32 tar -cjf zipper.sh.bz2 zipper.sh
     1183  2026-02-05 14:47:35 man tar
     1184  2026-02-05 14:47:41 ll
     1185  2026-02-05 14:49:51 ls
     1186  2026-02-05 14:51:14 rm -f *
     1187  2026-02-05 14:51:14 ls
     1188  2026-02-05 14:51:15 clear
     1189  2026-02-05 14:51:17 man bzip2
     1190  2026-02-05 14:51:25 cp ../zipper.sh .
     1191  2026-02-05 14:51:25 ls
     1192  2026-02-05 14:51:29 man bzip2
     1193  2026-02-05 14:52:06 bzip2 -c zipper.sh zipper.sh.bz2
     1194  2026-02-05 14:52:11 man bzip2
     1195  2026-02-05 14:52:18 bzip2 -z zipper.sh zipper.sh.bz2
     1196  2026-02-05 14:52:20 ls
     1197  2026-02-05 14:52:26 bzip2 -d zipper.sh.bz2 
     1198  2026-02-05 14:52:27 ll
     1199  2026-02-05 14:52:32 bzip2 -z zipper.sh 
     1200  2026-02-05 14:52:33 ll
     1201  2026-02-05 14:53:09 ls
     1202  2026-02-05 14:53:12 bzip2 -d zipper.sh.bz2 
     1203  2026-02-05 14:53:12 ls
     1204  2026-02-05 14:53:34 bzip2 -z zipper.sh 
     1205  2026-02-05 14:53:37 bunzip2 zipper.sh.bz2 
     1206  2026-02-05 14:53:38 ls
     1207  2026-02-05 14:59:31 tar -cJf zipper.sh.tar.xz zipper.sh 
     1208  2026-02-05 14:59:36 tar -tvf zipper.sh.tar.xz 
     1209  2026-02-05 15:00:33 ll
     1210  2026-02-05 15:01:34 man tar
     1211  2026-02-05 15:12:27 man visudo
     1212  2026-02-05 15:13:49 visudo
     1213  2026-02-05 15:19:26 ls
     1214  2026-02-05 15:19:45 gzip2 -z GZIP2.gz zipper.sh zipper.sh.tar.xz 
     1215  2026-02-05 15:19:46 ll
     1216  2026-02-05 15:32:03 ls
     1217  2026-02-05 15:32:05 man zip
    ```