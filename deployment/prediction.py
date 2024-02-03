import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

def run() :
    st.subheader('Prediksi Usia')
    st.write('Catatan : Anda hanya dapat memprediksi usia : 18-20, 21-30, 31-40, 41-50, 51-60')
    st.write('')
    model = load_model('best_model.h5')

    uploaded_file = st.file_uploader('Upload sebuah gambar', type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar yang Diunggah', use_column_width=True)

        # Praproses gambar
        resized_image = image.resize((110, 110))  # Ubah ukuran gambar agar sesuai dengan ukuran input model
        normalized_image = np.array(resized_image) / 255.0  # Normalisasikan nilai piksel
        input_image = np.expand_dims(normalized_image, axis=0)  # Tambahkan dimensi ekstra saat model mengharapkan sekumpulan gambar

        # Lakukan klasifikasi gambar
        prediction = model.predict(input_image)
        predicted_class = np.argmax(prediction)

        class_names = ["18-20", "21-30", "31-40", "41-50", "51-60"]
        # Menampilkan label kelas prediksi
        predicted_label = class_names[predicted_class]
        st.write('Dari foto diatas hasil prediksinya adalah :')
        st.write('Prediksi usia sekitar : ', predicted_label)

if __name__=='__main__':
    run()