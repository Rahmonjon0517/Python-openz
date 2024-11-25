import pandas as pd  
data = {  
    'Ism': ['Ali', 'Vali', 'Sardor'],  
    'Yoshi': [25, 30, 22],  
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro']  
}  
df = pd.DataFrame(data)  
print(df)  
young_people = df[df['Yoshi'] < 30]  
print("30 yoshdan kichiklar:\n", young_people)  

 
df['Yoshi'] += 1   
print("Yangilangan DataFrame:\n", df)  
df.to_csv('data.csv', index=False)
