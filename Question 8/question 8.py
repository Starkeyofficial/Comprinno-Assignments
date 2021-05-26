# input the number of test cases

t = int(input())

# for each test case:

for _ in range(t):

    # input the value of a, b and n

    a, b, n = [int(i) for i in input().split()]

    for turn in range(n):

        # if turn is even or 0, then it is A's turn, otherwise B's

        if(turn == 0 or turn%2 == 0):

            a *= 2

        else:

            b *= 2

    # calculate the result 

    res = max(a,b)/min(a,b)

    # print the result

    print(res)