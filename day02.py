print("hello sre")

ip = input("请输入IP地址：")
print("你输入的IP地址是:",ip)

if ip == "":
    print("错误：IP地址不能为空")
else:
    print("准备扫描:", ip)