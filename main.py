#Fungsi Matrix
class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    # Fungsi untuk mencari elemen terbesar dan terkecil dalam matriks
    def find_max_min(self):
        flattened = [item for sublist in self.matrix for item in sublist]
        max_val = max(flattened)
        min_val = min(flattened)
        return max_val, min_val

    # Fungsi untuk mentranspose matriks
    def transpose_matrix(self):
        transposed = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed

    # Fungsi untuk perkalian matriks
    def matrix_multiplication(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix):
            return "Error: Jumlah kolom pada matrix pertama harus sama dengan jumlah baris pada matrix kedua"

        result = [[0 for _ in range(len(other_matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(other_matrix[0])):
                for k in range(len(other_matrix)):
                    result[i][j] += self.matrix[i][k] * other_matrix[k][j]

        return result

    # Fungsi untuk penjumlahan matriks
    def matrix_addition(self, other_matrix):
        if len(self.matrix) != len(other_matrix) or len(self.matrix[0]) != len(other_matrix[0]):
            return "Error: Matrix harus memiliki dimensi atau penjumlahan yang sama."

        result = [[self.matrix[i][j] + other_matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return result

if __name__ == "__main__":
    A = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_ops = MatrixOperations(A)

    # Menghitung elemen terbesar dan terkecil dalam matriks A
    max_val, min_val = matrix_ops.find_max_min()
    print(f"Elemen terbesar: {max_val}")
    print(f"Elemen terkecil: {min_val}")

    # Transpose matriks A
    transposed_matrix = matrix_ops.transpose_matrix()
    print("Transpose Matrix:")
    for row in transposed_matrix:
        print(row)

    # Melakukan perkalian matriks A dengan transpose dari A
    multiplication_result = matrix_ops.matrix_multiplication(transposed_matrix)
    print("Hasil perkalian A dengan transpose dari A:")
    for row in multiplication_result:
        print(row)

    # Melakukan penjumlahan matriks A dengan transpose dari A
    addition_result = matrix_ops.matrix_addition(transposed_matrix)
    print("Hasil penjumlahan A dengan transpose dari A:")
    for row in addition_result:
        print(row)