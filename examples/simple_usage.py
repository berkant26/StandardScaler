
from scaler.standard_scaler import MyStandardScaler
import numpy as np

data = [
    [30,60],
    [25,66],
    [20,50],
    [20,60],
    [20,66],


]

scaler = MyStandardScaler()
scaled_data = scaler.fit_transform(data)

print("🔹 Orijinal Veri:")
print(np.array(data))

# Standardize edilmiş veriyi göster
print("\n🔸 Standardize Edilmiş Veri:")
print(scaled_data)

# Hesaplanan ortalama ve standart sapmaları yazdır
print("\n📊 Ortalama (mean):", scaler.mean_)
print("📊 Standart Sapma (std):", scaler.std_)