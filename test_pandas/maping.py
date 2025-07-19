import pandas as pd

df = pd.DataFrame({'country': ['Germany', 'Russia', 'Italy']})
print(df)
country_codes = {'Germany': 'DE', 'Russia': 'RU', 'France': 'FR'}

df['code'] = df['country'].map(country_codes)

print(df)