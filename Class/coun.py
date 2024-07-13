
def sum13(nums):
    count = 0
    el = 0
    while el < len(nums):
        if nums[el] == 13:
            el += 2
            continue
        count += nums[el]
        el += 1
    return count


if __name__ == "__main__":
    print(sum13([4, 6, 1, 4, 5, 13, 45]))
