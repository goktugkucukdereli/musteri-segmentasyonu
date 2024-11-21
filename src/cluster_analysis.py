import pandas as pd
from db_connection import get_db_connection

def fetch_data():
    """
    Veritabanından musteriler tablosundaki verileri çeker ve bir DataFrame döner.
    """
    try:
        conn = get_db_connection()
        if conn is None:
            print("Veritabanı bağlantısı sağlanamadı.")
            return None

        query = "SELECT ozellik1, ozellik2, kume FROM musteriler"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    except Exception as e:
        print(f"Veriyi çekerken bir hata oluştu: {e}")
        return None

def analyze_clusters(df):
    """
    Kümeler için temel istatistikleri hesaplar ve bir CSV dosyasına kaydeder.
    """
    try:
        # Küme bazında istatistikler
        cluster_analysis = df.groupby("kume").agg({
            "ozellik1": ["mean", "std", "min", "max"],
            "ozellik2": ["mean", "std", "min", "max"]
        })

        # Kolon isimlerini düzenle
        cluster_analysis.columns = [
            "_".join(col).strip() for col in cluster_analysis.columns.values
        ]
        cluster_analysis.reset_index(inplace=True)

        # CSV dosyasına kaydet
        cluster_analysis.to_csv("cluster_analysis_report.csv", index=False)
        print("Küme analiz raporu 'cluster_analysis_report.csv' olarak kaydedildi.")
        return cluster_analysis

    except Exception as e:
        print(f"Küme analizi sırasında bir hata oluştu: {e}")
        return None

if __name__ == "__main__":
    # Veriyi çek
    data = fetch_data()
    if data is not None:
        # Kümeleri analiz et
        cluster_summary = analyze_clusters(data)
        if cluster_summary is not None:
            print("Analiz başarıyla tamamlandı!")
            print(cluster_summary)
