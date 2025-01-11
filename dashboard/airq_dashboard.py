# Importing lib and package needed
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Layout Setting
tab1, tab2, tab3 = st.tabs(['Pendahuluan', 'Q1', 'Q2'])

# Main Page Setting
st.title('Proyek Analisis Data: Air Quality Dataset')
st.subheader('Shafira Nurrusyifa | shafiraenn')

# Tab 1: Intros
with tab1:
  st.header('Pendahuluan')
  st.subheader('Latar Belakang')
  st.text('Pada tahun 2013, penurunan kualitas udara di Beijing pernah mencapai \"Red Alert\" sebuah kondisi polusi serius dalam 3 hari berturut-turut, yang akhirnya memicu pemerintah untuk mengambil \"Heavy Air Pollution Contingency Plan\". Proyek analisis data kali ini, akan mengevaluasi keberhasilan \"5-year-action-plan\" pemerintah Munisipalitas Beijing, serta keperluan peringatan dini berdasarkan kondisi cuaca tertentu.')
  st.subheader('Pertanyaan')
  st.text('Pertanyaan 1: Bagaimana tren tahunan konsentrasi polutan di Beijing?')
  st.text('Pertanyaan 2: Bagaimana tingkat korelasi antara faktor meteorologi dengan konsentrasi polutan?')

# Data Loading
# Area dataframe
tiantan_df = pd.read_csv('dashboard/Tiantan.csv')
wanliu_df = pd.read_csv('dashboard/Wanliu.csv')
changping_df = pd.read_csv('dashboard/Changping.csv')
huairou_df = pd.read_csv('dashboard/Huairou.csv')

dataframes = [tiantan_df, wanliu_df, changping_df, huairou_df]

# Yearly area dataframe
tiantan_yearly_df = pd.read_csv('dashboard/yearly_Tiantan.csv')
wanliu_yearly_df = pd.read_csv('dashboard/yearly_Wanliu.csv')
changping_yearly_df = pd.read_csv('dashboard/yearly_Changping.csv')
huairou_yearly_df = pd.read_csv('dashboard/yearly_Huairou.csv')

yearly_df = [tiantan_yearly_df, wanliu_yearly_df, changping_yearly_df, huairou_yearly_df]

# Features
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
weathers = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

# color configuration
colors = {'CO': 'red', 'SO2': 'purple', 'O3': 'blue', 'PM2.5': 'yellow', 'PM10': 'darkorange', 'NO2': 'green'}

# Tab 2: Question 1
with tab2:
  st.header('Tren Tahunan Konsentrasi Polutan di Beijing')

  st.text('Terjadi sedikit kenaikan di tahun 2014 pada setiap polutan di setiap area administratif, kemudian konsentrasi polutan terus menurun sampai 2016 dan kembali naik di tahun 2017 (kecuali pada O3). Hal ini dikarenakan data yang terekam pada dataset di tahun 2017 merupakan periode paling tercemar di setiap tahun akibat penggunaan pemanas, serta persiapan produksi untuk Tahun Baru China.')

  fig, axes = plt.subplots(2, 2, figsize=(15, 10), sharex=True)
  axes = axes.flatten()

  for ax, df, station in zip(axes, yearly_df, [ 'Tiantan', 'Wanliu', 'Changping', 'Huairou']):
    for pollutant in pollutants:
        ax.plot(df['year'], df[pollutant], label=pollutant, color=colors[pollutant])

    ax.set_title(f'{station} - Yearly Air Pollution Levels', fontsize=12)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Pollutant Concentration (µg/m³)', fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.1)

  plt.tight_layout()
  st.pyplot(fig)

# Tab 3: Question 3
with tab3:
  st.header('Korelasi Antara Faktor Meteorologi dengan Konsentrasi Polutan')

  st.text('Koefisien korelasi antara faktor meteorologi dengan konsentrasi polutan menunjukkan korelasi yang rendah - sedang, sehingga usaha untuk sistem peringatan dini lebih baik dialihkan untuk sesuatu yang lebih mendesak (contoh: penggunaan dan penyediaan sumber daya dan sarana prasaana yang lebih berkelanjutan).')

  fig, axes = plt.subplots(2, 2, figsize=(10, 10))
  axes = axes.flatten()

  for ax, dataframe, station in zip(axes, dataframes, ['Tiantan', 'Wanliu', 'Changping', 'Huairou']):
    correlation_matrix = pd.DataFrame(index=pollutants, columns=weathers)
    for pollutant in pollutants:
      for weather in weathers:
        correlation_matrix.loc[pollutant, weather] = dataframe[pollutant].corr(dataframe[weather])

    correlation_matrix = correlation_matrix.astype(float)

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True, ax=ax)
    ax.set_title(f'Correlation Matrix for {station}', fontsize=12)
    ax.set_xlabel('Weather Features', fontsize=10)
    ax.set_ylabel('Pollutants', fontsize=10)

  plt.tight_layout()
  st.pyplot(fig)
