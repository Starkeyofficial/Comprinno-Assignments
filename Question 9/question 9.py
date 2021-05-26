# input the number of tesst cases

t = int(input())

# for each test case:

for _ in range(t):

    # input the sixe of array

    n = int(input())

    # input the array

    arr = [int(i) for i in input().split()]

    # the minimum value can be achieved only if we remove elements adjacent to the minimum number of the array

    # minimum element of array is:

    num = min(arr)

    # print the result

    print(num * (n - 1))

    