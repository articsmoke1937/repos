import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hvplot.pandas

from sklearn.datasets import load_wine

wine = load_wine()

print("Feature Names : ", wine.feature_names)
print("\nTarget Names : ", wine.target_names)

wine_df = pd.DataFrame(wine.data, columns = wine.feature_names)
wine_df["Target"] = wine.target
wine_df["Target"] = ["Class_1" if typ==0 else "Class_2" if typ==1 else "Class_3"  for typ in wine_df["Target"]]

print("\nDataset Size : ", wine_df.shape)

wine_df.head()

with plt.style.context(("seaborn", "ggplot")):
    wine_df.plot(
                 x="alcohol",
                 y="malic_acid",
                 kind="scatter",
                 s=100, alpha=0.7,
                 title="Alcohol vs Malic Acid Scatter Chart")

scat1 = wine_df.hvplot(
    x="alcohol",
    y="malic_acid",
    kind="scatter",
    size=70,
    alpha=0.7,
    title="Alcohol vs Malic Acid Scatter Chart")

scat1