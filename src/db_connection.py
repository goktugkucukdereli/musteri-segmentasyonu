import psycopg2
from config import DB_CONFIG

def get_db_connection():
    """
    PostgreSQL veritabanı bağlantısı döner.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Veritabanına başarıyla bağlanıldı!")
        return conn
    except Exception as e:
        print(f"Veritabanına bağlanırken bir hata oluştu: {e}")
        return None
