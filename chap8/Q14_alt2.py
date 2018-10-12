COUNT = 0

def count_eval(s, result):
    global COUNT
    COUNT += 1
    if len(s) == 0: return 0
    if len(s) == 1: return 1 if bool(s) == result else 0

    ways = 0

    for i in range(1, len(s), 2):
        c = s[i]
        left = s[0:i]
        right = s[i+1:len(s)]

        sub_ways = 0

        left_true = count_eval(left, True)
        left_false = count_eval(left, False)
        right_true = count_eval(right, True)
        right_false = count_eval(right, False)
        total = (left_true + left_false)*(right_true + right_false)

        total_true = 0
        if c == '^':
            if result:
                sub_ways = left_true*right_false + left_false*right_true
            else:
                sub_ways = left_true*right_true + left_false*right_false
        elif c == '&':
            if result:
                sub_ways = left_true*right_true
            else:
                sub_ways = left_true*right_false + left_false*right_true + left_false*right_false
        elif c == '|':
            if result:
                sub_ways = left_true*right_true + left_false*right_true + left_true*right_false
            else:
                sub_ways = left_false*right_false

        ways += sub_ways

    return ways

if __name__ == '__main__':
    expression = "0^0|1&1^1|0|1"
    result = True

    ways = count_eval(expression, result)
    print(f'{ways}/{COUNT}')
