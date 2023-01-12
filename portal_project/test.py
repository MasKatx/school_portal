n = int(input())
lst = []
for i in range(n):
    new_lst = list(input().split())
    lst.append(new_lst)
result = 0
a = 0
b = 0
print(lst)
for i in range(n):
    a += 1
    for j in range(n):
        b = 0
        if lst[i][b] == "T" and b < n:
            print(a, b, "tai 1")
            b += 1
            if b == n:
                b = 0
                break
            if lst[i][b] == "C" and b < n:
                print(a, b, "tai 2")
                b += 1
                if b == n:
                    b = 0
                    break
                if lst[i][b] == "B" and b < n:
                    print(a, b, "tai 3")
                    result += 1
                    print(result)
                    if b == n:
                        b = 0
                        break
                else:
                    break
            else:
                break

    # for j in range(n):
    #     if lst[a][j] == "T":
    #         if lst[a][j] == "C":
    #             if lst[a][j] == "B":
