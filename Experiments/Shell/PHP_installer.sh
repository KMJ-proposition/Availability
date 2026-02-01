#!/bin/bash

while true; do

	echo "------------------------------------------------"
	echo ">>> PHP 웹서버 설치 스크립트를 실행합니다."
	echo ">>> PHP 8.1 버전이며 RHEL 9에서 지원합니다."
	echo "1] 설치 진행 및 실행"
	echo "2] SELinux/방화벽 등록"
	echo "3] 종료"
	read -p ">>> 메뉴를 선택해주세요: " menu

	case $menu in
		1)
			# install php
			rpm -qi php-fpm 1>/dev/null
			if [[ $? -ne 0 ]]; then
				dnf module install php:8.1 -y
				rpm -qi php-fpm | echo ">>> 설치 패키지: $(grep -E "Name|Version" | cut -d: -f2 | tr '\n' ' ')"
				if [[ $? -eq 0 ]]; then echo ">>> php 패키지가 정상적으로 설치되었습니다."; fi
			else
				echo ">>> php 패키지가 이미 설치되어 있습니다."
			fi

			# install httpd
			rpm -qi httpd 1>/dev/null
			if [[ $? -ne 0 ]]; then
				dnf install httpd -y
				rpm -qi php-fpm 1>/dev/null | echo ">>> 설치 패키지: $(grep -E "Name|Version" | cut -d: -f2 | tr '\n' ' ')"
				if [[ $? -eq 0 ]]; then
					echo ">>> httpd 패키지가 정상적으로 설치되었습니다."
				fi
				echo ">>> httpd 패키지가 설치 완료되었습니다."
			else
				echo ">>> httpd 패키지가 이미 설치되어 있습니다."
			fi
			# starting daemon
			systemctl enable php-fpm httpd --now 1>/dev/null
			if [[ $? -eq 0 ]]; then 
				echo ">>> php, httpd 데몬이 정상적으로 실행되었습니다."
				echo ">>> 지금부터 php, httpd 데몬을 서버 시작마다 자동으로 실행합니다."
			else
				echo "[오류] 데몬 실행에 오류가 발생하였습니다."
			fi

			# testiong server
			systemctl status php-fpm httpd 1>/dev/null
			if [[ $? -eq 0 ]]; then
				PORT=$(grep ^Listen $(httpd -V | grep -E "HTTPD_ROOT|SERVER_CONFIG_FILE" | cut -d= -f2 | sed -e 's/"//g'| paste -sd '/') | cut -d' ' -f2)
				echo ">>> 현재 웹서버가 $PORT번 포트를 사용 중 입니다."
				INDEX_LOC="$(grep ^DocumentRoot $(httpd -V | grep -E "HTTPD_ROOT|SERVER_CONFIG_FILE" | cut -d= -f2 | sed -e 's/"//g'| paste -sd '/') | awk -F'\"' '{ print $2 }')"
				echo '<?php phpinfo(); ?>' > $INDEX_LOC/index.php
				if [[ $? -eq 0 ]]; then
					cat $INDEX_LOC/index.php 1>/dev/null
					curl localhost
				fi
				echo ">>> 웹 서버가 정상적으로 실행 중 입니다."
			fi
			;;
		2)
			rpm -qi firewalld 1>/dev/null
			if [[ $? -ne 0 ]]; then
				echo ">>> 방화벽 패키지를 설치합니다."
				dnf install firewalld -y
				echo ">>> 방화벽 패키지가 설치되었습니다."
				systemctl status firewalld 1>/dev/null
				if [[ $? -ne 0 ]]; then
					echo ">>> 방화벽이 작동중이지 않습니다."
					systemctl enable firewalld --now 1>/dev/null
					echo ">>> 지금부터 firewalld 데몬이 서버 시작마다 자동으로 실행됩니다."
					(ps -e | grep -E "httpd|php-fpm") && (pgrep httpd && pgrep php-fpm) 1>/dev/null
					if [[ $? -ne 1 ]]; then
						echo ">>> 방화벽에 서비스 포트를 등록합니다.";
						PORT=$(grep ^Listen $(httpd -V | grep -E "HTTPD_ROOT|SERVER_CONFIG_FILE" | cut -d= -f2 | sed -e 's/"//g'| paste -sd '/') | cut -d' ' -f2)
						{
							firewall-cmd --permanent --add-port=$PORT/tcp
							firewall-cmd --permanent --add-service=http
							firewall-cmd --reload
							firewall-cmd --list-all | grep -E "\s(ports|services)"
						}
						echo ">>> 방화벽 설정 완료"
					fi
				fi
			fi

			rpm -qi selinux-policy 1>/dev/null
			if [[ $? -ne 0 ]]; then
				echo ">>> SELinux가 설치되지 않았습니다."
			else
				if [[ $(getenforce) == "Enforcing" || $(grep -wi ^selinux=enforcing=.* $(rpm -qc selinux-policy)) ]]; then
					echo ">>> SELinux가 활성화 중 입니다."
				else
					read -p ">>> SELinux가 동작중이지 않습니다. 활성화 하겠습니까?[y/n]" SE_SET
					case $SE_SET in
						y|Y)
							setenforce Enforcing
							# sed -i "s/\(SELINUX=\).*/\1enforcing/gI" $(rpm -qc selinux-policy)
							# 내용 치환 후 재부팅 필요.
							echo ">>> SELinux를 활성화했습니다."
							;;
						n|N)
							echo ">>> SELinux 설정을 취소하셨습니다."
							;;
						*)
							echo ">>> SELinux 활성화 여부를 선택해주세요."
							;;
					esac
				fi
			fi

			INDEX_LOC="$(grep ^DocumentRoot $(httpd -V | grep -E "HTTPD_ROOT|SERVER_CONFIG_FILE" | cut -d= -f2 | sed -e 's/"//g'| paste -sd '/') | awk -F'\"' '{ print $2 }')"
			semanage fcontext -l | grep "$INDEX_LOC(/.*)" 1>/dev/null
			if [[ $? -eq 0 ]]; then
				semanage fcontext -a -t httpd_sys_content_t "$INDEX_LOC(/.*)" 1>/dev/null
				echo ">>> SELinux에 httpd 디렉터리를 등록하였습니다."
				echo ">>> $(semanage fcontext -l | grep -wo "$INDEX_LOC(/.*) ")"
				chattr +i -R $INDEX_LOC
				echo ">>> 디렉터리 수정과 삭제가 불가능하게 설정였습니다."
				echo ">>> $(lsattr $INDEX_LOC | tr '\n' ' ')"
			else
				echo ">>> SELinux에 httpd 디렉터리가 이미 등록되어 있습니다."
				echo ">>> $(semanage fcontext -l | grep "$INDEX_LOC(/.*) ")"
				chattr +i -R $INDEX_LOC
				echo ">>> 디렉터리 수정과 삭제가 불가능하게 설정였습니다."
				echo ">>> $(lsattr $INDEX_LOC | tr '\n' ' ')"
			fi
			;;
		3)
			echo ">>> PHP 웹서버 설치 스크립트를 종료합니다."
			exit 0
			;;
	esac

done
