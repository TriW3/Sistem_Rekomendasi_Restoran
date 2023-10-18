# Sistem_Rekomendasi_Restoran
Aplikasi sistem rekomendasi restoran berbasis user-based collaborative filtering (UBCF) menggunakan pendekatan cosine similarity untuk mencari kemiripan antar user dan metode KNN serta pengujian menggunakan metode RMSE (Root Mean Square Eror) dan MAE (Mean Absolute Eror)<br>
aplikasi ini menggunakan public dataset yang diperoleh dari situs kaggle yang berisikan daftar restoran Mexico dan rating yang diberikan oleh pelanggan terhadap masing masing restoran yang terdaftar. <br>
terdapat 1162 data rating pelanggan dengan skala 0-2 (ratingdataset.csv) dan 113 restoran (restodataset.csv) yang diberikan rating. <br>
setelah dilakukan preprocessing data didapatkan 97 restoran (resto_dataset3) dengan skala rating user yang dirubah menjadi skala 1-3 sejumlah 873 record. <br>
aplikasi yang digunakan untuk membuat sistem rekomendasi ini menggunakan Spyder melalui Anaconda Navigator dan menggunakan library Scikit Surprise. <br>

![Screenshot (891)](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/548f5a3c-b727-4a38-aa39-d501fc8022bc)<br>
gambar : hasil sistem rekomendasi restoran. <br> 
## cleaning data : <br> 
proses preprocessing dilakukan untuk mengkondisikan data sesuai dengan kebutuhan, pada projek ini dilakukan sebagai berikut: <br> 
1. proses menggabungkan 2 dataset nama restoran dengan prefensi masakannya berpatokan pada ID resto.<br>
   ![merge ](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/f3da0847-0b8e-4031-9134-fc2a871d2c4b)<br>
   
