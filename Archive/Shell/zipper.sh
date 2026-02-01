#!/bin/bash

zipper() {
	while true 
	do
		read -p "압축할 디렉터리의 경로: " LOC
		
		if [[ ! -e "$LOC" || -f "$LOC" ]]; then
			echo ">>> 디렉터리 경로를 입력하세요."
			continue
		fi

		zip -b /tmp -rq $LOC.zip $LOC
		break
	done
}

zipper
