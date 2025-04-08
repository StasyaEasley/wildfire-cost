import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = "/Users/stasyaeasley/Desktop/droughtshapefiles/Historic_Geomac_Perimeters_All_Years_2000_2018.gdb"

layer = "US_HIST_FIRE_PERIMTRS_2000_2018_DD83"
fires = gpd.read_file(path, layer=layer)

fires = fires.to_crs(epsg=3310) # 4269
fires['area_km2'] = fires.geometry.area / 1e6 # find area of polygons in shapefile

def raw_sizes():
    print(fires[['fireyear', 'area_km2']].sort_values(by='area_km2', ascending=False).head(10))

def range_fires():
    # wildfire size range and number of fires in that range
    counts, bin_edges = np.histogram(fires['area_km2'], bins=100)
    for i in range(len(counts)):
        print(f"Size range: {bin_edges[i]:,.2f} – {bin_edges[i+1]:,.2f} km² → {counts[i]} fires")
#disregard these
def size_vs_count():
    sns.histplot(fires['area_km2'], bins=100, log_scale=(False, True), element="bars")
    plt.xlabel("year")
    plt.title("Distribution of Wildfire Sizes (2000–2018)")
    return plt.show()

def year_vs_area():
    sns.boxplot(data=fires, x='fireyear', y='area_km2')
    plt.xlabel("year")
    plt.title("Distribution of Wildfire Sizes by year (2000–2018)")
    return plt.show()

def sizevscost():
    cost_df = pd.read_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv")
    avg_size = fires.groupby('fireyear')['area_km2'].mean().reset_index()
    merged = pd.merge(avg_size, cost_df, left_on='fireyear', right_on='Year', how='inner')
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Average fire size line
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Avg Fire Size (km²)', color='red')
    ax1.plot(merged['fireyear'], merged['area_km2'], color='red', marker='o')
    ax1.tick_params(axis='y', labelcolor='red')

    # Suppression cost line
    ax2 = ax1.twinx()
    ax2.set_ylabel('Suppression Cost (Billions $)', color='blue')
    ax2.plot(merged['fireyear'], merged['Constant Dollars'], color='blue', marker='s')
    ax2.tick_params(axis='y', labelcolor='blue')

    plt.title('Average Fire Size vs. Suppression Cost per Year')
    plt.grid(True)
    plt.tight_layout()
    print(merged)
    return plt.show()