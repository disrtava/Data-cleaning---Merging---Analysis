import pandas as pd

df = pd.read_csv('stars.csv')

df = df[df['mass'].notna()]
df = df[df['radius'].notna()]

df['mass'] = df['mass'].astype(float)
df['radius'] = df['radius'].astype(float)

df['radius'] = df['radius'] * 0.102763
df['mass'] = df['mass'] * 0.000954588
    
df_brightest = pd.read_csv('bright_stars.csv')

df_merged = pd.merge(df, df_brightest)


df_merged.to_csv('merged_stars.csv', index=False)
    
