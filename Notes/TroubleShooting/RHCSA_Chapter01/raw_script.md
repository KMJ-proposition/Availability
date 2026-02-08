# Raw Script

```bash
 1	#!/bin/bash
 2	# prevention reccurence of login problem
 3	# 패키지 기반 무결성 검증
 4	
 5	examine() {
 6		if [[ $(rpm -V pam | wc -l) -ne 0 ]]; then
 7			echo "[상태:0100] 무결성이 훼손되었습니다."
 8		else
 9			echo "[상태:1000] 무결성에 문제가 발견되지 않았습니다."
10		fi
11	}
12	
13	description() {
14		echo ">>> 상태 코드"
15		echo ">>> 000x: 설치 관련"
16		echo ">>> 00x0: 오류"
17		echo ">>> 0x00: 무결성 훼손"
18		echo ">>> x000: 무결성 유지"
19	}
20	
21	main() {
22		description
23	
24		rpm -qi pam &>/dev/null
25		
26		if [[ $? -ne 0 ]]; then
27			echo "[상태:0001] PAM 패키지가 설치되지 않았습니다."	
28		elif [[ $? -eq 0 ]]; then
29			examine
30		else
31			echo "[상태:0010] 오류가 발생하였습니다."
32		fi
33	}
34	
35	main
```