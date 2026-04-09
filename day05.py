import subprocess

def ping_ip(ip):
    """ping单个IP,返回True(存活)或False(不存活)"""
    result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip],
                          capture_output=True)
    return result.returncode == 0

# 主程序
ip_range = input("请输入IP范围(如192.168.1.1-10): ")
base_ip, range_part = ip_range.rsplit(".", 1)
start, end = range_part.split("-")

print(f"准备扫描 {start} 到 {end} 的IP")

alive = []
dead = []

for i in range(int(start), int(end) + 1):
    ip = f"{base_ip}.{i}"
    if ping_ip(ip):
        alive.append(ip)
        print(f"[存活] {ip}")
    else:
        dead.append(ip)
        print(f"[不存活] {ip}")

print(f"\n扫描完成: 存活{len(alive)}个, 不存活{len(dead)}个")

# 保存报告
with open("scan_report.txt", "w") as f:
    f.write(f"IP扫描报告\n总计: {len(alive)+len(dead)}个\n存活: {len(alive)}个\n不存活: {len(dead)}个\n\n")
    f.write("存活列表:\n")
    for ip in alive:
        f.write(f"  {ip}\n")

print("报告已保存到 scan_report.txt")