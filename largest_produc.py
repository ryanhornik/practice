def my_function(arg):
    top_positive = []
    top_negative = []
    for i in range(0, len(arg)):
        if arg[i] < 0:
                if len(top_negative) < 2:
                    top_negative.append(arg[i])
                    if len(top_negative) == 2:
                        sorted(top_negative)
                else:
                    for k in range(0, 2):
                        if arg[i] < top_negative[k]:
                            top_negative[k] = arg[i]
                            break
        elif arg[i] > 0:
            if len(top_positive) < 3:
                top_positive.append(arg[i])
                if len(top_positive) == 3:
                    sorted(top_positive, reverse=True)
            else:
                for j in range(0, 3):
                    if arg[i] > top_positive[j]:
                        top_positive[j] = arg[i]
                        break

    if len(top_negative) == 2 and top_negative[0] * top_negative[1] > top_positive[0] * top_positive[1]:
        return top_negative[0], top_negative[1], top_positive[0]
    return top_positive[0], top_positive[1], top_positive[2]


triple = my_function([-3, -2, 2, 2, 3, 3])
print(triple)
print(triple[0]*triple[1]*triple[2])
