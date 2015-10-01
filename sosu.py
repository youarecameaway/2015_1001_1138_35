n = 20
s_list = []
for x in range(2, n):
    for s in s_list:
        if x%s is 0:
            break
    else:
        s_list.append(x)

for s in s_list:
    print(s)
