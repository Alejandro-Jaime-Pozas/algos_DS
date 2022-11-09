def sum(numbers):
    # NORMAL WAY
    # total = 0
    # for num in numbers:
    #     total += num
    # return total

    # RECURSIVE
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum

print(sum([1, 2, 7, 9]))