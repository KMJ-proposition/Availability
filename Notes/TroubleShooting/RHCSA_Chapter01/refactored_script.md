# Refactored Script
* 개선점
    - 

```bash
#!/bin/bash
# prevention reccurence of login problem
# 패키지 기반 무결성 검증

# 실행 권한 검증
root() {
	if [[ $EUID -ne 0 ]]; then
		echo "관리자 권한으로 실행해주세요."
		exit 1
	fi
}

# file
LOG_DIR="/var/log/rec"
LOG_FILE="rec001_pam01.log"
# status
S1="상태:1000" # 설치 여부
S2="상태:2000" # 오류
S3="상태:3000" # 무결성
S3_1="상태:3001" # 무결성 유지
S3_2="상태:3002" # 무결성 훼손

# script
create_dir() {
	if [ ! -d "$LOG_DIR" ]; then
		mkdir -p "$LOG_DIR"
		echo ">>> 로그 기록용 디렉터리를 생성하였습니다."
		echo ">>> 경로: $LOG_DIR"
	else
		DATE="$(date +%Y-%m-%d_%H-%M-%S)"
		echo "[$DATE $S2] 오류가 발생하였습니다." | tee -a "$LOG_DIR/$LOG_FILE"
	fi
}

examine() {
	VERIFY="$(rpm -V pam)"
	if [[ -z "$VERIFY" ]]; then
		DATE="$(date +%Y-%m-%d_%H-%M-%S)"
		echo "[$DATE $S3_1] 무결성에 문제가 발견되지 않았습니다."
	else
		DATE="$(date +%Y-%m-%d_%H-%M-%S)"
		printf "%s\n%s\n" "[$DATE $S3_2]" "$VERIFY" | tee -a "$LOG_DIR/$LOG_FILE"
		echo "[$DATE $S3_2] 무결성이 훼손되었습니다."
	fi
}

main() {
	rpm -q pam &>/dev/null
	RC=$?

	if [[ $RC -ne 0 ]]; then
		DATE="$(date +%Y-%m-%d_%H-%M-%S)"
		printf "%s\n%s\n" "[$DATE $S1]" "PAM 패키지가 설치되지 않았습니다." | tee -a "$LOG_DIR/$LOG_FILE"
	else
		examine
	fi
}

# execute
root
create_dir
main
```