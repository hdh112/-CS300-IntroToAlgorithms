'''
This skeleton code shows you how to deal with input/output.
It is highly recommended to use this input/output method as is.
'''


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    answer = orderStat(A, 0, len(A) - 1, K)
    print(answer)


'''Helper function'''


# Partitions A[l ... r] into A[l ... m] entries < y and A[m+1 ... r] those >=y.
# Returns m.
def partition(A, l, r, y):
    if l >= r:  # A[l] ... A[r] sorted
        return
    a = l;
    b = r
    while a < b:
        while a < b and A[a] < y:
            a += 1
        while a < b and A[b] >= y:
            b -= 1
        A[b], A[a] = A[a], A[b]
    return a - 1


# Return the Kth order statistic among elements A[l ... r]
def orderStat(A, l, r, K):
    # i=0
    while l < r:  # and i<5:
        # i+=1
        # print("l, r:", l, r)
        # print(A)
        piv = approxMed(A, l, r)
        # print("piv:", piv)
        piv_index = partition(A, l, r, piv)
        # print("piv_index:", piv_index)
        if piv_index >= K:
            r = piv_index
        else:
            l = piv_index + 1
    # print("r:", r)
    return A[r]


# Return the approximate median among elements A[l ... r]
def approxMed(A, l, r):
    if r <= l + 5:
        return A[order5(A, l, r)]
    for group in range(l, r + 1, 5):
        m = order5(A, group, r)
        # print("m:", m)
        A[m], A[l + int((group - l) / 5)] = A[l + int((group - l) / 5)], A[m]
    return orderStat(A, l, l + int((r - l) / 5), int((r - l) / 10))


# Rearrange A[start, start+1, ..., min(start+4, r)] in ascending order
# Return index of the median of A[start, start+1, ..., min(start+4, r)]
def order5(A, start, r):
    for i in range(start + 1, min(start + 5, r + 1)):
        j = i
        while start + 1 <= j and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    # print("A:", A)
    return int((start + min(start + 5, r + 1)) / 2)


if __name__ == '__main__':
    main()