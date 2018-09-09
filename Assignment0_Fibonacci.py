PRIME = 30011


def main():
    import time
    start = time.clock()

    # Evaluate implemented functions measuring its CPU time on various inputs.
    # Measurement is intended to be understood as per trial on a single input not as 'for n = 1...10^10 do f(n)'

    # print(FibRec(996))
    # print(FibIter(250000004))
    print(FibRepSq(2147483647))

    print("CPU time used (s): " + str(time.clock() - start))


'''Modulo helper function'''
def Modulo(n, mod=PRIME):
    """
    @param n, mod:
    int, int
    @return:
    int. return n modulo mod
    """
    return n % mod


def FibRec(n):
    """
    20pts. Implement Fibonacci number with Recursive algorithm
    @param n:
    int
    @return:
    int. return fib(n) modulo PRIME.
    See the side section its definition
    """
    # implement here
    # check input parameter n
    if n < 0:
        print("Error: Input should be 0 or positive integer.")
        return 0
    if n == 0: return 0
    return FibRec_aux(n, 1, 0)  # n>=1

'''Tail recursive helper function'''
def FibRec_aux(n, acc_big=1, acc_small=0):
    """
    @param n, acc_big, acc_small:
    int, int, int
    @return:
    int
    """
    if n == 1: return acc_big
    return FibRec_aux(n - 1, Modulo(acc_big + acc_small), acc_big)


def FibIter(n):
    """
    20pts. Implement Fibonacci number with Iterative algorithm
    @param n:
    int
    @return:
    int. return fib(n) modulo PRIME.
    See the side section its definition
    """
    # implement here
    if n < 0:
        print("Error: Input should be 0 or positive integer.")
        return 0
    if n == 0: return 0

    # n>=1
    fib_big = 1; fib_small = 0
    while n > 1:
        tmp = fib_small
        fib_small = fib_big
        fib_big = Modulo(fib_small + tmp)
        n = n - 1
    return fib_big


def FibRepSq(n):
    """
    30pts. Implement Fibonacci number with Repeated Squaring algorithm
    @param n:
    int
    @return:
    int. return fib(n) modulo PRIME.
    See the side section its definition
    """
    # implement here
    if n < 0:
        print("Error: Input should be 0 or positive integer.")
        return 0
    if n == 0: return 0

    # n>=1
    CONSTANT = [1, 1, 1, 0]
    acc = [1, 0, 0, 1]  # init val: identity matrix
    index = []  # stack of index info about when to power
    n = n - 1  # constant matrix is multiplied n-1 times to calculate fib(n)

    # stack index
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            index.append(0)
        else:  # n is odd
            n = (n - 1) / 2
            index.append(1)

    # pop index & repeat squaring
    step = len(index)
    for i in range(step):
        if index.pop():  # power & multiply once more
            acc = MatMult(CONSTANT, MatMult(acc, acc))
        else:
            acc = MatMult(acc, acc)

    return acc[0]

'''Matrix multiplication helper function'''
def MatMult(A, B):
    """
    @param A, B:
    list(int), list(int)
    @return:
    list(int). return C=A*B, each component of C modulo PRIME
    @list component order:
    [a11, a12, a21, a22]
    """
    c11 = Modulo(A[0] * B[0] + A[1] * B[2])
    c12 = Modulo(A[0] * B[1] + A[1] * B[3])
    c21 = Modulo(A[2] * B[0] + A[3] * B[2])
    c22 = Modulo(A[2] * B[1] + A[3] * B[3])
    return [c11, c12, c21, c22]


'''
30pts (10pts each) Experiment
Try evaluating your implemented functions on different sizes of n
Determine the largest n which makes each function terminates within 30 seconds
The number ranges among (1: [0, 100], 2: [101, 10000], 
3: [10001, 1000000], 4: [1000001, 1000000000], 5: [1000000001, 2147483647])
Store the index of the range that you could reach for each function.
'''
MAX_OF_INPUT_REC = 2
MAX_OF_INPUT_ITER = 4
MAX_OF_INPUT_REPSQ = 5

if __name__ == "__main__":
    main()
