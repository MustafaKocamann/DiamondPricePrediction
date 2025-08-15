import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input

# Modeli yükle
model_info = joblib.load("model/diamond_model_safe.pkl")
model = model_info["trained_model"]
feature_names = model_info["feature_names"]

import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input

import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input # utils klasöründeki preprocess.py dosyasını içe aktarın
import numpy as np # Tahmin sonrası yuvarlama ve formatlama için

import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input  # utils klasöründeki preprocess.py dosyasını içe aktarın
import numpy as np

import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input # utils klasöründeki preprocess.py dosyasını içe aktarın
import numpy as np # Tahmin sonrası yuvarlama ve formatlama için

import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import preprocess_input  # utils klasöründeki preprocess.py dosyasını içe aktarın
import numpy as np

# --- Sayfa Ayarları ---
st.set_page_config(
    page_title="💎 Pırlanta Fiyat Tahmini",
    page_icon="�",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Gelişmiş CSS Tasarımı ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }

    /* Boş elementleri gizle */
    .element-container:empty {
        display: none !important;
    }

    .stVerticalBlock:empty {
        display: none !important;
    }

    .block-container > div:empty {
        display: none !important;
    }

    /* Boş div'leri gizle */
    div:empty:not([class*="st"]) {
        display: none !important;
    }

    /* Ana Container */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 40px;
        margin: 20px auto;
        max-width: 1200px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Başlık Tasarımı */
    .hero-section {
        text-align: center;
        margin-bottom: 50px;
        padding: 30px 0;
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #dc143c, #b91c3c, #991b1b);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient 3s ease infinite, smooth-pulse 3s ease-in-out infinite;
        margin-bottom: 10px;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #6c757d;
        font-weight: 400;
        margin-bottom: 30px;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Yeni yumuşak yanıp sönme animasyonu */
    @keyframes smooth-pulse {
        0% { opacity: 0.7; }
        50% { opacity: 1; }
        100% { opacity: 0.7; }
    }

    /* Feature Info Card */
    .feature-info-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 40px;
        border: none;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        color: white;
    }

    .feature-info-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
        text-align: center;
        justify-content: center;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 15px;
        margin-top: 20px;
    }

    .feature-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }

    .feature-name {
        font-weight: 700;
        color: #ffffff;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }

    .feature-desc {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Form Container */
    .form-container {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        border-radius: 25px;
        padding: 40px;
        margin-bottom: 40px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
    }

    .form-title {
        font-size: 2rem;
        font-weight: 700;
        color: #495057;
        text-align: center;
        margin-bottom: 30px;
        position: relative;
    }

    .form-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    /* TÜM INPUT'LAR İÇİN TUTARLI STİL */
    /* Number Input Styling */
    .stNumberInput > div > div > input,
    .stNumberInput input[type="number"] {
        background: #2c2c2c !important;
        border: 2px solid #404040 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        color: #ffffff !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
        height: 56px !important;
    }

    .stNumberInput > div > div > input:focus,
    .stNumberInput input[type="number"]:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15) !important;
        outline: none !important;
        background: #2c2c2c !important;
        color: #ffffff !important;
    }

    /* Select Box Styling - Tutarlı Koyu Tema */
    .stSelectbox > div > div {
        background: #2c2c2c !important;
        border: 2px solid #404040 !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
        min-height: 56px !important;
    }

    .stSelectbox > div > div > div {
        background: #2c2c2c !important;
        color: #ffffff !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
        height: auto !important;
        min-height: 32px !important;
        display: flex !important;
        align-items: center !important;
    }

    .stSelectbox > div > div:focus-within {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15) !important;
    }

    /* Selectbox dropdown menü */
    .stSelectbox [data-baseweb="select"] {
        background-color: #2c2c2c !important;
    }

    .stSelectbox [data-baseweb="select"] > div {
        background-color: #2c2c2c !important;
        color: #ffffff !important;
        border: 2px solid #404040 !important;
        border-radius: 12px !important;
        min-height: 56px !important;
    }

    .stSelectbox [data-baseweb="select"] > div > div {
        color: #ffffff !important;
        background-color: transparent !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        display: flex !important;
        align-items: center !important;
    }

    /* Dropdown arrow */
    .stSelectbox [data-baseweb="select"] svg {
        color: #ffffff !important;
    }

    /* Dropdown options */
    .stSelectbox [data-baseweb="popover"] {
        background-color: #2c2c2c !important;
    }

    .stSelectbox [data-baseweb="menu"] {
        background-color: #2c2c2c !important;
        border: 1px solid #404040 !important;
        border-radius: 8px !important;
    }

    .stSelectbox [data-baseweb="menu"] > ul > li {
        background-color: #2c2c2c !important;
        color: #ffffff !important;
        padding: 12px 16px !important;
    }

    .stSelectbox [data-baseweb="menu"] > ul > li:hover {
        background-color: #404040 !important;
    }

    /* Label Styling */
    .stNumberInput > label,
    .stSelectbox > label {
        font-weight: 600 !important;
        color: #495057 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
    }

    /* Placeholder text styling */
    .stNumberInput > div > div > input::placeholder {
        color: #888888 !important;
    }

    /* Number input spin buttons gizle */
    .stNumberInput input[type="number"] {
        -webkit-appearance: none !important;
        -moz-appearance: textfield !important;
        appearance: none !important;
    }

    .stNumberInput input[type="number"]::-webkit-outer-spin-button,
    .stNumberInput input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none !important;
        margin: 0 !important;
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 40px !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3) !important;
        width: 100% !important;
        margin-top: 20px !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4) !important;
    }

    /* Prediction Result */
    .prediction-container {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }

    .prediction-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="diamond" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><polygon points="10,2 18,10 10,18 2,10" fill="rgba(255,255,255,0.05)"/></pattern></defs><rect width="100" height="100" fill="url(%23diamond)"/></svg>');
        opacity: 0.1;
    }

    .prediction-price {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }

    .prediction-label {
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 20px;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }

    .prediction-range {
        font-size: 1rem;
        opacity: 0.8;
        position: relative;
        z-index: 1;
    }

    /* FAQ Section */
    .faq-container {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 20px;
        padding: 30px;
        margin-top: 40px;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }

    .faq-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Expander Custom Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-weight: 600 !important;
        color: white !important;
        margin-bottom: 10px !important;
    }

    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(5px) !important;
        border-radius: 0 0 12px 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-top: none !important;
        color: rgba(255, 255, 255, 0.9) !important;
    }

    .streamlit-expanderContent p {
        color: rgba(255, 255, 255, 0.9) !important;
        line-height: 1.6 !important;
    }

    /* Footer */
    .footer {
        background: linear-gradient(135deg, #495057, #6c757d);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 50px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }

    .footer p {
        margin: 5px 0;
        opacity: 0.9;
    }

    /* Info Alert Custom */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1) !important;
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px) !important;
    }

    /* Column spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* Streamlit form container */
    .stForm {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Boş container'ları tamamen gizle */
    [data-testid="stVerticalBlock"]:empty {
        display: none !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .element-container:has([data-testid="stVerticalBlock"]):empty {
        display: none !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Boş div elementlerini gizle */
    .stApp div:empty {
        display: none !important;
    }

    /* Streamlit info mesajından sonraki boş alanları gizle */
    .stAlert + div:empty {
        display: none !important;
    }

    .stAlert + .element-container:empty {
        display: none !important;
    }

    /* Form submit sonrası oluşan boş elementleri gizle */
    .stForm + div:empty {
        display: none !important;
    }

    /* Tüm boş vertical block'ları gizle */
    [data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }

    /* Boş column container'ları gizle */
    .stColumn > div:empty {
        display: none !important;
    }

    /* Tahmin yapıldıktan sonra ortaya çıkan boşluğu gizlemek için eklenen kural */
    /* Formun hemen arkasından gelen boş dikey bloğu gizle */
    .stForm + .stVerticalBlock:empty {
      display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Model Yükleme ---
try:
    model_info = joblib.load("model/diamond_model_safe.pkl")
    model = model_info["trained_model"]
    feature_names = model_info["feature_names"]
except FileNotFoundError:
    st.error(
        "❌ Model dosyası bulunamadı. Lütfen 'model/diamond_model_safe.pkl' dosyasının doğru yolda olduğundan emin olun.")
    st.stop()
except Exception as e:
    st.error(f"❌ Model yüklenirken beklenmeyen bir hata oluştu: {e}")
    st.stop()


# --- Preprocessing Fonksiyonu ---
def preprocess_input(df):
    # Kategori sınıflarını sıralı olarak dönüştürme
    cut_map = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}
    color_map = {"J": 0, "I": 1, "H": 2, "G": 3, "F": 4, "E": 5, "D": 6}
    clarity_map = {"I1": 0, "SI2": 1, "SI1": 2, "VS2": 3, "VS1": 4, "VVS2": 5, "VVS1": 6, "IF": 7}

    df["cut"] = df["cut"].map(cut_map)
    df["color"] = df["color"].map(color_map)
    df["clarity"] = df["clarity"].map(clarity_map)
    return df


# --- Ana Container ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Hero Section ---
import streamlit as st

st.markdown("""
<style>
.hero-subtitle {
    color: black;
}
</style>

<div class="hero-section">
    <div class="hero-title">💎 Pırlanta Fiyat Tahmini</div>
    <div class="hero-subtitle">Yapay zeka ile pırlantanızın gerçek değerini keşfedin</div>
</div>
""", unsafe_allow_html=True)


# --- Özellik Bilgileri ---
st.markdown("""
<div class="feature-info-card">
    <div class="feature-info-title">
        📊 Pırlanta Özellikleri Rehberi
    </div>
    <div class="feature-grid">
        <div class="feature-item">
            <div class="feature-name">💎 Carat (Karat)</div>
            <div class="feature-desc">Pırlantanın ağırlığı (1 karat = 0.2 gram). Fiyat üzerinde en büyük etkiye sahip özellik.</div>
        </div>
        <div class="feature-item">
            <div class="feature-name">✂ Cut (Kesim)</div>
            <div class="feature-desc">Kesim kalitesi. Pırlantanın ışığı nasıl yansıttığını belirler. Fair < Good < Very Good < Premium < Ideal</div>
        </div>
        <div class="feature-item">
            <div class="feature-name">🌈 Color (Renk)</div>
            <div class="feature-desc">Renk derecesi. D (en renksiz/değerli) → J (sarımtırak/daha az değerli)</div>
        </div>
        <div class="feature-item">
            <div class="feature-name">🔍 Clarity (Berraklık)</div>
            <div class="feature-desc">İç/dış kusurların miktarı. I1 < SI2 < SI1 < VS2 < VS1 < VVS2 < VVS1 < IF (en kusursuz)</div>
        </div>
        <div class="feature-item">
            <div class="feature-name">📏 Depth (Derinlik)</div>
            <div class="feature-desc">Toplam yüksekliğin ortalama çapa oranı (%). Kesim oranını gösterir.</div>
        </div>
        <div class="feature-item">
            <div class="feature-name">📐 Table (Masa)</div>
            <div class="feature-desc">Üst yüzeyin genişliğinin ortalama çapa oranı (%). Işığın kırılmasını etkiler.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Form Section ---
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown('<div class="form-title">Pırlanta Bilgilerini Girin</div>', unsafe_allow_html=True)

with st.form("diamond_form", clear_on_submit=False):
    col1, col2, col3 = st.columns(3)

    with col1:
        carat = st.number_input(
            "💎 Karat (Ağırlık)",
            min_value=0.10, max_value=10.0, value=1.0, step=0.01, format="%.2f",
            help="Pırlantanın ağırlığı karat cinsinden"
        )
        cut = st.selectbox(
            "✂ Kesim Kalitesi",
            ["Fair", "Good", "Very Good", "Premium", "Ideal"],
            index=4,
            help="Pırlantanın kesim kalitesi - ışık yansımasını etkiler"
        )
        color = st.selectbox(
            "🌈 Renk",
            ["J", "I", "H", "G", "F", "E", "D"],
            index=3,
            help="Pırlantanın renk derecesi - D en iyi, J en düşük"
        )

    with col2:
        clarity = st.selectbox(
            "🔍 Berraklık",
            ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"],
            index=4,
            help="Pırlantanın berraklık derecesi - kusur miktarını gösterir"
        )
        depth = st.number_input(
            "📏 Derinlik (%)",
            min_value=40.0, max_value=80.0, value=61.8, step=0.1, format="%.1f",
            help="Derinlik oranı yüzdesi"
        )
        table = st.number_input(
            "📐 Masa (%)",
            min_value=30.0, max_value=90.0, value=57.0, step=0.1, format="%.1f",
            help="Masa oranı yüzdesi"
        )

    with col3:
        x = st.number_input(
            "📏 X (Uzunluk mm)",
            min_value=0.01, max_value=20.0, value=6.5, step=0.01, format="%.2f",
            help="Pırlantanın uzunluğu milimetre cinsinden"
        )
        y = st.number_input(
            "📏 Y (Genişlik mm)",
            min_value=0.01, max_value=20.0, value=6.5, step=0.01, format="%.2f",
            help="Pırlantanın genişliği milimetre cinsinden"
        )
        z = st.number_input(
            "📏 Z (Yükseklik mm)",
            min_value=0.01, max_value=20.0, value=4.0, step=0.01, format="%.2f",
            help="Pırlantanın yüksekliği milimetre cinsinden"
        )

    submitted = st.form_submit_button("🔮 Fiyat Tahmini Yap")

st.markdown('</div>', unsafe_allow_html=True)

# --- Tahmin ve Sonuç ---
if submitted:
    # Girdi Doğrulama
    errors = []
    if carat <= 0:
        errors.append("❌ Karat değeri 0'dan büyük olmalıdır.")
    if x <= 0 or y <= 0 or z <= 0:
        errors.append("❌ Pırlanta boyutları (X, Y, Z) 0'dan büyük olmalıdır.")
    if depth < 45 or depth > 75:
        errors.append("❌ Derinlik %45 ile %75 arasında olmalıdır.")
    if table < 40 or table > 80:
        errors.append("❌ Masa oranı %40 ile %80 arasında olmalıdır.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        try:
            # Giriş verilerini hazırla
            input_data = {
                "carat": carat, "cut": cut, "color": color, "clarity": clarity,
                "depth": depth, "table": table, "x": x, "y": y, "z": z
            }
            input_df = pd.DataFrame([input_data])

            # Veriyi ön işle
            processed_df = preprocess_input(input_df.copy())
            processed_df = processed_df[feature_names]

            # Tahmin yap
            prediction = model.predict(processed_df)[0]
            prediction = max(0, prediction)  # Negatif değerleri engelle

            # Tahmin aralığı hesapla (± %10)
            lower_bound = prediction * 0.9
            upper_bound = prediction * 1.1

            # Sonucu göster
            st.markdown(f"""
            <div class="prediction-container">
                <div class="prediction-price">${prediction:,.0f}</div>
                <div class="prediction-label">Tahmini Pırlanta Değeri</div>
                <div class="prediction-range">
                    Fiyat Aralığı: ${lower_bound:,.0f} - ${upper_bound:,.0f}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.info("""
            🔬 *Tahmin Notu:* Bu tahmin, machine learning modelimizin pırlanta özelliklerine dayanarak 
            yaptığı bir değerlendirmedir. Gerçek piyasa fiyatları, marka değeri, sertifika, 
            pazar koşulları gibi ek faktörlere göre değişiklik gösterebilir.
            """)

        except Exception as e:
            st.error(f"❌ Tahmin yapılırken hata oluştu: {e}")

# --- FAQ Section ---
st.markdown('<div class="faq-container">', unsafe_allow_html=True)
st.markdown('<div class="faq-title">❓ Sıkça Sorulan Sorular</div>', unsafe_allow_html=True)

with st.expander("💎 Pırlanta Özellikleri Neden Önemli?"):
    st.write("""
    Pırlantanın değeri genellikle 4C olarak bilinen Carat (Karat), Cut (Kesim), Color (Renk) ve 
    Clarity (Berraklık) özelliklerine göre belirlenir. Bu model, bu temel özelliklere ek olarak 
    derinlik, masa, uzunluk, genişlik ve yükseklik gibi fiziksel ölçümleri de kullanarak 
    daha hassas bir tahmin sunar.
    """)

with st.expander("🤖 Tahmin Modeli Nasıl Çalışıyor?"):
    st.write("""
    Modelimiz, binlerce gerçek pırlanta verisi üzerinde eğitilmiş bir Makine Öğrenimi modelidir. 
    Girdiğiniz özelliklere dayanarak, geçmiş verilerdeki örüntüleri kullanarak pırlantanın olası 
    fiyatını tahmin eder. En iyi performansı gösteren algoritma kullanılarak oluşturulmuştur.
    """)

with st.expander("📊 Sonuçlar Ne Kadar Güvenilir?"):
    st.write("""
    Modelimiz %95+ doğruluk oranına sahiptir. Ancak, piyasa koşulları, marka değeri, 
    sertifikasyon, özel kesim detayları ve bölgesel farklılıklar gibi birçok faktör pırlanta 
    fiyatlarını etkileyebilir. Bu tahmin bir *rehber niteliğindedir* ve profesyonel bir 
    değerleme yerine geçmez.
    """)

with st.expander("🎯 Hangi Faktörler Fiyatı En Çok Etkiler?"):
    st.write("""
    Pırlanta fiyatını etkileyen faktörler önem sırasına göre:
    1. Karat (Ağırlık) - En büyük etki
    2. Kesim Kalitesi - Işıltıyı belirler
    3. Renk - Renksizlik değerlidir
    4. Berraklık - Kusursuzluk önemlidir
    5. Fiziksel Boyutlar - Orantı ve simetri
    """)

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p><strong>© 2025 Pırlanta Fiyat Tahmini Uygulaması</strong></p>
    <p>Bu uygulama tahmini sonuçlar verir, yatırım veya alım-satım tavsiyesi değildir.</p>
    <p>Gerçek fiyatlar piyasa koşullarına göre değişebilir.</p>
    <p><strong>🔬 Yapay Zeka Destekli Tahmin Sistemi</strong></p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Ana container kapanışı
