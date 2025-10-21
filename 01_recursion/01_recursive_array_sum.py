# def calculate_sum(numbers, index):
#     if index == len(numbers) - 1:
#         return numbers[index]
#
#     return numbers[index] + calculate_sum(numbers, index + 1)
#
#
# nums = [int(x) for x in input().split()]
# print(calculate_sum(nums, 0))


def calculate_sum(numbers, index, depth=0):
    indent = "  " * depth
    if index == len(numbers) - 1:
        val = numbers[index]
        print(f"{indent}base: return {val}")
        return val

    print(f"{indent}call: index={index}, value={numbers[index]}")
    rest = calculate_sum(numbers, index + 1, depth + 1)
    total = numbers[index] + rest
    print(f"{indent}compute: {numbers[index]} + {rest} = {total}")
    return total

nums = [int(x) for x in input().split()]
result = calculate_sum(nums, 0)
print("final sum =", result)