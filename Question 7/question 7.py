# input the number of testcase

t = int(input())

# for each test case:

for i in range(t):

    # input the number of sticks

    n=input()

    # input the length of sticks in an array

    lst = [int(i) for i in input().split()]

    # declare an empty list

    l2=[]

    for i in range(n):

        if(lst.count(lst[i]) > 1):

            # appending each stick with count > 1

            l2.append(lst[i])

    if len(l2)>3:

        # sort the resulting list

        l2.sort()

        # reverse the list

        l2.reverse()

        # print the area 

        print(l2[0]*l2[3])

    else:
        
        print('-1')