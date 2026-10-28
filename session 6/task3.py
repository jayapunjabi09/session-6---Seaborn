import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(2)
likes = np.random.randint(100, 5000, 100)
insta = pd.DataFrame({
    "likes": likes,
    "comments": (likes * np.random.uniform(0.02, 0.08, 100)).astype(int)
})

sns.jointplot(data=insta, x="likes", y="comments", kind="kde")
plt.show()