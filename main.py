# 用户列表
user_list = {}
# 员工列表
worker_list = {}

while 1:
    print("***欢迎使用vQueues挂号系统***")
    print("1.排队取号")
    print("2.柜台叫号")
    print("3.关闭系统")
    num = input("请输入操作对应的序号：")

    # 退出系统
    if num == "3":
        break
