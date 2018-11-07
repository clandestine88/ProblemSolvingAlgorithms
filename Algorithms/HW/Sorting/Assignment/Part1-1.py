def solve(nuts, bolts):
    #
    # Write your code here.
    #
    res = []
    i = 0
    for i in range(len(nuts)):
        for j in range(len(bolts)):
            if nuts[i] == bolts[j]:
                res.append(str(nuts[i]) + " " + str(bolts[j]))
                break
    return res
    # nuts = sorted(nuts)
    # bolts = sorted(bolts)
    # res = []
    # i = 0
    # while i < len(nuts):
    #     res.append([str(nuts[i]) + " " + str(bolts[i])])
    #     i += 1
    # print(res)
    # return res

NUTS = [4, 32, 5, 7]
BOLTS = [32, 7, 5, 4]
print(solve(NUTS,BOLTS))


if __name__ == "__main__":
    f = sys.stdout

    nuts_count = int(input())

    nuts = []

    for _ in range(nuts_count):
        nuts_item = int(input())
        nuts.append(nuts_item)

    bolts_count = int(input())

    bolts = []

    for _ in range(bolts_count):
        bolts_item = int(input())
        bolts.append(bolts_item)

    res = solve(nuts, bolts)

    f.write('\n'.join(res))
    f.write('\n')

    f.close()

