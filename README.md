# Sistem_Rekomendasi_Restoran
Aplikasi sistem rekomendasi restoran berbasis user-based collaborative filtering (UBCF) menggunakan pendekatan cosine similarity untuk mencari kemiripan antar user dan metode KNN serta pengujian menggunakan metode RMSE (Root Mean Square Eror) dan MAE (Mean Absolute Eror)<br>
aplikasi ini menggunakan public dataset yang diperoleh dari situs kaggle yang berisikan daftar restoran Mexico dan rating yang diberikan oleh pelanggan terhadap masing masing restoran yang terdaftar. <br>
terdapat 1162 data rating pelanggan dengan skala 0-2 (ratingdataset.csv) dan 113 restoran (restodataset.csv) yang diberikan rating. <br>
setelah dilakukan preprocessing data didapatkan 97 restoran (resto_dataset3.csv) dengan skala rating user yang dirubah menjadi skala 1-3 sejumlah 873 record (dataasli.csv). <br>
aplikasi yang digunakan untuk membuat sistem rekomendasi ini menggunakan Spyder melalui Anaconda Navigator dan menggunakan library Scikit Surprise. <br>

![Screenshot (891)](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/548f5a3c-b727-4a38-aa39-d501fc8022bc)<br>
gambar : hasil sistem rekomendasi restoran. <br> 
## cleaning data : <br> 
proses preprocessing dilakukan untuk mengkondisikan data sesuai dengan kebutuhan, pada projek ini dilakukan sebagai berikut: <br> 
1. proses menggabungkan 2 dataset nama restoran dengan prefensi masakannya berpatokan pada ID resto.<br>
dapat dilihat pada dataset chefmozcuisine.xlsx dan geoplaced.xlsx menjadi resto_dataset3.csv
   ![merge ](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/f3da0847-0b8e-4031-9134-fc2a871d2c4b)<br>
2. proses menghilangkan Char pada Id pelanggan <br>
   menggunakan fitur dari ms.Exel yaitu flashfill<br>
   ![flashfill](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/cf27315a-3d47-4f2a-9f52-a04b6af48e99)<br>

sehingga didapatkan 2 dataset yang siap digunakan yaitu prefensi masakan dari restoran (resto_dataset3.csv) dan id pelanggan beserta rating yang telah diberikan kepada restoran (dataasli.csv)<br>

kemudian untuk cara kerja sistem rekomendasi ini, akan diputuskan terlebih dahulu untuk merekomendasikan restoran kepada salah satu user atau mencari test subjek yang akan menerima rekomendasi restoran. pada penelitian ini akan diambil user dengan ID 1005 sebagai test subject.<br> 
![test subjek](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/f0ac4131-0ca5-42f5-9399-a7e62bf1171f)<br>
lalu karena berbasis USER_BASED program akan mencari daftar user yang telah memberikan rating terhadap restoran yang sama dengan yang telah diberikan rating oleh user dengan ID 1005 sebagai test subjek yang akan menerima rekomendasi restoran dengan menghitungnya menggunakan cosine similarity. <br> 
![matriks similaritas](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/c89b40f0-5410-412b-b383-95f0ce0ffc1f)<br> 
jika dilihat pada tabel adalah sebagai berikut<br>
![tabel berdasarkan user](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/0aaebc9f-003f-4d60-a83f-702c45e0535a)<br>
setelah dihitung keseluruhan user akan diambil 10 user yang paling mendekati atau bernilai 1<br>
![10 user dengan kemiripan yang sama](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/4517d5e8-7c5d-49db-912e-b7073414e38b)<br> 
jika sudah menemukan user yang serupa maka akan dicari restoran mana saja yang telah diberikan rating oleh user-user tersebut. <br>
![daftar rating dengan userserupa](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/cf9a7fc5-6dac-4176-b8d4-bbd6b70ee238)<br>
dapat dilihat pada gambar diatas merupakan daftar restoran yang telah diberikan rating oleh beberapa user lain yang telah memberikan rating terhadap restoran yang sama dengan user test subjek (user 1005), dan jika dilihat untuk masing masing restoran yang berbeda saya berikan warna yang berbeda, sehingga jika dihitung untuk setiap warna yang berbeda didapatkan 36 restoran yang berbeda dari seluruh restoran yang telah diberikan rating oleh test ID dan kawan-kawannya. <br> 
kemudian dilakukan perhitungan untuk mencari bobot restoran yang akan direkomendasikan kepada test subjek <br>
![perintah untuk mencari kandidat](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/6342cb8d-a09a-4b48-bc84-6987c37ceeaf)<br>
![perhitungan resto](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/6bc6b1eb-09b4-4d32-817e-37deab2bb79d) <br>
perhitungan dilakukan kepada 36 restoran tersebut <br>
![hasil perhitungan pada 36 restoran](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/e7aa3636-1c52-4dda-9746-f6c3f41309c2)<br>

## filtering<br> 
setelah didapatkan hasil perhitungan untuk ke-36 restoran dilakukan filtering untuk mencegah sistem merekomendasikan restoran yang sama yang pernah dikunjungi oleh test subjek <br> 
![perintah filter resto](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/6d887bec-2e4e-4ed6-a747-448684673123)<br> 
berikut adalah daftar resto yang pernah dikunjungi test subjek dan tidak lolos filter <br> 
![daftar resto yang pernah dikunjungi](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/85443794-c5d2-4991-97f2-5277ba3b67aa)<br> 
dan berikut adalah hasil rekomendasi restoran dengan point tertinggi yang direkomendasikan untuk user dengan ID 1005. <br> 
![hasil akhir](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/ddadd471-45a9-41c3-8259-e1ecb86a7173)<br> 
## pengujian <br> 
pengujian dilakukan menggunakan metode RMSE (Root Mean Squared Error) dan MAE (Mean Absolute Error) <br> 
hal ini dilakukan untuk mengetahui tingkat ketidak akuratan sistem didalam melakukan prediksi, untuk kasus yang lebih sensitif dan dataset memiliki tingkat outlier kecil maka kita akan berpatokan pada RMSE saja. <br> 
![hasil pengujian](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/ac4c95e3-8021-450a-9039-885531fe912a)<br>
dapat dilihat bahwa sistem ini masih memiliki tingkat eror yang cukup tinggi yaitu yang paling kecil dari pembagian train test tersebut adalah 0.67 menggunakan RMSE dengan pembagian 7:3, hal tersebut membuktikan bahwa sistem ini masih belum cukup akurat didalam memberikan rekomendasi secara spesifik preferensi masakan yang diminta <br> 
![hasil](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/eea9ee7c-482d-42f6-aa8f-68d67b6142a0)<br> 
dapat dilihat dari 2 tabel diatas bahwa tabel diatas adalah prefensi masakan dari user 1005 dan tabel bawahnya merupakan preferensi yang direkomendasikan <br> 
dapat dilihat terdapat 3 preferensi diluar dari preferensi masakan yang telah diberikan rating oleh userdengan ID 1005 yakni mexican, seafood, dan international, hal ini disebabkan karena sistem rekomendasi ini menggunakan User-based sebagai basis dari rekomendasinya sehingga menyebabkan keberagaman rekomendasi dari beberapa restoran yang diberikan rating oleh user lain.


