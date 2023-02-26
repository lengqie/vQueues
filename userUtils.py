# 判断输入号码是否合法
def is_number(number: str) -> bool:
    # 输入为数字，且 长度为11（暂时）
    return number.isdecimal() and len(number) == 11


# 判断是否为vip用户
def is_vip(number: str) -> bool:
    # 使用后两位为偶数 （暂时）
    t = number[-2:]
    t = int(t)
    return t % 2 + t // 10 % 2 == 0



if __name__ == '__main__':
    print(32 % 2)
    print(32 // 10 % 2)
    pass
