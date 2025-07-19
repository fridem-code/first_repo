# import pandas as pd

# df = pd.read_excel('Тест_faker.xlsx')

# country_dict = {}

# for index, row in df.iterrows():
#     country = row['country']
#     if country_dict.get(country, False):
#         country_dict[country] += 1
#     else:
#         country_dict[country] = 1

# country_sorted = dict(reversed(sorted(country_dict.items(), key=lambda item:item[1])))
# print('Топ 5 стран:')
# for index, item in enumerate(country_sorted.items()):
#     if index == 5:
#         break
#     print(f"{item[0]} - {item[1]}")

import pandas as pd
from collections import Counter

df = pd.read_excel('Тест_faker.xlsx')

# Считаем количество вхождений каждой страны и берём топ-5
top_countries = df['country'].value_counts().head(5)

print('Топ 5 стран:')
for country, count in top_countries.items():
    print(f"{country} - {count}")

top_5 = Counter(df['country']).most_common(5, n=True)

print(top_5)