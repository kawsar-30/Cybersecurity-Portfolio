# 2026-11-18 13:38:32 by RouterOS 7.24.6
# software id = 0XYZ-CFZR
#
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool0 ranges=0.0.0.2-255.255.255.254
add name=dhcp_pool1 ranges=0.0.0.2-255.255.255.254
add name=pppoe_client_pool ranges=192.168.10.10-192.168.10.50
/ppp profile
add local-address=192.168.10.1 name=ISP_Broadband_Profile remote-address=\
    pppoe_client_pool
/interface pppoe-server server
add default-profile=ISP_Broadband_Profile disabled=no interface=ether2 \
    service-name=ISP_Server
/ip address
add address=192.168.0.40/24 comment=WAN_IP interface=ether1 network=\
    192.168.0.0
/ip dhcp-server
# No IP address on interface
add address-pool=*7 interface=ether2 name=dhcp1
/ip dhcp-server network
add dns-none=yes gateway=0.0.0.1
add address=192.168.11.0/24 gateway=192.168.11.1
/ip dns
set servers=8.8.8.8@main,8.8.4.4
/ip firewall nat
add action=masquerade chain=srcnat
/ip route
add disabled=no dst-address=0.0.0.0/0 gateway=192.168.0.1 routing-table=main
/ppp secret
add name=USER_KALI profile=ISP_Broadband_Profile service=pppoe
/system gps
set set-system-time=yes
