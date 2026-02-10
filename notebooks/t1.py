# %%
import numpy as np, pandas as pd

# %%
import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(0)
data = np.random.normal(0, 1, 100)
data = np.append(data, [5, 6, -4])  # Add some outliers

# Create boxplot with outliers in red
plt.boxplot(data, flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'))
plt.title("Boxplot with Outliers in Red")
plt.show()


# %%
import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(0)
data = np.random.normal(0, 1, 100)
data = np.append(data, [5, 6, -4])  # Add some outliers

# Step 1: Identify outliers using IQR
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Step 2: Remove outliers
data_no_outliers = data[(data >= lower_bound) & (data <= upper_bound)]

# Step 3: Plot both boxplots in one subplot
plt.figure(figsize=(4,3))

plt.boxplot([data, data_no_outliers],
            labels=['With Outliers', 'Without Outliers'],
            flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'))

plt.ylabel("Values")
plt.title("Comparison of Boxplots With and Without Outliers")
plt.show()

# %%
