from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
from utils import process_pdf, get_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    soru: str
    sohbet_gecmisi: List[List[str]]

@app.post("/yukle")
async def pdf_yukle(dosya: UploadFile = File(...)):
    if not dosya.filename.endswith(".pdf"):
        raise HTTPException(400, "Sadece PDF dosyaları kabul edilir.")
    
    try:
        icerik = await dosya.read()
        vektor_deposu = process_pdf(icerik)
        vektor_deposu.save_local("vektor_deposu")
        return {"mesaj": "PDF başarıyla işlendi."}
    except Exception as e:
        raise HTTPException(500, f"PDF işlenirken hata oluştu: {str(e)}")

@app.post("/sohbet")
async def sohbet(mesaj: Message):
    cevap = get_answer(mesaj.soru, mesaj.sohbet_gecmisi)
    return {"cevap": cevap}