def get_total_plan(steps, h):
    # steps Array that used to store the step length
    # n the total number of stairs
    f = [0] * (h + 1)
    f[0] = 1
    for i in range(1, h + 1):
        for x in steps:
            if i >= x:
                f[i] += f[i - x]
    return f[h]


print(get_total_plan([34, 44], 1500))


