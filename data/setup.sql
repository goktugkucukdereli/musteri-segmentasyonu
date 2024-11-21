-- Veritabanını oluştur
CREATE DATABASE musteri_segmentasyonu;

-- musteri_segmentasyonu veritabanına bağlan
\c musteri_segmentasyonu

-- musteriler tablosunu oluştur
CREATE TABLE musteriler (
    id SERIAL PRIMARY KEY,
    ozellik1 FLOAT,
    ozellik2 FLOAT,
    kume INTEGER
);
