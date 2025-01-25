def rand_num_cr():
    import random
    rand_num = random.randint(0, 10)
    return rand_num


a = [rand_num_cr(), rand_num_cr(), rand_num_cr(), rand_num_cr(), rand_num_cr(), rand_num_cr()]
average = int(sum(a)/len(a))
print(f'average: {average}')
count = 0
while True:
    for i in range(len(a)):
        if a[i] <= average:
            continue
        elif a[i] > average:
            surplus = a[i]-average
            if i == len(a) - 1 and a[-1] > average:
                surplus = a[i] - average
                a[0] += surplus
                a[i] = average
            else:
                a[i+1] += surplus
                a[i] = average
        count += 1
        print(f'Array: {a} -- Cycles counter: {count}')

        if all(x >= average for x in a):
            print("Done!")
            exit(0)