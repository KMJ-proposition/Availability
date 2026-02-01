#!/bin/bash

# DNS config

PAC_I='rpm -qi bind'
PAC_L='rpm -ql bind'
GREP_LOC='grep named.localhost'
GREP_LOO='grep named.loopback'
DIR='xargs dirname'
NAME='xargs basename'

Search_Localhost() {
	echo "정방향 DNS 설정 파일을 탐색합니다."
	$PAC_I >/dev/null
	if [[ $? -eq 0 ]]; then
		echo "파일 경로: $($PAC_I | $GREP_LOC | $DIR)"
		echo "파일 이름: $($PAC_I | $GREP_LOC | $NAME)"
		read -p "설정 파일이 존재합니다. 설정하시겠습니까?[y/n]" Choice
	else
		Update
	fi
}

Localhost() {
	cp named.localhost 
}

Search_Loopback() {
	echo "역방향 설정 파일을 탐색합니다."
	if locate named.loopback 2>/dev/null; then
		read -p "설정 파일이 존재합니다. 설정하시겠습니까?[y/n]" Choice
	else
		Update
	fi
}

Update() {
	echo "파일을 검색 중 입니다."
	read -p "파일을 찾을 수 없습니다. 검색 목록을 최신화 후 재검색하시습니까?[y/n]" Choice
	case $Choice in
		Y|y)
			echo "검색 목록을 최신화 후 재검색합니다."
			updatedb
			if [[ $Config -eq 1 ]]; then
				Localhost
			else
				Loopback
			fi
			;;
		N|n)
			echo "프로그램을 종료합니다."
			exit 0
			;;
		*)
			echo "잘못 입력하셨습니다."
			;;
	esac
}

Config() {
	echo "----- DNS 설정 프로그램을 실행합니다."
	echo "1. 정방향 DNS 설정"
	echo "2. 역방향 DNS 설정"
	read -p "----- 메뉴를 선택해주세요: " Choice
	case $Choice in
		1)
			Search_Localhost
			;;
		2)
			Search_Loopback
			;;
		*)
			echo "잘못 선택하셨습니다."
			;;
	esac
}
