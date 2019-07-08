import tushare as ts
from matplotlib import pyplot  as plt
import matplotlib
df = ts.get_hist_data("510590")



x = df.index
y = df[["price_change"]]
print(y)

my_font = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
df = df[["price_change"]]
df = df.sort_values("price_change", ascending = False)

plt.figure(figsize=(20, 8), dpi=80)
#print(df)

