l1 = [10, 11, 14, 23, 46, 50, 53, 53, 73, 75, 81, 89, 90, 91, 92, 98]
l2 = [5, 15, 24, 25, 29, 33, 39, 41, 52, 53, 55, 63, 76, 85, 89, 92]
l3 = [1,1,5]
l4 = [2,3,4,5,6]

def merge_parallels(l1, l2):
    r = []
    i, j = 0, 0
    while True:
        if i < len(l1):
            if j < len(l2):
                if l1[i] <= l2[j]:
                    r.append(l1[i])
                    i += 1
                else:
                    r.append(l2[j])
                    j += 1
            else:
                r.append(l1[i])
                i += 1
        else:
            if j < len(l2):
                r.append(l2[j])
                j += 1
            else:
                break
    return r


print(merge_parallels(l1,l2))
print(merge_parallels(l3,l4))


