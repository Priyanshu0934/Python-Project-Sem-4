import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#                                                   ETA

data=pd.read_excel(r"C:\Users\Priyanshu\Desktop\Python\PROJECTTT\mk.xlsx");

# print(data.head()) 
# print()
# print("Shape : ",data.shape) 
# print()

# print("Info :")
# data.info()   

# print("Descriptive Statistics",data.describe()) 
# print()

# print("Missing values in each column:\n", data.isnull().sum())
# print()

# print("Number of duplicate rows:", data.duplicated().sum())
# print()

# # droping cols with missign value
# data = data.dropna(subset=["Income"]) 
# print("Covariance:\n",data.iloc[:,8:27].cov())

# cor=data.iloc[:,8:27].corr();
# plt.figure(figsize=(16,12))
# sns.heatmap(cor,annot=True) #annot give corr values in each checkbox
# plt.title("heatmap")
# plt.show()





#                                                             Objective 1 

# Find and profile top-spending customer across different product categories to prioritize in loyalty or VIP programs


# prod_cat = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

# # Loop through each product type
# for product in prod_cat:
#     sorted_data = data.sort_values(by=product, ascending=False)
#     top_buyer = sorted_data.iloc[0]
#     print(f"\n Selected customer for VIP Voucher in category of {product[3:]} is with customer Id {top_buyer["ID"]} and amount spend: {top_buyer[product]}")

# max_amt = data[prod_cat].max()  # max for top customer spend

# # Plot
# plt.figure(figsize=(8, 6))
# sns.barplot(x=max_amt.index.str[3:], y=max_amt.values)
# plt.title("Top Amount Spend in Each Product Category")
# plt.xlabel("Product Category")
# plt.ylabel("Amount Spent")
# plt.show()





#                                                Objective 2

# Predict which customers are likely to become inactive based on recency, frequency of purchases, and web visits. 


# data["total_purchase"] = (data["NumWebPurchases"] + data["NumCatalogPurchases"] + data["NumStorePurchases"])


# high_recency = data["Recency"] >= data["Recency"].quantile(0.70)
# low_webvisit = data["NumWebVisitsMonth"] <= data["NumWebVisitsMonth"].quantile(0.30)
# low_Tpurchase = data["total_purchase"] <= data["total_purchase"].quantile(0.30)


# data["tobe_inactive"] = high_recency & low_webvisit & low_Tpurchase

# inactive = data["tobe_inactive"].sum()
# active = len(data) - inactive

# print("Number of people that are likely to become inactive are :",inactive)

# plt.figure(figsize=(6, 6))
# plt.pie(
#     [inactive, active],
#     labels=["Likely Inactive", "Active"],
#     autopct="%1.1f%%",
#     colors=["lightblue", "teal"],
#     startangle=90
# )
# plt.title("Customer Activity Status")
# plt.show()



#                                                  Objective 3
# Determine customer preferences for product types (e.g., wine vs. meat) across different age groups. 


# from datetime import datetime
# current_year = datetime.now().year
# data["Age"] = current_year - data["Year_Birth"]

# bins = [20, 30,  40,  50, 60, 70, 100]
# labels = ['20-30','31-40', '41-50', '51-60', '61-70', '70+']

# data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)


# avg_spend = data.groupby("AgeGroup")[["MntFruits", "MntSweetProducts", "MntGoldProds"]].mean()

# plt.figure(figsize=(12, 6))
# plt.plot(avg_spend.index, avg_spend["MntFruits"], marker='o', label="Fruit Spend", color='green')
# plt.plot(avg_spend.index, avg_spend["MntSweetProducts"], marker='o', label="Sweet Spend", color='orange')
# plt.plot(avg_spend.index, avg_spend["MntGoldProds"], marker='o', label="Gold Spend", color='purple')

# plt.title("Average Spending by Different Age Grops")
# plt.xlabel("Age Group")
# plt.ylabel("Average Amount Spent")
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()
# print("Conclusion : By observing the graph we can conclude that young customers are more inclined toward sweets but customers of age around 40 invest more on gold and fruits. We can also( for customer of age above 50) see as age increases,sales for all three item also increases")



#                                                        Objective 4

# Compare customers who buy via web, store, and catalog channels.

# cols = ["NumWebPurchases", "NumStorePurchases", "NumCatalogPurchases"]
# source = ["Website", "Store", "Catalog"]

# total_purchases = data[cols].sum()

# plt.figure(figsize=(8, 5))
# sns.barplot(x=source, y=total_purchases.values, palette="Set2")
# plt.title("Total Purchases by different Source")
# plt.ylabel("Total Number of Purchases")
# plt.xlabel("Sources of shopping ")
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()
# print("Conclusion: From the graph we can see that most sales are done through stores while least from catalog. Sales from store are approximately twice of sales from catalog. So company should focus more on advertising more so that sales from website and catalog channels can increase.")




#                                      Objective 5
# Group customers by their Dt_Customer enrollment date to see how newer vs. older customers behave differently.


data["en_year"] = data["Dt_Customer"].dt.year
data["CustomerType"] = data["en_year"].apply(lambda x: "Old" if x < 2013 else "New")

cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntGoldProds',"MntSweetProducts"]

total_spend_type = data.groupby("CustomerType")[cols].sum()


total_spend_type.plot(kind="bar",stacked=True, figsize=(8, 5), colormap="Set2")
plt.title("Total Product Spending by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Amount Spent")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("Conclusion: By observing the graph we can say that almost all new customer are spending twice of old customers. So we can say that ratio of spending on differnet products is mostly same for both new and old customer but there is slighty more increase in fruits and meat products")

