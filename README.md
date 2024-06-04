Program merupakan pengembangan dari program blbla yang mana program ini terdiri dari tiga segmen kode yang berbeda, yang melakukan berbagai

## Prasyarat
Syarat-syarat sebelum menjalankan Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching adalah sebagai berikut:
1. Telah memiliki Pyhton minimal versi 3.
1. Telah memiliki Pyhton minimal versi 3.11.4
2. Telah mengunduh package opencv-python, numpy, matplotlib.pyplot, skimage.feature, glob, dan os.

## Segmen Kode 1 : Penghapusan Latar Belakang

![Screenshot 2024-06-04 110547](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/0a9b9c3c-1877-4993-9acf-e6e5b5c80ba4)

## Segmenn Kode 2 : Proses Filtering
Latar belakang ditambahkan kembali ke gambar, dan hasilnya disimpan dalam file t
![Screenshot 2024-06-04 110711](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/24a8371d-bf3f-4bc1-befd-c24df9eef468)
![Screenshot 2024-06-04 110736](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/b45ea42d-e2fe-46da-aae7-3270346e8123)
![Screenshot 2024-06-04 110749](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/d5e03bf3-9994-4d5d-bc16-ce12c0436499)


### Langkah 1: Memuat Gambar
Gambar yang dihasilkan pada Langkah 1 dikonversi menjadi gambar biner, dan berba
### Langkah 2: Menggunakan Proses High Boots Filtering
Meningkatkan ketajaman gambar dengan mengurangi komponen kabur dari gambar asli.
### Langkah 3 : Menggunakan Grayscale Filtering

### Langkah 4 : Fungsi CLAHE (Histogram)
Teknik penyesuaian histogram yang membatasi kontras untuk memperbaiki kontras gambar.
### Langkah 5 : Binary Image
Thresholding dilakukan setelah citra dikonversi ke citra grayscale. Tujuannya adalah untuk memisahkan area sidik jari dari latar belakang dengan cara mengubah citra grayscale menjadi citra biner, di mana piksel dengan intensitas di atas ambang batas akan dianggap sebagai bagian dari sidik jari, sedangkan piksel dengan intensitas di bawah ambang batas akan dianggap sebagai latar belakang.
### Langkah 6 : Thining 
Algoritma Thinning atau Skeletonization diterapkan pada gambar biner, dan hasilnya disimpan. Dilakukan thinning pada citra biner untuk mendapatkan garis tengah sidik jari. Thinning adalah proses untuk mengurangi lebar garis sehingga menjadi satu piksel lebar.

## Segmen Kode 3: Ekstraksi Minutiae 
![Screenshot 2024-06-05 061047](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/7955a94c-c0d3-4ce9-812f-a9816672acaa)
![Screenshot 2024-06-05 061039](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/7eda2abe-d651-436e-9246-e8b6366d752c)


### Langkah 1: Memuat Gambar Referensi
Gambar referensi ('input_img') dimuat dan dikonversi menjadi citra grayscale. Matcher berbasis Flann digunakan untuk mengidentifikasi kecocokan antara titik-t
### Langkah 4: Visualisasi Kecocokan
Kecocokan antara gambar referensi dan gambar lainnya divisualisasikan, dan diberitahu apakah kecocokan ditemukan.
#### Langkah 3 : Ekstrasi Minutiae
Setelah mendapatkan garis tengah, dilakukan iterasi pada setiap piksel pada citra hasil thinning untuk menemukan minutiae. Minutiae diidentifikasi berdasarkan pola garis tengah. Minutiae dapat berupa titik bifurkasi (terbagi menjadi dua) atau titik ujung (berakhir). Mengidentifikasi titik-titik penting seperti titik ujung dan titik bifurkasi dari garis tengah yang telah diperoleh melalui thinning.
### Langkah 4 : Pencocokan Minutiae
Setelah mendapatkan minutiae dari kedua gambar sidik jari, dilakukan pencocokan minutiae antara keduanya. Pencocokan dilakukan dengan mencari minutiae dari gambar pertama yang memiliki jarak terdekat dengan minutiae dari gambar kedua, dengan memperhitungkan threshold jarak yang telah ditentukan. Menggunakan KD Tree untuk mencocokkan minutiae dari dua gambar sidik jari. Pencocokan dilakukan dengan mencari minutiae pada kedua gambar yang memiliki jarak terdekat satu sama lain, dengan memperhitungkan threshold jarak yang telah ditentukan.
### Langkah 5 : Penentuan Kecocokan Sidik Jari 
Berdasarkan hasil pencocokan minutiae, ditentukan apakah kedua sidik jari cocok atau tidak berdasarkan rasio jumlah minutiae yang cocok terhadap total jumlah minutiae pada masing-masing gambar.

## Ringkasan
Program Pencocokan Sidik Jari ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20". Program ini dihosting di repositori GitHub publik dan digunakan untuk menjalankan berbagai tahap pengolahan sidik jari serta menjelaskannya.  algoritma yang digunakan dalam kode tersebut adalah thresholding, thinning, ekstraksi minutiae, pencocokan minutiae menggunakan KD Tree, dan penentuan kecocokan sidik jari berdasarkan rasio jumlah minutiae yang cocok. KD-Tree digunakan untuk mencocokkan minutiae dari dua gambar sidik jari. Ini membantu dalam mencari minutiae pada gambar kedua yang memiliki jarak terdekat dengan minutiae pada gambar pertama dengan cara yang efisien, sehingga membantu dalam pencocokan sidik jari yang akurat.
