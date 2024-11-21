from db_connection import get_db_connection

def initialize_database():
    conn = None
    cursor = None
    try:
        # Bağlantıyı al
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Veritabanını oluştur (eğer yoksa)
        cursor.execute("CREATE DATABASE musteri_segmentasyonu;")
        print("Veritabanı 'musteri_segmentasyonu' başarıyla oluşturuldu.")
        
        # İlk bağlantıyı kapat ve yeni veritabanına bağlan
        cursor.close()
        conn.close()
        conn = get_db_connection(dbname="musteri_segmentasyonu")
        cursor = conn.cursor()

        # Tabloyu oluştur
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS musteriler (
                id SERIAL PRIMARY KEY,
                ozellik1 FLOAT,
                ozellik2 FLOAT,
                kume INTEGER
            );
        """)
        print("Tablo 'musteriler' başarıyla oluşturuldu.")
        
        # Değişiklikleri kaydet
        conn.commit()

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    finally:
        # Bağlantıyı kapat
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    initialize_database()
