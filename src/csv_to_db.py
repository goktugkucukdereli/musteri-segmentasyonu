import pandas as pd
from db_connection import get_db_connection

def save_report_to_db(csv_path):
    conn = get_db_connection()
    cursor = conn.cursor()

    print("Veritabanına başarıyla bağlanıldı!")
    
    # CSV dosyasını oku
    data = pd.read_csv(csv_path)
    
    # Sütun adlarını temizle ve kontrol et
    data.columns = data.columns.str.strip()
    print("CSV sütunları:", data.columns.tolist())

    # Yeni bir tablo oluştur
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cluster_report (
        id SERIAL PRIMARY KEY,
        kume INT,
        ozellik1_mean FLOAT,
        ozellik1_std FLOAT,
        ozellik1_min FLOAT,
        ozellik1_max FLOAT,
        ozellik2_mean FLOAT,
        ozellik2_std FLOAT,
        ozellik2_min FLOAT,
        ozellik2_max FLOAT
    )
    """)

    # Verileri tabloya ekle
    for _, row in data.iterrows():
        cursor.execute("""
        INSERT INTO cluster_report (
            kume, ozellik1_mean, ozellik1_std, ozellik1_min, ozellik1_max,
            ozellik2_mean, ozellik2_std, ozellik2_min, ozellik2_max
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            int(row['kume']), 
            float(row['ozellik1_mean']), float(row['ozellik1_std']),
            float(row['ozellik1_min']), float(row['ozellik1_max']),
            float(row['ozellik2_mean']), float(row['ozellik2_std']),
            float(row['ozellik2_min']), float(row['ozellik2_max'])
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("Veriler başarıyla tabloya kaydedildi!")

save_report_to_db('cluster_analysis_report.csv')
