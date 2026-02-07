🟦 작업 1 — 사용자 및 그룹 관리
- devops 사용자를 UID 2045로 생성하시오.
- 기본 그룹은 devteam으로 설정하시오.
- /shared 디렉터리를 생성하고 소유자를 devops:devteam으로 설정하시오.
- /shared 디렉터리에 SGID 비트를 설정하시오.

```bash
useradd -m devops
groupadd devteam
mkdir /shared
usermod -u 2045 -g devteam devops
chown devops:devteam /shared
chmod g+s /shared
```


🟦 작업 2 — 파일 권한 및 ACL
- /secure/data.txt 파일을 생성하시오.
- 사용자 analyst에게 읽기/쓰기 ACL을 부여하시오.
- 기본 권한은 640으로 설정하시오.
- ACL이 적용되었는지 확인하시오.
- 다음 부팅에서 일시적으로 rescue 모드로 진입하도록 설정하시오.
```bash
mkdir /secure
touch /secure/data.txt
setfacl -m u:analyst:rw /secure/data.txt
getfacl /secure/data.txt
chmod 0640 /secure/data.txt 
systemctl reboot --boot-loader-entry=rescue
```


🟦 작업 3 — SELinux 관리- /webdata 디렉터리를 생성하시오.
- Apache가 이 디렉터리를 읽을 수 있도록 SELinux 컨텍스트를 설정하시오.
- 컨텍스트가 영구적으로 유지되도록 설정하시오.
- SELinux 모드가 Enforcing인지 확인하시오.
```bash
mkdir /webdata
semanage fcontext -a -t httpd_sys_content_t "/webdata(/.*)?"
restorecon -R -v /webdata
getenforce
```


🟦 작업 4 — 스토리지 구성 (LVM)- /dev/sdb의 첫 번째 파티션을 생성하시오.
- PV로 초기화하고, VG 이름은 data_vg, LV 이름은 data_lv로 생성하시오.
- LV 크기는 300MB로 설정하시오.
- 파일 시스템은 XFS로 생성하고 /mnt/data에 영구적으로 마운트하시오.
```bash
fdisk -l /dev/sdb
pvcreate /dev/sdb1
vgcreate data_vg /dev/sdb1
lvcreate -L 300m data_vg -n data_lv
mkfs.xfs /dev/data_vg/data_lv 
xfs_info /dev/data_vg/data_lv 
blkid
vi /etc/fstab
mount /dev/data_vg/data_lv /mnt/data
systemctl daemon-reload
tail -n 1 /etc/fstab 
/dev/mapper/data_vg-data_lv	/mnt/data			xfs		defaults		0 0
```


🟦 작업 5 — 네트워크 설정- 인터페이스 ens224에 다음 설정을 적용하시오.
- IP: 192.168.50.20
- Netmask: 255.255.255.0
- Gateway: 192.168.50.1
- 설정이 재부팅 후에도 유지되도록 하시오.
- 네트워크 연결을 재시작하시오.
```bash
cat /etc/NetworkManager/system-connections/ens224.nmconnection 
[connection]
id=ens224
uuid=24da71cb-99ee-3dba-a3b6-052889f6bbf3
type=ethernet
autoconnect-priority=-999
interface-name=ens224
timestamp=1770444203

[ethernet]

[ipv4]
address1=192.168.50.20/24
gateway=192.168.50.1
method=manual

[ipv6]
addr-gen-mode=eui64
method=disabled

[proxy]
```
```bash
nmcli connection reload
nmcli connection down ens224 
nmcli connection up ens224
```


🟦 작업 6 — 서비스 관리- httpd 서비스를 설치하시오.
- 서비스가 부팅 시 자동으로 시작되도록 설정하시오.
- 방화벽에서 HTTP 서비스를 허용하시오.
- 서비스가 정상적으로 실행 중인지 확인하시오.
```bash
systemctl enable httpd --now
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
systemctl status httpd
```


🟦 작업 7 — 부팅 및 GRUB 관리- 시스템의 기본 타겟을 multi-user.target으로 변경하시오.
```bash
systemctl set-default multi-user.target
```


🟦 작업 8 — 아카이브 및 압축- /project 디렉터리를 /backup/project.tar.gz로 압축하시오.
- 압축 파일이 정상적으로 생성되었는지 확인하시오.
```bash
tar -czf /backup/project.tar.gz /project
tar -tvf /backup/project.tar.gz
```


🟦 작업 9 — 패키지 관리- vim-enhanced 패키지를 설치하시오.
- 설치된 패키지 버전을 확인하시오.
```bash
rpm -qi vim-enhanced | grep -i version
```


🟦 작업 10 — 스케줄링- 사용자 devops가 매일 03:30에 /usr/local/bin/backup.sh를 실행하도록 cron 작업을 설정하시오.
```bash
crontab -l
30 03 * * * bash /usr/local/bin/backup.sh
```