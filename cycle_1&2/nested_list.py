print("\nJerry James SJC23MCA036")
print("MCA 2023-2025 \n")

X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[1,2,3,],[4,5,6],[7,8,9]]
result = [[X[i][j] + Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]
for r in result:
    print(r)