# Refined Script
```Bash
#!/bin/bash
# prevention recurrence of login problem

# 1. 환경 설정
LOG_DIR="/var/log/rec"
LOG_FILE="$LOG_DIR/rec001_pam01.log"

S1="상태:1000" # 패키지 미설치
S2="상태:2000" # 디렉터리/시스템 오류
S3_1="상태:3001" # 무결성 유지
S3_2="상태:3002" # 무결성 훼손

# 2. 유틸리티 함수 (중복 제거용)
get_date() {
    date "+%Y-%m-%d %H:%M:%S"
}

log_write() {
    echo "[$(get_date) $1] $2" | tee -a "$LOG_FILE"
}

# 3. 검증 로직
root_check() {
    if [[ $EUID -ne 0 ]]; then
        echo "관리자 권한으로 실행해주세요."
        exit 1
    fi
}

create_dir() {
    if [[ ! -d "$LOG_DIR" ]]; then
        mkdir -p "$LOG_DIR" && echo ">>> 로그 디렉터리 생성 완료 ($LOG_DIR)"
    fi
    
    # 디렉터리 생성 실패 시 에러 처리
    if [[ ! -w "$LOG_DIR" ]]; then
        echo "[$(get_date) $S2] 로그 디렉터리 쓰기 권한이 없습니다."
        exit 1
    fi
}

examine() {
    local verify_out
    verify_out=$(rpm -V pam)

    if [[ -z "$verify_out" ]]; then
        log_write "$S3_1" "무결성에 문제가 발견되지 않았습니다."
    else
        log_write "$S3_2" "무결성 훼손이 발견되었습니다."
        echo "$verify_out" >> "$LOG_FILE"
        echo "$verify_out" # 화면 출력
    fi
}

main() {
    rpm -q pam &>/dev/null
    local rc=$?

    if [[ $rc -ne 0 ]]; then
        log_write "$S1" "PAM 패키지가 설치되지 않았습니다."
    else
        examine
    fi
}
```

# 4. 실행순서
root_check
create_dir
main
주요 리팩토링 포인트 (비교 분석용)
중복 제거 (DRY): 각 함수마다 반복되던 DATE 선언을 get_date와 log_write 함수로 통합했습니다. 이제 로그 형식을 바꾸고 싶을 때 함수 하나만 고치면 됩니다.

경로 변수 최적화: LOG_FILE에 전체 경로를 미리 담아 호출 시 코드를 짧게 줄였습니다.

에러 핸들링: create_dir에서 단순히 에러 메시지만 찍는 게 아니라, 쓰기 권한이 없으면 exit 1로 실행을 중단하게 하여 안정성을 높였습니다.

지역 변수 사용: 함수 내부에서만 쓰는 변수에 local을 붙여 다른 함수와의 변수 이름 충돌을 방지했습니다.

사용자님을 위한 팁
사용자님의 원본 코드에서 create_dir의 else 문에 있던 오류 로직은 "디렉터리가 이미 존재할 때" 실행되는 구조였습니다. 이는 의도와 다를 수 있어, "디렉터리를 만들 수 없거나 권한이 없을 때" 에러를 뱉도록 수정했습니다.