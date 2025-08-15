# 💎 Diamonds Price Prediction

## 🚀 Proje Genel Bakışı
Bu proje, **elmas fiyatlarını tahmin etmek** amacıyla farklı makine öğrenimi algoritmalarını karşılaştırarak en iyi performansı gösteren modeli seçmeyi hedefler.

Kullanılan veri setindeki elmasların **kesim (cut)**, **renk (color)**, **berraklık (clarity)** gibi kategorik özellikleri ile **karat (carat)**, **derinlik (depth)**, **tablo (table)**, **uzunluk (x)**, **genişlik (y)**, **yükseklik (z)** gibi sayısal özellikleri kullanılarak fiyat tahmini yapılır.

Proje, **Streamlit** ile kullanıcı dostu ve etkileşimli bir web uygulaması olarak sunulmuştur.  
Kullanıcı, elmasın özelliklerini girerek tahmini fiyatı anında görebilir.

---

## ✨ Özellikler
- **Ana Sayfa:** Projenin amacı, kullanılan veri seti ve model hakkında genel bilgi.
- **Fiyat Tahmin Aracı:**
  - Kullanıcı, elmasın fiziksel ve kalite özelliklerini girer.
  - Model, eğitilmiş **XGBRegressor** algoritması ile tahmini fiyatı döndürür.
- **Otomatik Ön İşleme:** Kullanıcının girdiği veriler, eğitimde kullanılan aynı veri ön işleme adımlarından geçirilir.
- **Eğitim Sonuçları:** Birden fazla algoritma karşılaştırılmıştır:
  - LinearRegression
  - Lasso
  - DecisionTree
  - RandomForest
  - KNeighbors
  - XGBRegressor
- **En iyi sonuç:** XGBRegressor (R²: **0.9810**)

---

## 🛠️ Kullanılan Teknolojiler
- **Python** – Temel programlama dili
- **Streamlit** – Web arayüzü geliştirme
- **Pandas** – Veri analizi ve manipülasyonu
- **NumPy** – Sayısal hesaplamalar
- **Scikit-learn** – Makine öğrenimi algoritmaları
- **XGBoost** – Yüksek performanslı gradient boosting modeli
- **Joblib** – Modeli güvenli formatta kaydetme ve yükleme

---

## 📊 Veri Seti
Bu projede kullanılan veri seti, elmasların **fiziksel** ve **kalite** özelliklerini içermektedir.  

**Temel sütunlar:**
- `carat` → Elmasın ağırlığı (karat cinsinden)
- `cut` → Kesim kalitesi (Fair, Good, Very Good, Premium, Ideal)
- `color` → Renk skalası (D - en iyi, J - en kötü)
- `clarity` → Berraklık seviyesi (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
- `depth` → Toplam derinlik yüzdesi
- `table` → Tablo genişliği yüzdesi
- `x`, `y`, `z` → Elmasın boyutları (mm)
- `price` → Fiyat (USD)

Veri seti, **kategori kodlama** ve **ölçeklendirme** işlemlerinden geçirilerek modellere uygun hale getirilmiştir.

---

## 🧠 Model Detayları
Model seçim sürecinde test edilen algoritmalar ve performans sonuçları:

| Model            | RMSE      | R²      |
|------------------|-----------|---------|
| LinearRegression | 1383.854  | 0.8783  |
| Lasso            | 1366.991  | 0.8816  |
| DecisionTree     | 736.502   | 0.9650  |
| RandomForest     | 548.844   | 0.9809  |
| KNeighbors       | 816.559   | 0.9578  |
| **XGBRegressor** | **548.347** | **0.9810** |

- **Seçilen Model:** XGBRegressor  
- **Test Setinde R²:** 0.9821  
- **Test Setinde Adjusted R²:** 0.9821  

Model, `model/diamond_model_safe.pkl` dosyasında **Joblib** ile güvenli formatta saklanmaktadır.  
Dosya içeriğinde:
- Model parametreleri
- Eğitilmiş model
- Kullanılan özellik isimleri yer almaktadır.

---

## 🌐 Canlı Uygulama
🔗 **Streamlit Linki:** [https://diamondspricepredictionn.streamlit.app/](https://diamondspricepredictionn.streamlit.app/)

---

## 👤 İletişim

- [LinkedIn - Mustafa Kocaman](https://www.linkedin.com/in/mustafakocamann/)

---

## 📄 Lisans
Bu proje **MIT Lisansı** altında lisanslanmıştır.  

