# Dokumentasi Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching
Kode asli berasal dari https://github.com/aasthac67/Fingerprint-Matching

## Pendahuluan
Dokumen ini bertujuan untuk menjelaskan program Pencocokan Sidik Jari yang dikembangkan untuk sistem masuk. Kode program ini awalnya berasal dari repositori GitHub milik "aasthac67" dan dikembangkan lebih lanjut oleh "anasm20".
Program ini terdiri dari tiga segmen kode yang berbeda, yang melakukan berbagai tahap dalam proses pengolahan sidik jari. Tujuan utama program ini adalah membandingkan sidik jari dan mengidentifikasi kemungkinan kecocokan.

## Prasyarat
Syarat-syarat sebelum menjalankan Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching adalah sebagai berikut:
1. Telah memiliki Pyhton minimal versi 3.
2. Telah mengunduh package opencv-python, numpy, matplotlib.pyplot, skimage.feature, glob, dan os.

## Segmen Kode 1: Penghapusan Latar Belakang
![1](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/5833aaba-9cb7-4ea9-8562-eac7ae9a552f)

### Langkah 1: Memuat Gambar
Pada langkah ini, sebuah gambar input (misalnya, ‘./input/f1.jpeg’) dimuat menggunakan OpenCV dan ditampilkan dalam sebuah jendela.

### Langkah 2: Penghapusan Latar Belakang
Penghapusan latar belakang dilakukan dengan menggunakan algoritma GrabCut. Sebuah kotak di sekitar sidik jari ditetapkan sebagai Region of Interest (ROI), dan latar belakang dihapus.

### Langkah 3: Pemulihan Latar Belakang
Latar belakang ditambahkan kembali ke gambar, dan hasilnya disimpan dalam file terpisah ('input.jpg').

## Segmen Kode 2: Deteksi dan Pemrosesan Fitur
![2](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/a91810b6-a0b8-42f6-b674-895f8a127843)

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

## Segmen Kode 3: Pembandingan Sidik Jari
![3](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/3aadeff0-1c20-4af3-8cb1-8603a40039ad)

### Langkah 1: Memuat Gambar Referensi
Gambar referensi ('input_img') dimuat dan dikonversi menjadi citra grayscale.

### Langkah 2: Deteksi Fitur
Metode SIFT (Scale-Invariant Feature Transform) digunakan untuk mendeteksi titik-titik kunci dalam gambar.

### Langkah 3: Penerapan Matcher
Matcher berbasis Flann digunakan untuk mengidentifikasi kecocokan antara titik-titik kunci dalam gambar referensi dan gambar lainnya.

### Langkah 4: Visualisasi Kecocokan
Kecocokan antara gambar referensi dan gambar lainnya divisualisasikan, dan diberitahu apakah kecocokan ditemukan.

## Versi 2 memiliki banyak fitur spesifik pembandingan
![4](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/34719d1c-aeb5-4c51-89e2-161be872b6d3)

## Ringkasan
Program Pencocokan Sidik Jari ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20". Program ini dihosting di repositori GitHub publik dan digunakan untuk menjalankan berbagai tahap pengolahan sidik jari serta menjelaskannya.

Kode pertama menghapus latar belakang, yang kedua menekankan fitur, dan yang ketiga membandingkan sidik jari menggunakan titik-titik kunci dan kecocokan. Program ini dapat digunakan untuk membandingkan sidik jari dan mengidentifikasi kemungkinan kecocokan, yang dapat berguna dalam berbagai skenario keamanan dan identifikasi.
