import coin_throw as coin_throw
import time as time


if __name__ == '__main__':

    for _ in range(0, 5):
        print(coin_throw.CoinThrow.avg_throws())
    print(coin_throw.CoinThrow.avg_throws(5, 10000))

    for _ in range(0, 5):
        print(coin_throw.CoinThrow.avg_throws_smp())
    print(coin_throw.CoinThrow.avg_throws_smp(5, 10000))

    start = time.time()
    print(coin_throw.CoinThrow.avg_throws(15, 1000))
    end = time.time()
    print(f"Took {end-start}")

    start = time.time()
    print(coin_throw.CoinThrow.avg_throws_smp(15, 1000))
    end = time.time()
    print(f"Took {end-start}")
