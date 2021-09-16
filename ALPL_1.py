import numpy as np
import sys, os


penyimpanan = []

def clr():
   if os.name == 'clearscreen':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def underScore():
    return "\n_______________________________________________________________________"

def printMatriks(a, n):
    for i in range(n):
        print("\t", end="")
        for j in range(n):
            print(round(a[i][j], 2), "\t", end="")
        print()
    print("\n")




def printHasilMatriks(a, n):
    for i in range(n):
        print("\t", end="")
        for j in range(n+1):
            print(round(a[i][j], 2), "\t", end="")
            if (j == n-1):
                print("|", end=" ")
        print()
    print("\n")




def eleminasiGauss(a, n):
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Mengandung Pembagian Terhadap Nol!')

        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]        
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    # Back Substitution
    x[n-1] = a[n-1][n] / a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x

n = 0
print("\n\n+                                                                +")
print("|  a11     a12     a13     ...     a1j  |  |  x1  |       |  b1  |")
print("|  a21     a22     a23     ...     a2j  |  |  x2  |   ＝  |  b2  |")
print("|   :       :       :       :       :   |  |  :   |       |   :  |")
print("|  ai1     ai2     ai3     ...     aij  |  |  x3  |       |  bi  |")
print("+                                                                +")
n = int(input('\n\n Berapa Jumlah Variabel Yang Ingin Dicari ?    : '))

A = np.zeros((n, n))
a = np.zeros((n, n))
Matriks = np.zeros((n, n))
x = np.zeros((n))
b = []


print(underScore())
print(f"Silahkan Masukkan Elemen/Angka Matriks A({n} x {n})")
print("Masukkan Elemen/Angka dan pisah dengan Spasi, dan Tekan Enter Untuk Baris Baru!\n\nContoh Inputan:\n")
print(">>>\ta11\ta12\ta13\t...\ta1n")
print(">>>\ta21\ta22\ta23\t...\ta2n ")
print(">>>\t :\t :\t :\t :\t :")
print(">>>\tam1\tam2\tam3\t...\tamn \n\n")
print("Input (A): \n")
for i in range(n):
    print(">>>\t", end="")
    listBaru = filter(None, input().split(" "))
    listBaru = list(map(float, listBaru))  
    penyimpanan.append(listBaru)
A = penyimpanan.copy()
penyimpanan.clear()
print(underScore())


print("Silahkan Masukkan Elemen/Angka Vektor B")
print("Masukkan Elemen/Angka dan pisah dengan Spasi, dan Tekan Enter Untuk Baris Baru!\n\nContoh Inputan:\n")
print(">>>\tb1\tb2\tb3\t...\tbn\n\n")
print("Input (b): \n")
print(">>>\t", end="")

listBaru = filter(None, input().split(" "))
listBaru = list(map(float, listBaru)) 
penyimpanan.append(listBaru) 
b = penyimpanan.copy()
penyimpanan.clear()
print(underScore())

for i in range(n):
    for j in range (n):
        a[i][j] = A[i][j]
    A[i].append(b[0][i])




# Metode Eleminasi Gauss
# =====================================================================================================================




print("\n\n\nMatriks (A) Anda :   \n")
printMatriks(A, n)
print("Vektor (b) Anda :   \n")
for i in range(n):
    print("\t", round(b[0][i], 2))

x = eleminasiGauss(A, n)

print("\n\nAugumented Matrix Akhir Adalah : \n")
printHasilMatriks(A, n);
print()

print('\n\nMaka Vektor (x) :  \n')
for i in range(n):
    print("\t", round(x[i], 2))          

print('\n\nSolusi Yang Dicari Adalah :  \n\n')
for i in range(n):
    print('x%d = %0.2f' %(i+1,round(x[i], 2)), end = '\t')
print("\n\n\n")

input("Tekan Enter untuk Keluar ...")
print("\t\t Terima Kasih Telah Menggunakan Program Ini ")
