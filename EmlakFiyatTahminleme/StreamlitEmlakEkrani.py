import streamlit as st
import pandas as pd
import joblib

model = joblib.load(r"C:\Users\Ahmet\Desktop\AHMET\Python\StreamlitWorks\EmlakFiyatTahminleme\EmlakTahminModeli.pkl")

st.set_page_config(
    page_title="Emlak Fiyat Tahmini",
    page_icon="🏠"
)
st.title("Emlak Fiyat Tahmin Ekranı")
st.write("Lütfen tahmin yapmak için gerekli değerleri girin:")

# Girdi elementlerinin oluşturulması
Metrekare = float(st.number_input("Metrekare",step=1,min_value=1,help="Konutun büyüklüğünü metrekare cinsinden giriniz.")) # Veri setindeki öz nitelik tipinden dolayı float veri tipine dönüştürüldü
Yatak_Odasi_Sayisi = st.number_input("Yatak Odası Sayısı", min_value=1, max_value=10, step=1,help="Yatak odası sayısını giriniz.")
Banyo_Sayisi = st.number_input("Banyo Sayısı", min_value=1, max_value=5, step=1,help="Banyo sayısını giriniz.")
Kat_Sayisi = st.number_input("Kat Sayısı", min_value=1, max_value=10, step=1,help="Toplam kat sayısını giriniz.")
Insa_Yili = st.number_input("İnşa Yılı", min_value=1900, max_value=2024, step=1,help="Yapı inşa yılınız giriniz.")
Bahcesi_Var_Mi_Text = st.selectbox("Bahçesi Var Mı?", ["Var", "Yok"])
Bahcesi_Var_Mi = 1 if Bahcesi_Var_Mi_Text == "Var" else 0 # Metinsel ifade boolean değere dönüştürüldü
Havuzu_Var_Mi_Text = st.selectbox("Havuzu Var Mı?", ["Var", "Yok"])
Havuzu_Var_Mi = 1 if Havuzu_Var_Mi_Text == "Var" else 0 # Metinsel ifade boolean değere dönüştürüldü
Garaj_Boyutu = st.number_input("Garaj Boyutu", min_value=0, max_value=50, step=1,help="Varsa garaj boyutunu metrekare cinsinden giriniz. Yoksa 0 giriniz.")
Konum_Skoru = float(st.number_input("Konum Skoru", min_value=0.0, max_value=10.0, step=0.1,help="1-10 arasında bir muhit skoru giriniz.")) # Veri setindeki öz nitelik tipinden dolayı float veri tipine dönüştürüldü
Merkeze_Uzaklik_Km = float(st.number_input("Merkeze Uzaklık (km)", min_value=0.0, max_value=150.0, step=0.5,help="Konutun il merkezine uzaklığını kilometre cinsinden giriniz. Konut merkezde ise 0 giriniz.")) # Veri setindeki öz nitelik tipinden dolayı float veri tipine dönüştürüldü

input_data = pd.DataFrame({
    "Metrekare": [Metrekare],
    "Yatak_Odasi_Sayisi": [Yatak_Odasi_Sayisi],
    "Banyo_Sayisi": [Banyo_Sayisi],
    "Kat_Sayisi": [Kat_Sayisi],
    "Insa_Yili": [Insa_Yili],
    "Bahcesi_Var_Mi": [Bahcesi_Var_Mi],
    "Havuzu_Var_Mi": [Havuzu_Var_Mi],
    "Garaj_Boyutu": [Garaj_Boyutu],
    "Konum_Skoru": [Konum_Skoru],
    "Merkeze_Uzaklik_Km": [Merkeze_Uzaklik_Km],
})

if st.button("Fiyatı Tahmin Et"):
    prediction = model.predict(input_data)
    formatted_price = float(prediction[0])
    st.success(f"Tahmini Fiyat: {formatted_price:,.2f} TL".replace(",", "X").replace(".", ",").replace("X", "."))