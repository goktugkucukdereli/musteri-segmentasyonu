import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from db_connection import get_db_connection

def plot_box_plots():
    """
    Veritabanındaki ozellik1 ve ozellik2 sütunları için aykırı değerleri analiz eden bir box plot oluşturur.
    """
    try:
        # Veritabanına bağlan
        conn = get_db_connection()
        query = "SELECT ozellik1, ozellik2 FROM musteriler"
        data = pd.read_sql_query(query, conn)
        conn.close()

        # Box plot oluştur
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=data)
        plt.title("Aykırı Değer Analizi (Box Plot)", fontsize=16)
        plt.ylabel("Değerler", fontsize=12)
        plt.xlabel("Özellikler", fontsize=12)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Box plot oluşturulurken bir hata oluştu: {e}")

if __name__ == "__main__":
    plot_box_plots()
