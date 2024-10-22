import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a distplot

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a distplot without the histogram

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


