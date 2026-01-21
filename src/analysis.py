import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
import os
from dotenv import load_dotenv
load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="sales_analysis"
)

# --- Query 1: Regional Sales ---
query_region = """
SELECT Region, SUM(Sales) AS total_sales
FROM Orders
GROUP BY Region
ORDER BY total_sales DESC;
"""
df_region = pd.read_sql(query_region, conn)
print("Regional Sales Totals:")
print(df_region)
df_region.to_csv("../data/regional_sales.csv", index=False)   # Save to data/

# --- Query 2: Top Products ---
query_products = """
SELECT Product_Name, SUM(Sales) AS total_sales
FROM Orders
GROUP BY Product_Name
ORDER BY total_sales DESC
LIMIT 10;
"""
df_products = pd.read_sql(query_products, conn)
print("\nTop 10 Products by Sales:")
print(df_products)
df_products.to_csv("../data/top_products.csv", index=False)   # Save to data/

# --- Query 3: Customer Segments ---
query_segment = """
SELECT Segment, SUM(Sales) AS total_sales
FROM Orders
GROUP BY Segment
ORDER BY total_sales DESC;
"""
df_segment = pd.read_sql(query_segment, conn)
print("\nSales by Customer Segment:")
print(df_segment)
df_segment.to_csv("../data/segments.csv", index=False)        # Save to data/

# --- Visualization: Regional Sales ---
sns.barplot(x="Region", y="total_sales", data=df_region)
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.savefig("../charts/region_sales.png")   # Save chart to charts/
plt.show()

# --- Visualization: Top Products ---
sns.barplot(x="total_sales", y="Product_Name", data=df_products)
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.savefig("../charts/top_products.png")   # Save chart to charts/
plt.show()

# --- Visualization: Customer Segments ---
plt.pie(df_segment["total_sales"], labels=df_segment["Segment"], autopct="%1.1f%%")
plt.title("Sales by Customer Segment")
plt.savefig("../charts/segments.png")       # Save chart to charts/
plt.show()

# Close connection
conn.close()
