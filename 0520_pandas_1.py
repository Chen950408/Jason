import pandas as pd


list_data = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(list_data)


index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(list_data, index=index_labels)


stock3 = stock2.to_dict()



stock2.to_csv('0520_stock.csv', header=False)


print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

print(f"Banana 庫存： {stock2['Banana']}")
print()

print("缺失值檢查：")
print(stock2.isna())
print()

print(f"缺失值數量： {stock2.isna().sum()}")