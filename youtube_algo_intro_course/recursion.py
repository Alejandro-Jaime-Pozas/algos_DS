# recursion
def sum(numbers):
    # base case when just 1 num left, return that num
    if len(numbers) == 1:
        return numbers[0]
    # print(f"Calling sum({numbers[1:]})")
    remaining_sum = numbers[1:]
    # print(f"Call to sum({numbers}) returning {numbers[0]} + {remaining_sum}")
    return numbers[0] + sum(remaining_sum)

# # normal way
# def sum(numbers):
#     total = 0
#     for number in numbers:
#         total += number 
#     return total 

print(sum([1,2,7,9]))