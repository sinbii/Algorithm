def search_count(P, target):
    l, r = 1, P
    cnt = 0
    while True:
        cnt += 1
        c = (l + r) // 2
        if c == target:
            return cnt
        elif c > target:
            r = c
        else:
            l = c

T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    a_cnt = search_count(P, Pa)
    b_cnt = search_count(P, Pb)

    if a_cnt < b_cnt:
        result = "A"
    elif a_cnt > b_cnt:
        result = "B"
    else:
        result = "0"

    print(f"#{tc} {result}")
