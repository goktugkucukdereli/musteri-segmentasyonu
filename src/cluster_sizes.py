import pandas as pd
from db_connection import get_db_connection

def cluster_sizes():
    """
    Her kümede kaç veri bulunduğunu hesaplar ve sonuçları bir CSV dosyasına kaydeder.
    """
    try:
        # Veritabanına bağlan
        conn = get_db_connection()
        query = "SELECT kume, COUNT(*) as count FROM musteriler GROUP BY kume"
        cluster_sizes = pd.read_sql_query(query, conn)
        conn.close()

        # Sonuçları ekrana yazdır
        print("Küme Boyutları:")
        print(cluster_sizes)

        # Sonuçları bir CSV dosyasına kaydet
        cluster_sizes.to_csv("cluster_sizes.csv", index=False)
        print("Küme boyutları 'cluster_sizes.csv' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Küme boyutlarını hesaplarken bir hata oluştu: {e}")

if __name__ == "__main__":
    cluster_sizes()
