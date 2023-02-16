# 用户号码：所取号码
user_list = []
# 普通排队列表
t1 = []
# vip用户排队列表
v1 = []
# 排号计数
a = 0

while 1:
    print("***欢迎使用vQueues挂号系统***")
    print("1.排队取号")
    print("2.柜台叫号")
    print("3.关闭系统")
    num = input("请输入操作对应的序号：")

    # 排队取号
    if num == "1":
        # 用户手机号码
        user_num = str(input("请输入您的手机号码："))
        user_list.append(user_num)
        a += 1
        # 用户所取号
        A_num = "A" + str(a)
        t1.append(A_num)
        print("您的排队号码是A{}，前面排队人数为{}人，请稍等。\n".format(a, len(t1) - 1))

    # 后台叫号
    elif num == "2":
        print("当前排队序列为:{}".format(t1))
        del_num = str(input("请叫号："))
        t1.remove(del_num)
        print("请{}到1号柜台办理业务，当前排队人数为{}人。".format(del_num, len(t1)))

    # 退出系统
    elif num == "3":
        print("谢谢使用，祝您生活愉快！")
        break

    # 无效操作
    else:
        print("输入错误，请重新操作！")