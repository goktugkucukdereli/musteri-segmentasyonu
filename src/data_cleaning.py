import pandas as pd
from db_connection import get_db_connection

def load_data():
    """
    Veritabanından musteriler tablosundaki verileri yükler.
    """
    conn = get_db_connection()
    query = "SELECT * FROM musteriler;"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def clean_data(data):
    """
    Veriyi temizler:
    - Eksik verileri kontrol eder ve temizler.
    - Aykırı değerleri belirler ve temizler.
    - Veri türlerini kontrol eder ve dönüştürür.
    """
    print("Eksik verileri kontrol ediliyor...")
    print(data.isnull().sum())

    # Eksik değerleri temizleme (örneğin, NaN değerleri kaldırma)
    data = data.dropna()

    # Veri türlerini kontrol etme
    print("Veri türleri:")
    print(data.dtypes)

    # Aykırı değer kontrolü
    print("Aykırı değerler kontrol ediliyor...")
    print(data.describe())

    # Örnek: Eğer bir filtreleme yapmak isterseniz (örneğin, ozellik1 için bir alt/üst sınır)
    data = data[(data['ozellik1'] > -10) & (data['ozellik1'] < 10)]

    return data

if __name__ == "__main__":
    print("Veri yükleniyor...")
    data = load_data()
    print("Veri temizleniyor...")
    cleaned_data = clean_data(data)
    print("Temizlenmiş veri:")
    print(cleaned_data.head())
