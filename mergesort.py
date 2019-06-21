def mergesort(lst):
    if len(lst) <= 1:
        return lst
    A = mergesort(lst[:len(lst)//2])
    B = mergesort(lst[len(lst)//2:])
    out = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    for k in range(i, len(A)):
        out.append(A[k])
    for k in range(j, len(B)):
        out.append(B[k])
    return out


print(mergesort([5, 4, 3, 2, 1, 0]))
print(mergesort([5, 4, 10, 15, 3, 2, -1, -1000, 1000, 3, 2, 1, 0]))
