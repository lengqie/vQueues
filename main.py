import userUtils

# 用户号码：所取号码
user_list = []
# 普通排队列表
a_user_list = []
# vip用户排队列表
v_user_list = []
# 排号计数 （没有用户时为-1）
index = -1

while 1:
    print("***欢迎使用vQueues挂号系统***")
    print("1.排队取号")
    print("2.柜台叫号")
    print("3.关闭系统")
    num = input("请输入操作对应的序号：")

    # 排队取号
    if num == "1":
        # 用户手机号码
        user_num = input("请输入您的手机号码：")

        # 输入判断
        if not userUtils.is_number(user_num):
            print("输入异常")
            continue
        vip = userUtils.is_vip(user_num)
        # 临时用户字典
        temp_user_dic = {
            "number": user_num,
            "vip": vip
        }
        user_list.append(temp_user_dic)
        # 记录用户在user list中的位置
        index += 1

        # 临时长度 用来判断当前用户类型数量
        temp_len = 0
        # 如果是vip用户
        if vip:
            v_user_list.append(index)
            temp_len = len(v_user_list)
        else:
            a_user_list.append(index)
            temp_len = len(a_user_list)
        # 用户所取号
        print("您的排队号码是A{}，前面排队人数为{}人，请稍等。\n".format(6, temp_len - 1))

    # 后台叫号
    elif num == "2":
        print("当前排队序列为:{}".format(a_user_list))
        del_num = input("请叫号：")
        a_user_list.remove(del_num)
        print("请{}到1号柜台办理业务，当前排队人数为{}人。".format(del_num, len(a_user_list)))

    # 退出系统
    elif num == "3":
        print("谢谢使用，祝您生活愉快！")
        break

    # 无效操作
    else:
        print("输入错误，请重新操作！")