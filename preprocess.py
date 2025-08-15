import pandas as pd
from sklearn.preprocessing import LabelEncoder

# LabelEncoder'lar (model eğitiminde kullandığın sıra ile)
cut_encoder = LabelEncoder().fit(["Fair", "Good", "Very Good", "Premium", "Ideal"])
color_encoder = LabelEncoder().fit(["J", "I", "H", "G", "F", "E", "D"])
clarity_encoder = LabelEncoder().fit(["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    """Kullanıcıdan gelen veriyi modele uygun hale getirir"""
    df["cut"] = cut_encoder.transform(df["cut"])
    df["color"] = color_encoder.transform(df["color"])
    df["clarity"] = clarity_encoder.transform(df["clarity"])
    return df

