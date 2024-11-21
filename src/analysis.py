import pandas as pd
from db_connection import get_db_connection
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def fetch_data():
    """
    Veritabanından verileri çeker.
    """
    conn = get_db_connection()
    if conn is None:
        return None

    query = "SELECT id, ozellik1, ozellik2 FROM musteriler"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def perform_clustering(data, n_clusters=3):
    """
    Veriyi ölçekleyerek K-Means kümeleme algoritmasını uygular.
    """
    features = data[["ozellik1", "ozellik2"]]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    data["kume"] = clusters
    return data

def save_clusters_to_db(data):
    """
    Kümeleme sonuçlarını veritabanına kaydeder.
    """
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    for _, row in data.iterrows():
        cursor.execute(
            "UPDATE musteriler SET kume = %s WHERE id = %s",
            (int(row["kume"]), int(row["id"]))
        )
    
    conn.commit()
    cursor.close()
    conn.close()

def analyze_clusters(data):
    """
    Küme bazında özet istatistikleri hesaplar ve kaydeder.
    """
    cluster_summary = data.groupby('kume').agg({
        'ozellik1': ['mean', 'std', 'min', 'max'],
        'ozellik2': ['mean', 'std', 'min', 'max']
    })
    cluster_summary.to_csv("cluster_analysis_report.csv", index=False)
    print("Küme analiz raporu kaydedildi!")

if __name__ == "__main__":
    data = fetch_data()
    if data is not None:
        clustered_data = perform_clustering(data)
        save_clusters_to_db(clustered_data)
        analyze_clusters(clustered_data)
