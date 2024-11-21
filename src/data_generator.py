from sklearn.datasets import make_blobs
from db_connection import get_db_connection

def generate_and_insert_data():
    """
    Sahte veri oluşturur ve veritabanına ekler.
    """
    # Sahte veri oluşturma
    data, labels = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)

    # Veritabanına bağlanma
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    # Verileri ekleme
    for i in range(len(data)):
        cursor.execute(
            "INSERT INTO musteriler (ozellik1, ozellik2, kume) VALUES (%s, %s, %s)",
            (float(data[i][0]), float(data[i][1]), int(labels[i]))
        )
    
    conn.commit()
    print("Veriler başarıyla eklendi!")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    generate_and_insert_data()
