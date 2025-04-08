import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file_path = '/droughtseverity.csv'

df = pd.read_csv(file_path)

print(df.columns)
df['MapDate'] = pd.to_datetime(df['MapDate'], format='%Y%m%d')
date = df["MapDate"]

fig, ax = plt.subplots(figsize=(12, 6))

levels = ['D0', 'D1', 'D2', 'D3', 'D4']
colors = ['#ffffb2', '#fecc5c', '#fd8d3c', '#f03b20', '#bd0026']
for level, color in zip(levels, colors):
    ax.plot(df['MapDate'], df[level], label=level, color=color, linewidth=1.5)
    ax.fill_between(df['MapDate'], df[level], color=color, alpha=0.3)

# Format the x-axis to show month names
ax.xaxis.set_major_locator(mdates.YearLocator())  # One tick per month
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format: Year

plt.xticks(rotation=45)
ax.set_xlabel("Year")
ax.set_ylabel("Percent Area (%)")
plt.title("U.S. Drought Coverage Over Time (D0–D4)")
ax.legend(title="Drought Level")
plt.ylim(0,100)
plt.tight_layout()
plt.show()

# df = df.drop(['MapDate','AreaOfInterest',"ValidStart","ValidEnd","StatisticFormatID"], axis=1)
# import seaborn as sns
# corr = df.corr()
# sns.heatmap(corr,
#             xticklabels=corr.columns.values,
#             yticklabels=corr.columns.values)
# plt.show()

# do this for so cal and more specific regions
# Palm oil nick stuff
