import numpy as np

# Membuat matriks
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Menghitung transpose matriks
A_transpose = np.transpose(A)

# Menghitung determinan matriks
det_A = np.linalg.det(A)

try:
    # Menghitung invers matriks
    A_inv = np.linalg.inv(A)
    # Menampilkan hasil
    print("Matriks A:")
    print(A)
    print("\nInvers dari A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("Matriks A adalah matriks singular, tidak dapat diinvers.")

# Menampilkan hasil
print("\nMatriks A:")
print(A)
print("\nTranspose dari A:")
print(A_transpose)
print("\nDeterminan dari A:", det_A)
