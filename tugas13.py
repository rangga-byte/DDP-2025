import streamlit as st
import math

# halaman utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.header('Ini Buatan Anak SI')

menu = st.sidebar.selectbox('Menu', ['luas persegi', 'luas segitiga', 'luas lingkaran'])

if menu == 'luas persegi':
    st.write('[halaman ini untuk menghitung luas persegi]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='gambar persegi')
    def luasPersegi(a):
        return a*a
    sisi = st.number_input('Silahkan Masukkan Sisi', min_value=0)

    if st.button('hitung'):
        luas = luasPersegi(sisi)
        st.success(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write('halaman ini untuk menghitung luas segitiga')
    st.image('https://fti.ars.ac.id/img-blog/cara-mengitung-luas-segitiga-dengan-bahasa-pemograman-c', caption='gambar segitiga')
    alas=st.number_input('Silahkan Masukkan Alas', min_value=0)
    tinggi=st.number_input('Silahkan Masukkan Tinggi', min_value=0)
    
    if st.button('Hitung'):
        luas=(alas*tinggi)/2
        st.success(f'Luas Segitiga Adalah {luas}')

elif menu=='luas lingkaran':
    st.write('halaman ini untuk menghitung luas lingkaran')
    st.image('https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253bd91b52f8-rumus-luas-lingkaran_665_374.jpg', caption='gambar lingkaran')
    r=st.number_input('Silahkan Masukkan Jari-Jari', min_value=0)

    if st.button('Hitung'):
        luas=math.pi*r*r
        st.success(f'Luas lingkaran adalah {luas:2f}')