import os
import cv2
import glob
import random
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Deteksi Usia - EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run() :
    # Membuat Title
    st.title('Mendeteksi usia pada wajah manusia')

    # Membuat sub Header
    st.subheader('EDA untuk melihat analisis dari suatu foto wajah manusia dan mendeteksi jarak usianya antara 18-60 tahun dari dataset age-detection-human-faces-18-60-years.zip yang diambil dari kaggle')

    # Menambahkan Image
    st.image('https://verihubs.com/wp-content/uploads/2022/09/face-detection-1.jpg', 
             caption='Age_detection')
    
    # Menambahkan Deskripsi
    st.write('Page ini dibuat oleh Jeni :')
    st.write('### Pada halaman ini kita akan melihat beberapa contoh data dari berbagai class usia')

    # Membuat garis lurus 
    st.write('---')

    # create variables for path
    main_path = 'database'

    # train
    train_18to20 =os.path.join(main_path, 'train', '18-20')
    train_21to30 =os.path.join(main_path, 'train', '21-30')
    train_31to40 =os.path.join(main_path, 'train', '31-40')
    train_41to50 =os.path.join(main_path, 'train', '41-50')
    train_51to60 =os.path.join(main_path, 'train', '51-60')

    # Creating dataset train, test, validation
    # function to visualize each class
    def create_dataframe(list_of_images):
        data = []
        for image in list_of_images:
            # Splitting paths using '\\' for Windows paths
            data.append((image, image.split('\\')[-2]))  
        return pd.DataFrame(data, columns=['images', 'label'])

    train_df = create_dataframe(
        glob.glob(os.path.join(train_18to20, '*.jpg'))+
        glob.glob(os.path.join(train_21to30, '*.jpg'))+
        glob.glob(os.path.join(train_31to40, '*.jpg'))+
        glob.glob(os.path.join(train_41to50, '*.jpg'))+
        glob.glob(os.path.join(train_51to60, '*.jpg'))
    )
    train_df = train_df.sample(frac=1, random_state=7).reset_index(drop=True)

    def visualize_samples_by_label(df, label, num_samples=20):
        samples = df[df['label'] == label]['images'].iloc[:num_samples].tolist()
        print(f"Number of samples: {len(samples)}")  # Debug statement

        num_cols = min(num_samples, 5)
        num_rows = (num_samples - 1) // num_cols + 1
        fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(10, 2 * num_rows))
        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if count < len(samples):
                    sample = samples[count]
                    img = Image.open(sample)
                    ax = axes[i, j]
                    ax.imshow(img)
                    ax.axis('off')
                    count += 1
                else:
                    break
        plt.tight_layout()
        st.pyplot(fig)
        

    # visualize 'Bean' class
    st.write(' 1. Usia 18-20')
    visualize_samples_by_label(train_df, '18-20', num_samples=20)
    st.write('**Karakteristik**')
    st.write('wajah terlihat masih muda dan tidak memiliki banyak keriput pada wajahnya')

    st.markdown('----')

    # visualize 'Bitter_Gourd' class
    st.write(' 2. Usia 21-30')
    visualize_samples_by_label(train_df, '21-30', num_samples=20)
    st.write('**Karakteristik**')
    st.write('wajah terlihat sudah dewasa dan mulai memiliki sedikit keriput/garis halus pada wajahnya')

    st.markdown('----')

    # visualize 'Bitter_Gourd' class
    st.write(' 3. Usia 31-40')
    visualize_samples_by_label(train_df, '31-40', num_samples=20)
    st.write('**Karakteristik**')
    st.write('wajah terlihat sangat dewasa dan memiliki keriput/garis halus pada area bawah mata dan garis senyum')

    st.markdown('----')

    # visualize 'Bitter_Gourd' class
    st.write(' 4. Usia 41-50')
    visualize_samples_by_label(train_df, '41-50', num_samples=20)
    st.write('**Karakteristik**')
    st.write('wajah terlihat sedikit menua dan memiliki keriput pada area wajahnya')

    st.markdown('----')

    # visualize 'Bitter_Gourd' class
    st.write(' 5. Usia 51-60')
    visualize_samples_by_label(train_df, '51-60', num_samples=20)
    st.write('**Karakteristik**')
    st.write('wajah terlihat sudah menua dan memiliki banyak keriput pada seluruh area wajahnya')

    st.markdown('----')


if __name__== '__main__':
    run()