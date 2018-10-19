
def sortTwoNumbers_dc(x):
    try:
        x[0] - x[1]
    except:
        out = "You need to enter two *NUMBERS* !"
    else:
        if len(x) > 2:
            out = "You need to enter *TWO* numbers !"
        elif x[0] > x[1]:
            out = [x[1], x[0]]
        elif x[0] < x[1]:
            out = x
    return out