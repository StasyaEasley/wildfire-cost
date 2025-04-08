import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import os
import glob
from tqdm import tqdm
import matplotlib.colors as mcolors

shapefile_folder = "/Users/stasyaeasley/Desktop/droughtshapefiles"
shapefiles = sorted(glob.glob(os.path.join(shapefile_folder, "**/*.shp"), recursive=True))

world = gpd.read_file("/Users/stasyaeasley/Desktop/droughtshapefiles/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")
us_outline = world[world['NAME'] == 'United States of America']

frames = []

for shp in tqdm(shapefiles):
    gdf = gpd.read_file(shp)

    date_str = "".join([part for part in shp.split("_") if part.isdigit()])
    if not date_str:
        date_str = "".join(filter(str.isdigit, os.path.basename(shp)))
    date = pd.to_datetime(date_str[:8], format="%Y%m%d", errors='coerce')

    if 'DM' in gdf.columns and not gdf.empty:
        gdf = gdf[['geometry', 'DM']]
        gdf['date'] = date
        frames.append(gdf)

all_data = pd.concat(frames, ignore_index=True)

drought_colors = {
    'D0': '#ffffb2',
    'D1': '#fecc5c',
    'D2': '#fd8d3c',
    'D3': '#f03b20',
    'D4': '#bd0026'
}
levels = ['D0', 'D1', 'D2', 'D3', 'D4']

fig, ax = plt.subplots(figsize=(10, 6))
plt.axis('off')

dates = sorted(all_data['date'].dropna().unique())


def update(frame_num):
    ax.clear()
    ax.axis('off')

    ax.set_xlim(-130, -60)  # Longitude bounds (left and right edges of the US)
    ax.set_ylim(24, 50)
    ax.set_aspect('equal')

    us_outline.plot(ax=ax, color="#f0f0f0", edgecolor="lightgray", linewidth=0.5)

    week = dates[frame_num]
    data = all_data[all_data['date'] == week]
    data.plot(ax=ax, column='DM', cmap=mcolors.ListedColormap([drought_colors[l] for l in levels]),
              categorical=True, legend=False, edgecolor='none')
    ax.set_title(f"U.S. Drought Monitor\n{week.strftime('%Y-%m-%d')}", fontsize=16)


# 6. Animate
ani = FuncAnimation(fig, update, frames=len(dates), repeat=False)

# 7. Save as GIF
# ani.save("drought_animation.gif", writer='pillow', fps=5)

# Optional: Save as MP4 (requires ffmpeg)
ani.save("drought_animation.gif", writer='pillow', fps=10)