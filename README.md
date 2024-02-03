# Age Detection

_Project ini dibuat guna memprediksi kisaran usia berdasarkan bentuk wajah apakah usianya termasuk antara 18-60 tahun dari database **kaggle**._

---

## Assignment Objectives

Project ini dibuat guna mengevaluasi konsep Computer Vision / Natural Language Processing sebagai berikut:

- Mampu memahami konsep Computer Vision/NLP.
- Mampu mempersiapkan data untuk digunakan dalam model Computer Vision/NLP.
- Mampu mengimplementasikan Artificial Neural Network dengan data yang dipilih.
- Mampu menganalisis dan menjelaskan performansi dari arsitektur Artificial Neural Network yang dibuat.

---

## Assignment Instructions

*Project* dikerjakan dalam format *notebook* dan *model deployment* dengan beberapa *kriteria* di bawah ini:

1. Deep Learning framework yang digunakan adalah *TensorFlow*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-val-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.   
   
   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. Pilihlah 1 arsitektur ANN yang terbaik berdasarkan hasil evaluasi sebelumnya.
   
   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set, val-set, ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. **Model Inference harus berada pada notebook yang berbeda dari notebook yang dipakai untuk pembuatan model.**
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

---

## Assignment Submission

- Simpan assignment dengan nama `<nama>.ipynb`.

- Untuk Model Deployment :
  * Folder bernama `deployment` dan berisi semua file yang berkaitan dengan deployment ke folder ini.
  * File bernama `url.txt` berisi URL Dataset dan URL deployment.
  * Contoh bentuk isi repository dengan Model Deployment.
    ```
    ├── deployment/
    │   ├── app.py
    │   ├── eda.py
    │   ├── prediction.py
    │   ├── model.h5
    │   ├── requirements.txt
    ├── <nama>.ipynb
    ├── <nama>_inference.ipynb
    ├── url.txt
    └── README.md
    ```

---
