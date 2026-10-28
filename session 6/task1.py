import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
sample = pd.DataFrame({
    "rating": np.round(np.random.uniform(3.0, 5.0, 60), 1),
    "price": np.random.randint(500, 5000, 60)
})
sample.to_csv("flipkart_ratings_prices.csv", index=False)

df = pd.read_csv("flipkart_ratings_prices.csv")

sns.jointplot(data=df, x="rating", y="price", kind="scatter")
plt.show()