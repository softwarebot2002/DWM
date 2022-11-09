import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv('dwm_dv.csv')

# Scatter plot
plt.scatter(data['Gr Liv Area'], data['SalePrice'])

# Adding Title to the Plot
plt.title('Scatter Plot')

# Setting the X and Y labels
plt.xlabel('Living Area Above Ground')
plt.ylabel('House Price')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# # reading the database
# data = pd.read_csv('dwm_dv.csv')
x=[1,2,3,4,5]
y=[2,3,4,5,6]

# Scatter plot
plt.scatter(x,y)

# Adding Title to the Plot
plt.title('Scatter Plot')

# Setting the X and Y labels
plt.xlabel(x)
plt.ylabel(y)
plt.show()

# Histogram
plt.hist(x)
plt.title('Histogram')
plt.show()