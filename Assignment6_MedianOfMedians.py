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
        A[a], A[b] = A[b], A[a]
    return a - 1


# Return the Kth order statistic among elements A[l ... r]
def orderStat(A, l, r, K):
    while l < r:
        piv = approxMed(A, l, r)
        piv_index = partition(A, l, r, piv)
        if piv_index >= K:
            r = piv_index
        else:
            l = piv_index + 1
    return A[r]


# Return the approximate median among elements A[l ... r]
def approxMed(A, l, r):
    medians = []
    if r <= l + 5:
        return A[order5(A, l, r)]
    for group in range(l, r + 1, 5):
        medians.append(A[order5(A, group, r)])
    return orderStat(medians, 0, len(medians) - 1, int(len(medians) / 2))


# Rearrange A[start, start+1, ..., min(start+4, r)] in ascending order
# Return index of the median of A[start, start+1, ..., min(start+4, r)]
def order5(A, start, r):
    for i in range(start + 1, min(start + 5, r + 1)):
        j = i
        while start + 1 <= j and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return int((start + min(start + 5, r + 1)) / 2)


if __name__ == '__main__':
    main()