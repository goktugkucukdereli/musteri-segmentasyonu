# Müşteri Segmentasyonu Projesi

Bu proje, müşteri verilerini kullanarak K-Means kümeleme algoritmasıyla segmentasyon yapmayı amaçlamaktadır. Python, PostgreSQL ve Tableau gibi araçlar kullanılarak veri analizi ve görselleştirme gerçekleştirilmiştir.

---

## 📋 Projenin İçeriği

1. **Veri Üretimi ve İşleme**
    - Sahte veri oluşturmak için Python'da `make_blobs` kullanıldı.
    - PostgreSQL veritabanında veriler depolandı.

2. **Kümeleme Analizi**
    - K-Means algoritması ile veriler 3 kümeye ayrıldı.
    - Küme bazında özet istatistikler hesaplandı.

3. **Aykırı Değer Analizi**
    - Python ile `Box Plot` kullanılarak aykırı değerler analiz edildi.

4. **Görselleştirme**
    - Tableau kullanılarak küme boyutları ve dağılımı görselleştirildi.

---

## 🛠 Kullanılan Teknolojiler

- **Python**: Veri analizi ve kümeleme işlemleri.
- **PostgreSQL**: Veri depolama ve sorgulama.
- **Tableau**: Veri görselleştirme.
- **Kütüphaneler**:
    - pandas
    - numpy
    - scikit-learn
    - seaborn
    - matplotlib
    - psycopg2

---

## 🚀 Projenin Çalıştırılması

### Gereksinimler
- Python 3.8+
- PostgreSQL
- Tableau Desktop veya Tableau Public

### Kurulum
1. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. PostgreSQL veritabanını başlatın ve `data/setup.sql` dosyasını çalıştırın.

3. Veri oluşturmak ve PostgreSQL'e yüklemek için:
    ```bash
    python3 src/main.py
    ```

4. Tableau ile görselleştirme için:
    - `cluster_analysis_report.csv` ve `cluster_sizes.csv` dosyalarını Tableau'ya yükleyin.
    - Görselleştirmeleri oluşturun.

---

## 📊 Önemli Analizler

1. **Küme Dağılımı**:
    - `ozellik1` ve `ozellik2` değerlerinin küme bazlı dağılımını scatter plot ile görselleştirdik.

2. **Küme Boyutları**:
    - Her kümenin müşteri sayısını bar chart ile görselleştirdik.

3. **Aykırı Değer Analizi**:
    - Box Plot kullanarak aykırı değerleri inceledik.

---

## 📂 Proje Yapısı

```plaintext
musteri_segmentasyonu/
│
├── data/
│   └── setup.sql          # Veritabanı tabloları için SQL komutları
│
├── src/
│   ├── main.py            # Ana çalışma dosyası
│   ├── cluster_analysis.py
│   ├── csv_to_db.py
│   ├── db_connection.py   # PostgreSQL bağlantısı
│   ├── db_initializer.py  # Veritabanı başlatma
│   ├── data_generator.py  # Veri üretme ve işleme
│   ├── analysis.py        # Analiz ve modelleme
│   └── visualization.py   # Görselleştirme
│
├── cluster_analysis_report.csv
├── cluster_sizes.csv
├── requirements.txt       # Gerekli Python paketleri
└── README.md              # Proje açıklaması
