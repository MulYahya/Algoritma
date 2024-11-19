def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Merge Sort
sorted_merge = merge_sort(X.copy())
print("Hasil Merge Sort :", sorted_merge)

# Quick Sort
sorted_quick = quick_sort(X.copy())
print("Hasil Quick Sort :", sorted_quick)

# Analisis : Dikarenakan Merge Sort adalah cara untuk memilah kemudian menggabungkan kembali sebuah permasalahan besar maka dalam best case, worst case, dan average casenya sama. Kecepatan dalam menyortir data akan selalu sama dimana dikarenakan time complexity algoritma ini adalah O(n log n) yang berarti akan memisah jumlah masalah besar ke beberapa masalah-masalah yang kecil sehingga selalu konsisten tidak berpengaruh dengan nilai sebuah variabel didalamnya.

# Analisis : Quick Sort adalah cara mengurutkan data dengan memilih satu elemen sebagai pivot (acuan), lalu memindahkan elemen yang lebih kecil ke kiri dan elemen yang lebih besar ke kanan. Proses ini dilakukan berulang-ulang pada setiap bagian hingga semua data terurut. Dalam kondisi terbaik, pivot membagi data menjadi dua bagian yang sama besar, sehingga waktu yang dibutuhkan cukup cepat, yaitu 𝑂(𝑛 log 𝑛). Dalam kondisi rata-rata, Quick Sort juga berjalan dengan baik dan memiliki kecepatan yang sama, asalkan pembagian pivot cukup merata. Namun, pada kondisi terburuk, seperti ketika pivot selalu menjadi elemen terkecil atau terbesar (misalnya pada data yang hampir terurut), waktu yang diperlukan menjadi jauh lebih lama, yaitu 𝑂(𝑛^2), karena pembagian datanya tidak seimbang. Dengan kata lain, Quick Sort bisa sangat cepat, tetapi performanya sangat bergantung pada pemilihan pivot.