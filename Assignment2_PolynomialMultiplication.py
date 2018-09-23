'''
This skeleton code shows you how to deal with input/output.
You may or may not utilize this skeleton code.
You can also start from scratch.
'''

# Threshold to switch from long multiplication to Karatasuba
THRESHOLD = 500


def main():
    N = int(input())
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))

    C = multiply(N, A, B)

    for c in C:
        print('%.10f' % c, end=' ')


def multiply(N, A, B):
    C = []  # C = A*B

    # wlog 2|N
    if N % 2 != 0:  # if N is odd
        isOdd = True
        N += 1  # make N even
        A.append(0.0)
        B.append(0.0)
    else:
        isOdd = False

    # index to split A and B
    N_half = N // 2
    # make halves of A and B
    A0 = A[:N_half]
    A1 = A[N_half:]
    B0 = B[:N_half]
    B1 = B[N_half:]

    if N > THRESHOLD:  # Karatsuba algorithm
        C0 = multiply(N_half, A0, B0)
        C2 = multiply(N_half, A1, B1)
        prod1 = multiply(N_half, AddSubLists('+', A0, A1), AddSubLists('+', B0, B1))
        inter = AddSubLists('-', prod1, C0)  # intermediate result
        C1 = AddSubLists('-', inter, C2)
    else:  # long multiplication
        C0 = multiplySplits(N_half, A0, B0)
        C2 = multiplySplits(N_half, A1, B1)
        C1 = AddSubLists('+', multiplySplits(N_half, A0, B1), multiplySplits(N_half, A1, B0))

    for index in range(N * 2 - 1):
        if index < N_half:
            C.append(C0[index])
        elif N_half <= index < N - 1:
            C.append(C0[index] + C1[index - N_half])
        elif index == N - 1:
            C.append(C1[index - N_half])
        elif N <= index < N + N_half - 1:
            C.append(C1[index - N_half] + C2[index - N])
        else:
            C.append(C2[index - N])

    # Pop out the additional 0-coefficient elements
    if isOdd:
        C.pop()
        C.pop()

    return C

'''Helper function to multiply split coefficients - long multiplication'''
def multiplySplits(N_half, A_split, B_split):
    N = N_half * 2
    C_split = []  # C_split = A_split * B_split

    for j in range(N_half):
        coef = 0
        for i in range(j + 1):
            coef += A_split[i] * B_split[j - i]
        C_split.append(coef)

    for j in range(N_half, N - 1):
        coef = 0
        for i in range(j - N_half + 1, N_half):
            coef += A_split[i] * B_split[j - i]
        C_split.append(coef)
    return C_split

'''Helper function to add/subtract lists by element'''
def AddSubLists(sign, list1, list2):
    if sign == '+':  # addition
        return [list1[i] + list2[i] for i in range(len(list1))]
    elif sign == '-':  # subtraction
        return [list1[i] - list2[i] for i in range(len(list1))]


if __name__ == '__main__':
    main()