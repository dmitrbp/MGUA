A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]
    ]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]
    ]

C = [[0, 0, 0] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            C[i][j] += A[i][k] * B[k][j]

print(f'C:')
for i in range(len(C)):
    print(C[i])
