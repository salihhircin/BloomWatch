import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulated NDVI time series (1 year - monthly)
months = np.arange(1, 13)
ndvi_values = 0.2 + 0.4 * np.exp(-((months - 5)**2) / 10) + np.random.normal(0, 0.02, 12)

# 2. Detect bloom start (largest NDVI increase)
ndvi_diff = np.diff(ndvi_values)
bloom_start_month = np.argmax(ndvi_diff) + 1

# 3. DataFrame for clarity
data = pd.DataFrame({
    "Month": months,
    "NDVI": ndvi_values.round(3)
})

# 4. Plot NDVI pattern
plt.figure(figsize=(8, 5))
plt.plot(data["Month"], data["NDVI"], marker='o', linewidth=2)
plt.title("🌸 BloomWatch NDVI Simulation")
plt.xlabel("Month")
plt.ylabel("NDVI (Normalized Difference Vegetation Index)")
plt.grid(True)

# 5. Highlight bloom onset
plt.axvline(bloom_start_month, color='pink', linestyle='--', label=f'Estimated Bloom Start: Month {bloom_start_month}')
plt.legend()

# 6. Output data and plot
print(data)
print(f"\n🌼 Estimated flowering begins around month {bloom_start_month}.\n")
plt.show()
