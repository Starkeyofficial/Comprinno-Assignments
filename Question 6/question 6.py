# Input the number of test cases

t = int(input())

# for each test case:

for i in range(t):

    # input number of legs

    n = int(input())

    if(n % 4 == 0):

        print("yes")

    else:

        print("no")