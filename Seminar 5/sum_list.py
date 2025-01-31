def sum_list(slist: list, iter = 0):
    if iter == len(slist):
        return 0
    else:
        return slist[iter] + sum_list(slist, iter + 1)

slist = [1, 2, 3, 4, 5, 10]
print(sum_list(slist))
