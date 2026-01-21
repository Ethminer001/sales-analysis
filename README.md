# 📈 Sales Performance Analysis

End-to-end analysis of company sales data to diagnose a **15% quarterly sales decline** and deliver actionable recommendations.

Built with SQL + Python + Pandas + Seaborn.

## 🎯 Business Problem

Sales dropped ~15% this quarter. Leadership needed answers:

- Which **regions** are underperforming?
- Which **products** are driving or dragging results?
- Which **customer segments** are most impacted?

## 🔍 Key Findings

**Regional Performance**  
- South region declined **23%** — $47K in lost revenue  
- West and East regions remained stable and strong  

![Regional Sales](https://github.com/Ethminer001/sales-analysis/blob/main/charts/region_sales.png?raw=true)

**Top Products**  
- Canon imageCLASS copier leads overall sales volume  
- Binding systems and printers showed the largest declines  

![Top Products](https://github.com/Ethminer001/sales-analysis/blob/main/charts/top_products.png?raw=true)

**Customer Segments**  
- Consumer segment dominates revenue but dropped **18%** in the South  
- This segment drove the majority of the regional revenue loss  

![Customer Segments](https://github.com/Ethminer001/sales-analysis/blob/main/charts/segments.png?raw=true)

## ✅ Recommended Actions

1. **Targeted email campaign** to 340 lapsed South-region customers  
   → Expected lift: **$15K** within 60 days

2. **Bundled promotions** on underperforming categories  
   → Binding systems + printers with discount incentives

3. **Consumer segment retention program** in South region  
   → Recover lost share and stabilize performance

## 📁 Project Structure


```
sales-analysis/
├── README.md
├── data/
│   ├── regional_sales.csv
│   ├── top_products.csv
│   └── segments.csv
├── charts/
│   ├── region_sales.png
│   ├── top_products.png
│   └── segments.png
└── src/
    └── analysis.py          # SQL queries + Pandas + charting

```


## 🛠️ Tech Stack

- **SQL (MySQL)** → Data extraction & aggregation  
- **Python** → Orchestration & automation  
- **Pandas** → Data cleaning & transformation  
- **Matplotlib + Seaborn** → Professional visualizations

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Ethminer001/sales-analysis.git
cd sales-analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn mysql-connector-python

# 3. Run the full analysis
python src/analysis.py
```


This will:Connect to the database
Run SQL queries
Create summary CSVs
Generate all charts in /charts/

 ContactLinkedIn → linkedin.com/in/eriioluwa  
Email → olowu.tayo200@gmail.com  
GitHub → @Ethminer001

 AcknowledgmentsInspired by real-world sales performance diagnostics.
Built as part of my data analytics portfolio.From raw database → SQL insights → Python analysis → clear business recommendations.
