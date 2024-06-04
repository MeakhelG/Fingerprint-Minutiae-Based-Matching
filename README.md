@ -7,7 +7,7 @@ Program ini terdiri dari tiga segmen kode yang berbeda, yang melakukan berbagai

## Prasyarat
Syarat-syarat sebelum menjalankan Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching adalah sebagai berikut:
1. Telah memiliki Pyhton minimal versi 3.
1. Telah memiliki Pyhton minimal versi 3.11.4
2. Telah mengunduh package opencv-python, numpy, matplotlib.pyplot, skimage.feature, glob, dan os.

## Segmen Kode 1: Penghapusan Latar Belakang
@ -26,7 +26,7 @@ Latar belakang ditambahkan kembali ke gambar, dan hasilnya disimpan dalam file t
![Screenshot 2024-06-04 110711](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/24a8371d-bf3f-4bc1-befd-c24df9eef468)
![Screenshot 2024-06-04 110736](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/b45ea42d-e2fe-46da-aae7-3270346e8123)
![Screenshot 2024-06-04 110749](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/d5e03bf3-9994-4d5d-bc16-ce12c0436499)

![Screenshot 2024-06-04 110800](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/3c90a98d-5a36-4c54-be88-c2af6b1636f3)
![Screenshot 2024-06-04 110813](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/cce25c0c-5e7a-4583-a2b0-40e73a99debc)

### Langkah 1: Memuat Gambar
@ -50,8 +50,10 @@ Gambar yang dihasilkan pada Langkah 5 dikonversi menjadi gambar biner, dan berba
### Langkah 7: Algoritma Thinning
Algoritma Thinning atau Skeletonization diterapkan pada gambar biner, dan hasilnya disimpan.

## Segmen Kode 3: Pembandingan Sidik Jari
![3](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/3aadeff0-1c20-4af3-8cb1-8603a40039ad)
## Segmen Kode 3: Ekstraksi Minutiae 
![Screenshot 2024-06-04 111051](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/a298ab10-2c1a-47c1-93f1-a6c7e99d798f)
![Screenshot 2024-06-04 111032](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/ea9f353e-4164-49e1-b371-127d3f6ae45d)


### Langkah 1: Memuat Gambar Referensi
Gambar referensi ('input_img') dimuat dan dikonversi menjadi citra grayscale.
@ -65,8 +67,6 @@ Matcher berbasis Flann digunakan untuk mengidentifikasi kecocokan antara titik-t
### Langkah 4: Visualisasi Kecocokan
Kecocokan antara gambar referensi dan gambar lainnya divisualisasikan, dan diberitahu apakah kecocokan ditemukan.

## Versi 2 memiliki banyak fitur spesifik pembandingan
![4](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/34719d1c-aeb5-4c51-89e2-161be872b6d3)

## Ringkasan
Program Pencocokan Sidik Jari ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20". Program ini dihosting di repositori GitHub publik dan digunakan untuk menjalankan berbagai tahap pengolahan sidik jari serta menjelaskannya.
