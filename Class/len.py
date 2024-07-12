
def sum2(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0
    return nums[0] + nums[1]


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2


def double_char(sstr):
    result = ''
    for el in sstr:
        result += el * 2
    return result


if __name__ =='__main__':
    print(caught_speeding(70, False))
    print(caught_speeding(81, False))
    print(caught_speeding(65, True))
    print(sum2([2, 9, 5, 6]))
    print(sum2([12, 45, 3]))
    print(sum2([2]))
    print(sum2([0]))
    print(double_char('oleg'))