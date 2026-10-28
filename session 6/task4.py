import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(3)
zomato = pd.DataFrame({
    "rating": np.round(np.random.uniform(2.5, 5.0, 300), 1),
    "num_reviews": np.random.randint(10, 2000, 300)
})

for kind in ["scatter", "hex", "kde"]:
    sns.jointplot(data=zomato, x="rating", y="num_reviews", kind=kind)
    plt.suptitle(f"Rating vs Reviews ({kind})", y=1.02)
    plt.show()

# Observation :
# Scatter shows every individual restaurant and is good for spotting outliers,
# but points overlap when the data is dense.
# Hexbin counts points per cell, so it shows where most restaurants are concentrated.
# KDE gives a smooth density view of the overall pattern, but hides single points.
# For this data, hexbin helps most because it shows the dense areas clearly
# without the clutter of scatter or the over-smoothing of KDE.