import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("PDF Sohbet Asistanı")

if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []

pdf_dosya = st.file_uploader("PDF Yükle", type="pdf")

if pdf_dosya:
    try:
        response = requests.post(
            f"{BACKEND_URL}/yukle",
            files={"dosya": pdf_dosya}
        )
        response.raise_for_status()
        st.success(response.json().get("mesaj", "PDF başarıyla işlendi."))
    except requests.exceptions.RequestException as e:
        st.error(f"PDF yüklenirken hata oluştu: {str(e)}")
    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")

for mesaj in st.session_state.mesajlar:
    with st.chat_message(mesaj["rol"]):
        st.markdown(mesaj["icerik"])

if soru := st.chat_input("PDF hakkında soru sorun"):
    st.session_state.mesajlar.append({"rol": "kullanıcı", "icerik": soru})

    try:
        sohbet_gecmisi = []
        for i in range(0, len(st.session_state.mesajlar) - 1, 2):
            if st.session_state.mesajlar[i]["rol"] == "kullanıcı" and st.session_state.mesajlar[i + 1]["rol"] == "asistan":
                sohbet_gecmisi.append([
                    st.session_state.mesajlar[i]["icerik"],
                    st.session_state.mesajlar[i + 1]["icerik"]
                ])

        response = requests.post(
            f"{BACKEND_URL}/sohbet",
            json={
                "soru": soru,
                "sohbet_gecmisi": sohbet_gecmisi
            }
        )
        response.raise_for_status()
        cevap = response.json()["cevap"]

        st.session_state.mesajlar.append({"rol": "asistan", "icerik": cevap})

        st.rerun()
    except requests.exceptions.RequestException as e:
        st.error(f"Sohbet sırasında hata oluştu: {str(e)}")