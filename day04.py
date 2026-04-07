from ipaddress import ip_address

print("hello sre")

ip = input("请输入IP地址：")
print("你输入的IP地址是:",ip)

if ip == "":
    print("错误：IP地址不能为空")
else:
    print("准备扫描:", ip)

ip_range = input("请输入IP范围（如192.168.1.1-10）：")

base_ip, range_part = ip_range.rsplit(".", 1)
start, end = range_part.split("-")

print(f"准备扫描{start} 到 {end}的IP")

for i in range(int(start),int(end)+1):
    ip = f"{base_ip}.{i}"
    print(f" 生成IP:{ip}")

print("ip列表生成完毕")

import subprocess

def ping_ip(ip):
    """ping单个IP,返回True(存活)或False(不存活)"""
    result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip],
                          capture_output=True)
    return result.returncode == 0

for i in range(int(start),int(end)+1):
    ip = f"{base_ip}.{i}"

    if ping_ip(ip):
        print(f"[存活]{ip}")
    else:
        print(f"[不存活】{ip}")