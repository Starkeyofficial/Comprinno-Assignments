# input number of test cases

t = int(input())

# for each test case:

for _ in range(t):

    # input the basic salary

    bs = int(input())

    # calculate the hra and da for each conditions

    if(bs < 1500):

        hra = float(bs * 0.1)

        da = float(bs * 0.9)

        print(float(bs) + hra + da)

    if(bs >= 1500):

        hra = 500

        da = float(bs * 0.98)

        print(float(bs) + float(hra) + da)

