import random
import time
import matplotlib.pyplot as plt

def create_random_array(length, max_val=160, random_seed=42):
    """Membuat array dengan angka acak berdasarkan panjang tertentu."""
    random.seed(random_seed)
    return [random.randint(1, max_val) for _ in range(length)]

def is_all_unique(elements):
    """Mengembalikan True jika semua elemen dalam array unik."""
    return len(elements) == len(set(elements))

def measure_execution_time(function, *params):
    """Mengukur waktu eksekusi suatu fungsi."""
    start_time = time.perf_counter()
    function(*params)
    end_time = time.perf_counter()
    return end_time - start_time

def performance_test():
    # Panjang array yang diuji
    sizes = [100, 150, 200, 250, 300, 350, 400, 500]
    max_val = 175
    random_seed = 42

    # Untuk menyimpan hasil waktu eksekusi
    times_worst_case = []
    times_average_case = []

    for length in sizes:
        # Average case: array dengan angka acak
        avg_case_array = create_random_array(length, max_val, random_seed)

        # Worst case: array dengan elemen yang sama
        worst_case_array = [1] * length

        # Waktu untuk worst case
        time_worst_case = measure_execution_time(is_all_unique, worst_case_array)

        # Waktu untuk average case
        time_average_case = measure_execution_time(is_all_unique, avg_case_array)

        # Simpan hasil waktu
        times_worst_case.append(time_worst_case)
        times_average_case.append(time_average_case)

        # Cetak hasil waktu ke konsol
        print(f"Array Length = {length}, Worst Case Time = {time_worst_case:.10f}s, Average Case Time = {time_average_case:.10f}s")

    # Membuat plot untuk visualisasi
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_worst_case, marker='o', label='Worst Case', color='red')
    plt.plot(sizes, times_average_case, marker='s', label='Average Case', color='blue')
    plt.title('Execution Time: Worst Case vs Average Case')
    plt.xlabel('Array Length')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    performance_test()
