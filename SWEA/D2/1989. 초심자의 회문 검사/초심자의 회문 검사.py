T = int(input())

for tc in range(1, T + 1):
    word = input().strip()
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0
    print(f"#{tc} {ans}")