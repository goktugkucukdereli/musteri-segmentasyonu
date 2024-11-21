import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from db_connection import get_db_connection

def fetch_data():
    """
    Veritabanından verileri çeker.
    """
    conn = get_db_connection()
    if conn is None:
        return None

    query = "SELECT ozellik1, ozellik2, kume FROM musteriler"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def plot_clusters(data):
    """
    Veriyi görselleştirir.
    """
    plt.figure(figsize=(10, 7))
    sns.scatterplot(
        data=data,
        x="ozellik1",
        y="ozellik2",
        hue="kume",
        palette="viridis",
        s=100
    )
    plt.title("Kümeleme Analizi Sonuçları")
    plt.xlabel("Özellik 1")
    plt.ylabel("Özellik 2")
    plt.legend(title="Küme")
    plt.show()

if __name__ == "__main__":
    data = fetch_data()
    if data is not None:
        plot_clusters(data)
