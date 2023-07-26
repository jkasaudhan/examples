import sqlite3
import pandas as pd

# connect to the database
con = sqlite3.connect('database.db')

# fetch data from database
df = pd.read_sql_query('SELECT * FROM orders', con)

# close the database connection
con.close()

# calculate sum of order values by customer
df['total_order_value'] = df.groupby('customer_id')['order_value'].apply(sum)

# calculate average order value by customer
df['avg_order_value'] = df.groupby('customer_id')['order_value'].transform('mean')

# replace certain values
df['order_status'] = df['order_status'].map({
    'processing': 'in_progress',
    'shipped': 'delivered',
    'complete': 'finished'
})

# export the dataframe to excel
df.to_excel('output.xlsx')
