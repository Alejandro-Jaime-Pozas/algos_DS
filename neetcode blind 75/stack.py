def isValid(s):
    stack = []
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False  

print(isValid('{}[]'))

    # # order does matter
    # # somehow need to track which brackets are opening/closing and in which order to determine if valid
    # # looks like the order of closing is what matters really here.
    # # so when you close a bracket, should correspond in order to the last opened bracket there
    # brackets = []
    # open, close = 0, 0
    # for b in s:
    #     if b in {'(', '[', '{'}:
    #         brackets.append(b)
    #         open += 1
    #     elif b in {')', ']', '}'}:
    #         close += 1
    #         # if there exist open brackets already
    #         if brackets:
    #             if brackets[-1] == '(' and b == ')':
    #                 brackets.pop()
    #             elif brackets[-1] == '[' and b == ']':
    #                 brackets.pop()
    #             elif brackets[-1] == '{' and b == '}':
    #                 brackets.pop()
    #             else:
    #                 return False
    #     # if char is not bracket type return false
    #     else:
    #         return False
    # return True if not brackets and open == close else False 

# print(isValid('{}[]')) # where would this be wrong? bc an open was no closed properly? or bc extra closing parentheses in end? prob the first option