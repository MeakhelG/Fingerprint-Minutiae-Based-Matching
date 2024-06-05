## Pendahuluan

Sidik jari telah lama menjadi salah satu metode utama untuk identifikasi personal dalam berbagai aplikasi, mulai dari forensik hingga sistem keamanan digital. Dengan kemajuan teknologi, metode otomatis untuk pencocokan sidik jari telah berkembang pesat, memberikan akurasi dan efisiensi yang lebih tinggi dibandingkan metode manual. Salah satu teknik yang digunakan dalam pencocokan sidik jari adalah Minutiae Based Matching, yang fokus pada titik-titik khusus pada sidik jari, seperti bifurkasi dan titik ujung.

Dalam proyek ini, kami akan mengeksplorasi Program Pencocokan Sidik Jari berbasis Minutiae, yang melibatkan beberapa tahap pemrosesan gambar dan analisis. Program ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20", serta dihosting di repositori GitHub publik. Kami akan membahas prasyarat untuk menjalankan program ini, berbagai segmen kode yang terlibat, serta langkah-langkah pemrosesan dari penghapusan latar belakang hingga pencocokan minutiae dan penentuan kecocokan sidik jari.

Melalui langkah-langkah ini, kita akan melihat bagaimana algoritma seperti thresholding, thinning, dan penggunaan KD Tree untuk pencocokan minutiae diterapkan untuk mencapai hasil yang akurat dan efisien dalam pencocokan sidik jari. Program ini memanfaatkan beberapa paket Python seperti OpenCV, numpy, dan matplotlib untuk mengolah dan menganalisis citra sidik jari.

Di bawah ini, kami akan memulai dengan prasyarat yang diperlukan untuk menjalankan program ini, diikuti dengan segmen-segmen kode yang menjelaskan setiap tahap pemrosesan sidik jari secara detail.

## Prasyarat
Syarat-syarat sebelum menjalankan Program Pencocokan Sidik Jari berdasarkan Minutiae Based Matching adalah sebagai berikut:
1. Telah memiliki Pyhton minimal versi 3.11.4.
2. Telah mengunduh package opencv-python, numpy, matplotlib.pyplot, skimage.feature, glob, dan os dengan benar.

## Diagram Alur Algoritma


## Segmen Kode 1 : Penghapusan Latar Belakang
![Screenshot 2024-06-04 110547](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/0a9b9c3c-1877-4993-9acf-e6e5b5c80ba4)

## Langkah 1: Memuat Gambar
Pada langkah ini, sebuah gambar input (misalnya, ‘./input/f1.jpeg’) dimuat menggunakan OpenCV dan ditampilkan dalam sebuah jendela.

## Langkah 2: Penghapusan Latar Belakang
Penghapusan latar belakang dilakukan dengan menggunakan algoritma K-MEANS, lalu mengubah gambar menjadi array 2D, menentukan jumlah kluster

## Segmenn Kode 2 : Proses Filtering
Latar belakang ditambahkan kembali ke gambar, dan hasilnya disimpan dalam file t
![Screenshot 2024-06-04 110711](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/24a8371d-bf3f-4bc1-befd-c24df9eef468)
![Screenshot 2024-06-04 110736](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/b45ea42d-e2fe-46da-aae7-3270346e8123)
![Screenshot 2024-06-04 110749](https://github.com/MeakhelG/Fingerprint-Minutiae-Based-Matching/assets/113085615/d5e03bf3-9994-4d5d-bc16-ce12c0436499)


### Langkah 1: Memuat Gambar
Gambar yang dihasilkan pada Langkah 1 dikonversi menjadi gambar biner.
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
### Langkah 3 : Ekstrasi Minutiae
Setelah mendapatkan garis tengah, dilakukan iterasi pada setiap piksel pada citra hasil thinning untuk menemukan minutiae. Minutiae diidentifikasi berdasarkan pola garis tengah. Minutiae dapat berupa titik bifurkasi (terbagi menjadi dua) atau titik ujung (berakhir). Mengidentifikasi titik-titik penting seperti titik ujung dan titik bifurkasi dari garis tengah yang telah diperoleh melalui thinning.
### Langkah 4 : Pencocokan Minutiae
Setelah mendapatkan minutiae dari kedua gambar sidik jari, dilakukan pencocokan minutiae antara keduanya. Pencocokan dilakukan dengan mencari minutiae dari gambar pertama yang memiliki jarak terdekat dengan minutiae dari gambar kedua, dengan memperhitungkan threshold jarak yang telah ditentukan. Menggunakan KD Tree untuk mencocokkan minutiae dari dua gambar sidik jari. Pencocokan dilakukan dengan mencari minutiae pada kedua gambar yang memiliki jarak terdekat satu sama lain, dengan memperhitungkan threshold jarak yang telah ditentukan.
### Langkah 5 : Penentuan Kecocokan Sidik Jari 
Berdasarkan hasil pencocokan minutiae, ditentukan apakah kedua sidik jari cocok atau tidak berdasarkan rasio jumlah minutiae yang cocok terhadap total jumlah minutiae pada masing-masing gambar.

## Ringkasan
Program Pencocokan Sidik Jari ini awalnya dikembangkan oleh "aasthac67" dan kemudian dikembangkan lebih lanjut oleh "anasm20". Program ini dihosting di repositori GitHub publik dan digunakan untuk menjalankan berbagai tahap pengolahan sidik jari serta menjelaskannya.  algoritma yang digunakan dalam kode tersebut adalah thresholding, thinning, ekstraksi minutiae, pencocokan minutiae menggunakan KD Tree, dan penentuan kecocokan sidik jari berdasarkan rasio jumlah minutiae yang cocok. KD-Tree digunakan untuk mencocokkan minutiae dari dua gambar sidik jari. Ini membantu dalam mencari minutiae pada gambar kedua yang memiliki jarak terdekat dengan minutiae pada gambar pertama dengan cara yang efisien, sehingga membantu dalam pencocokan sidik jari yang akurat.
## Referensi
https://github.com/aasthac67/Fingerprint-Matching
https://github.com/drat/Program-Pencocokan-Sidik-Jari
