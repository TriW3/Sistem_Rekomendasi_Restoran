# Sistem_Rekomendasi_Restoran
Aplikasi sistem rekomendasi restoran berbasis user-based collaborative filtering menggunakan pendekatan cosine similarity untuk mencari kemiripan antar user dan metode KNN serta pengujian menggunakan metode RMSE (Root Mean Square Eror) dan MAE (Mean Absolute Eror)<br>
aplikasi ini menggunakan public dataset yang diperoleh dari situs kaggle yang berisikan daftar restoran Mexico dan rating yang diberikan oleh pelanggan terhadap masing masing restoran yang terdaftar. <br>
terdapat 1162 data rating pelanggan dengan skala 0-2 (ratingdataset.csv) dan 113 restoran (restodataset.csv) yang diberikan rating. <br>
setelah dilakukan preprocessing data didapatkan 97 restoran (resto_dataset3) dengan skala rating user yang dirubah menjadi skala 1-3 sejumlah 873 record. <br>
aplikasi yang digunakan untuk membuat sistem rekomendasi ini menggunakan Spyder melalui Anaconda Navigator dan menggunakan library Scikit Surprise. <br>

![Screenshot (891)](https://github.com/TriW3/Sistem_Rekomendasi_Restoran/assets/100888453/548f5a3c-b727-4a38-aa39-d501fc8022bc)<br>
gambar : hasil sistem rekomendasi restoran. <br> 
