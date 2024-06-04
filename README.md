# Dokumentasi Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching
Kode asli berasal dari https://github.com/aasthac67/Fingerprint-Matching

## Pendahuluan
Dokumen ini bertujuan untuk menjelaskan program Pencocokan Sidik Jari yang dikembangkan untuk sistem masuk. Kode program ini awalnya berasal dari repositori GitHub milik "aasthac67" dan dikembangkan lebih lanjut oleh "anasm20".
Program ini terdiri dari tiga segmen kode yang berbeda, yang melakukan berbagai tahap dalam proses pengolahan sidik jari. Tujuan utama program ini adalah membandingkan sidik jari dan mengidentifikasi kemungkinan kecocokan.

## Prasyarat
Syarat-syarat sebelum menjalankan Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching adalah sebagai berikut:
1. Telah memiliki Pyhton minimal versi 3.11.4
2. Telah mengunduh package opencv-python, numpy, matplotlib.pyplot, skimage.feature, glob, dan os.

## Segmen Kode 1: Penghapusan Latar Belakang
![Screenshot 2024-06-04 110547](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/0a9b9c3c-1877-4993-9acf-e6e5b5c80ba4)

### Langkah 1: Memuat Gambar
Pada langkah ini, sebuah gambar input (misalnya, ‘./input/f1.jpeg’) dimuat menggunakan OpenCV dan ditampilkan dalam sebuah jendela.

### Langkah 2: Penghapusan Latar Belakang
Penghapusan latar belakang dilakukan dengan menggunakan algoritma GrabCut. Sebuah kotak di sekitar sidik jari ditetapkan sebagai Region of Interest (ROI), dan latar belakang dihapus.

### Langkah 3: Pemulihan Latar Belakang
Latar belakang ditambahkan kembali ke gambar, dan hasilnya disimpan dalam file terpisah ('input.jpg').

## Segmen Kode 2: Deteksi dan Pemrosesan Fitur
![Screenshot 2024-06-04 110711](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/24a8371d-bf3f-4bc1-befd-c24df9eef468)
![Screenshot 2024-06-04 110736](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/b45ea42d-e2fe-46da-aae7-3270346e8123)
![Screenshot 2024-06-04 110749](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/d5e03bf3-9994-4d5d-bc16-ce12c0436499)
![Screenshot 2024-06-04 110800](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/3c90a98d-5a36-4c54-be88-c2af6b1636f3)
![Screenshot 2024-06-04 110813](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/cce25c0c-5e7a-4583-a2b0-40e73a99debc)

### Langkah 1: Memuat Gambar
Gambar yang telah diproses dalam segmen kode sebelumnya ('input.jpg') dimuat.

### Langkah 2: Pemajuan Gambar
Gambar diproses dengan kernel pemajuan untuk menampilkan tepi dan fitur.

### Langkah 3: Konversi ke Grayscale
Gambar dikonversi menjadi citra grayscale untuk mempermudah pemrosesan.

### Langkah 4: Equalisasi Histogram
Equalisasi histogram diterapkan untuk meningkatkan kontras gambar.

### Langkah 5: Deteksi Ridge
Dengan menggunakan matriks Hessian, tepi (ridge) pada gambar terdeteksi, dan hasilnya divisualisasikan.

### Langkah 6: Binarisasi
Gambar yang dihasilkan pada Langkah 5 dikonversi menjadi gambar biner, dan berbagai tahap pemrosesan gambar diterapkan.

### Langkah 7: Algoritma Thinning
Algoritma Thinning atau Skeletonization diterapkan pada gambar biner, dan hasilnya disimpan.

## Segmen Kode 3: Ekstraksi Minutiae 
![Screenshot 2024-06-04 194056](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/be554f7c-87b2-432a-86d2-289c44692d28)
![Screenshot 2024-06-04 194026](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/72ed0242-dbf1-4810-abea-b1f2178f2383)


### Langkah 1: Memuat Gambar Referensi
Gambar referensi ('input_img') dimuat dan dikonversi menjadi citra grayscale.

### Langkah 2: Deteksi Fitur
Metode SIFT (Scale-Invariant Feature Transform) digunakan untuk mendeteksi titik-titik kunci dalam gambar.

### Langkah 3: Penerapan Matcher
Matcher berbasis Flann digunakan untuk mengidentifikasi kecocokan antara titik-titik kunci dalam gambar referensi dan gambar lainnya.

### Langkah 4: Visualisasi Kecocokan
Kecocokan antara gambar referensi dan gambar lainnya divisualisasikan, dan diberitahu apakah kecocokan ditemukan.


## Ringkasan
Program Pencocokan Sidik Jari ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20". Program ini dihosting di repositori GitHub publik dan digunakan untuk menjalankan berbagai tahap pengolahan sidik jari serta menjelaskannya.

Kode pertama menghapus latar belakang, yang kedua menekankan fitur, dan yang ketiga membandingkan sidik jari menggunakan titik-titik kunci dan kecocokan. Program ini dapat digunakan untuk membandingkan sidik jari dan mengidentifikasi kemungkinan kecocokan, yang dapat berguna dalam berbagai skenario keamanan dan identifikasi.
