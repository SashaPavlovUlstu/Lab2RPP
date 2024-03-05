import random
def make_matrix(N,M):
    matrix = [];
    for i in range(N):
        row  =[]
        for j in range(M):
            row.append(random.randint(1, 100))
        matrix.append(row)
    return matrix
def mnozh_matrix(matrix):
    res = 1
    for i in range(N):
        res *= matrix[len(matrix)-i-1][i]
    return res


N_input = input("Введите (N): ")
M_input = input("Введите (M): ")

try:
    N = int(N_input)
    M = int(M_input)
except ValueError:
    print("Нужные корректные значения")
    quit()

matrix = make_matrix(N, M)

print(mnozh_matrix((matrix)))
with open("C:\\Users\\sasha\\OneDrive\\Рабочий стол\\РПП\\Лаб2\\output.txt", "w") as file:
    file.write("Matrix:\n")
    for row in matrix:
        file.write(' '.join([f'{val:6d}' for val in row]) + '\n')

    result = mnozh_matrix(matrix)
    file.write(f"\nResult: {result}")
print("Git")
print("clone Git")