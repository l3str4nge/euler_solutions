


def solution(number):
    cc = number
    factors = []
    for x in range(2, number):
        if cc % x == 0:
            factors.append(x)
            cc = cc /x
            if cc == 1:
                break

            continue
    return max(factors)



if __name__ == '__main__':
    print(solution(13195))
    print(solution(600851475143))
    # print(is_prime(7))
