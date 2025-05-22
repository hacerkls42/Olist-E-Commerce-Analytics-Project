# utils.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset(path):
    """CSV dosyasını oku ve DataFrame olarak döndür."""
    try:
        df = pd.read_csv(path)
        print(f"'{path}' başarıyla yüklendi. Şekil: {df.shape}")
        return df
    except Exception as e:
        print(f"Dosya yüklenemedi: {e}")
        return None

def check_missing_values(df):
    """Eksik değerleri tablo halinde göster."""
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    return pd.DataFrame({'Eksik Değer Sayısı': missing, 'Yüzde (%)': (missing / len(df) * 100).round(2)})

def plot_correlation(df, figsize=(12, 8)):
    """Korelasyon matrisini çiz."""
    plt.figure(figsize=figsize)
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title("Korelasyon Matrisi")
    plt.show()

def plot_countplot(df, column):
    """Belirli bir sütun için countplot çiz."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"{column} Değerlerinin Dağılımı")
    plt.show()
