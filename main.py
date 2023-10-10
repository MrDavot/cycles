n = int(input())
for i in range(1, n + 1):
    stair = ""
    for j in range(1, i + 1):
        stair += str(j)
    print(stair)