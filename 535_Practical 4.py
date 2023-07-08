import numpy as np
import pandas as pd
import itertools
data = pd.read_csv("C:\\Users\\Admin\\Download\\535_Ass4Dataset")
df = pd.DataFrame(data)
print(df)
# Best month for sales and the earnings
best_month=total_sales_month.idxmax()
earnings_best_month=total_sales_month.max()
print("\nBest month for sales:", best_month)
print("Earnings in the best month:", earnings_best_month)

# Product that sold the most
best_selling_product = total_sales_grain.idxmax()
print("\nProduct that sold the most:", best_selling_product)
# City that sold the most products
best_selling_city = total_sales_city.idxmax()
print("\nCity that sold the most products:", best_selling_city)
# Products that are most often sold together
product_combinations = data.groupby('City')['GrainName'].apply(lambda
x: list(itertools.combinations(x, 2)))
# Count the frequency of product combinations
product_combinations_count = pd.Series(list(itertools.chain(*product_combinations))).value_counts()
# Get the most frequently sold product combinations
most_sold_combinations = product_combinations_count.head(5) 
# You can change the number as desired
print("\nProducts most often sold together:")
for combination, count in most_sold_combinations.items():
  print(combination, ": Sold together", count, "times")
import numpy as np
import pandas as pd
data = pd.read_csv("C:\\Users\\Admin\\Download\\535_Ass4Dataset")
df = pd.DataFrame(data)
print(df)
# 1 Total sales for each grain
total_sales_grain = data.groupby('GrainName')['Sales'].sum()
print("Total Sales for each grain:\n", total_sales_grain)
# 2 Total sales for each state
total_sales_state = data.groupby('State')['Sales'].sum()
print("\nTotal Sales for each state:\n", total_sales_state)
# 3 Total sales for each city
total_sales_city = data.groupby('City')['Sales'].sum()
print("\nTotal Sales for each city:\n", total_sales_city)
# 4 Total sales for each month
total_sales_month = data.groupby('Months')['Sales'].sum()
print("\nTotal Sales for each month:\n", total_sales_month)
# 5 Total sales for each year
total_sales_year = data.groupby('Year')['Sales'].sum()
print("\nTotal Sales for each year:\n", total_sales_year)
# 6 Total sales for each grain in a specific month
month = 'JAN' # Replace with the desired month
grain_sales_month = data[data['Months'] == 
month].groupby('GrainName')['Sales'].sum()
print("\nTotal Sales for each grain in", month, ":\n", 
grain_sales_month)
# 7 Total sales for each grain in a specific city
city = 'Nagpur' # Replace with the desired city
grain_sales_city = data[data['City'] ==
city].groupby('GrainName')['Sales'].sum()
print("\nTotal Sales for each grain in", city, ":\n", grain_sales_city)
#8 Total sales for each grain in a specific state
state = 'Maharashtra' # Replace with the desired state
grain_sales_state = data[data['State'] == 
state].groupby('GrainName')['Sales'].sum()
print("\nTotal Sales for each grain in", state, ":\n", 
grain_sales_state)
# 9 Total sales for each grain in a specific year
year = 2023 # Replace with the desired year
grain_sales_year = data[data['Year'] == 
year].groupby('GrainName')['Sales'].sum()
print("\nTotal Sales for each grain in", year, ":\n", grain_sales_year)
#10 Total sales for a specific grain in a specific month and city
grain = 'Ragi' # Replace with the desired grain
city = 'Nagpur' # Replace with the desired city
month = 'JAN' # Replace with the desired month
grain_sales = data[(data['GrainName'] == grain) & (data['City'] == city) & (data['Months'] == month)]['Sales'].sum()
print("\nTotal Sales for", grain, "in", city, "during", month, ":\n",grain_sales)