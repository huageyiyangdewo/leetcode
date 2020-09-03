import math


def find_prime_count(m, n):
    """
    输入m,n(1 < m < n < 1000000)，返回区间[m,n]内的所有素数的个数
    https://blog.csdn.net/weixin_42889383/article/details/102887282
    :param m:
    :param n:
    :return:
    """

    assert 1 < m < n

    count = 0
    if m == 2:
        count += 1
        m += 1

    for i in range(m, n + 1, 2):

        square = int(math.sqrt(i))

        j = 2
        for j in range(2, square + 1):

            if i % j == 0:
                break

        if j >= square:
            count += 1

    return count


print(find_prime_count(3, 1000000))
