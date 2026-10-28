import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1)
swiggy = pd.DataFrame({
    "delivery_time": np.random.randint(15, 60, 200),
    "order_value": np.random.randint(150, 1200, 200)
})

sns.jointplot(x="delivery_time", y="order_value", data=swiggy, kind="hex")
plt.show()