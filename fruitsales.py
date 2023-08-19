# add your code here
# add your code here
import pandas as pd

fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21,34]}, index=['2017 Sales', '2018 Sales'])

with open('fruits.csv', 'w') as csv_file:
    fruit_sales.to_csv(path_or_buf=csv_file)
    