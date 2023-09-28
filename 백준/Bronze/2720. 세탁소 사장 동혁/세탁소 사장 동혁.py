testcaseCount = int(input())

for i in range(testcaseCount):
    testcase = int(input())
    q = testcase // 25
    testcase %= 25

    d = testcase // 10
    testcase %= 10

    n = testcase // 5
    testcase %= 5

    p = testcase // 1
    testcase %= 1

    print(q, d, n, p)