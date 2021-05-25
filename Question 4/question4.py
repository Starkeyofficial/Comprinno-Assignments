# Input the number of test cases.

t = int(input())

# for each test case

for i in range(t):

    # Input the number of minutes(N).

    n = int(input())

    # Input the space saperated strings into an array (Arr).

    arr = [ i for i in input().split()]

    # Initialize flag = 0 to check whether loop break due to unfavourable conditions.

    flag = 0

    for action in range(n-2):

        if(arr[i] == 'cookie' and arr[i+1] != 'milk'):

            # set flag = 1

            flag = 1
            break

    # check for corner case

    if(flag == 0 and arr[n-1] == 'cookie'):

        flag = 1

    # print the result

    if(flag == 0):

        print("YES")

    else:

        print("NO")