import pandas as pd 
# Lúc đầu cậu thiếu dòng này, nên nó không import được thưu viện
# bất cứ dùng cái gì đều cần import

df =pd.read_excel('data.xlsx')
# Print() -> sai. Đúng phải là print()
print("Dữ liệu ban đầu:")
print(df)
df['Birthday year'] = 2023 - df['Age'] # df[Age] -> Sai. Đúng là: df['Age']
print("\nDữ liệu sau khi thêm cột mới:")
print(df)
young_people = df[df['Age'] < 30]
print("\nDữ liệu sau khi lọc:")
print(young_people)
df.to_excel('data_moi.xlsx',index=False) #false -> sai. Đúng là: False