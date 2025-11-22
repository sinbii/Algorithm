T = int(input())

for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 보기
    for p in reversed(prices):
        if p < max_price:
            profit += max_price - p
        else:
            max_price = p

    print(f"#{tc} {profit}")
