from db_connection import get_db_connection
from data_generator import generate_and_insert_data
from cluster_analysis import fetch_data, analyze_clusters

def main():
    """
    Projenin ana çalışma dosyası.
    - Veri setini oluştur ve PostgreSQL'e aktar.
    - Veriyi analiz et ve rapor oluştur.
    """
    # Veri setini oluştur ve PostgreSQL'e aktar
    print("Veri seti oluşturuluyor ve PostgreSQL'e aktarılıyor...")
    generate_and_insert_data()
    print("Veri seti başarıyla PostgreSQL'e aktarıldı!")

    # Veriyi çek ve analiz et
    print("Veritabanından veri çekiliyor ve analiz ediliyor...")
    data = fetch_data()
    if data is not None:
        analyze_clusters(data)
        print("Analiz ve raporlama işlemleri başarıyla tamamlandı!")

if __name__ == "__main__":
    main()
