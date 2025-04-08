import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_csv():
    file_path = '/Users/stasyaeasley/Desktop/Yearly_Suppression_Costs.csv'
    file_2 = "/annual-index-value_annual-percent-change.csv"

    df1 = pd.read_csv(file_path, thousands=',')
    df2 = pd.read_csv(file_2)

    df2=df2.drop(df2.index[0:38])
    df2 = df2.reset_index(drop=True)
    df1=df1.drop([39,40])

    df = pd.merge(df1, df2, on="Year")

    print(df1)
    print(df2)
    print(df.columns)


    df["Year"] = df["Year"].astype(int)
    year = df["Year"]
    df["Fires"]= df["Fires"].astype(int)
    cpi = df["CPI"]
    df["Forest Service"] = df["Forest Service"].str.replace(',', '').str.replace('$', '').astype(int)
    df["DOI Agencies"] = df["DOI Agencies"].str.replace(',', '').str.replace('$', '').astype(int)
    df["Acres"]= pd.to_numeric(df["Acres"].str.replace(",", "")).astype(int)
    df["Total"] = df["Total"].str.replace(',', '').str.replace('$', '').astype(int)
    total = df["Total"]
    cpi_2023 = df.loc[year == 2023, "CPI"].values[0]

    df["Constant Dollars"] = (total * cpi_2023 / cpi ).astype(int)
    constant_dollars = df["Constant Dollars"]

    plt.plot(year, constant_dollars)

    # plt.xlabel("Year")
    # plt.ylabel("Constant Dollars")
    # plt.ylim(0,200000)
    # plt.show()

    df.to_csv("Yearly_Suppression_Costs_Clean.csv", index=False)

def add_km():
    df = pd.read_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv", thousands=',')
    df['km2'] = (df['Acres'] * 0.00404686).astype(int)
    return df.to_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv", index=False)


def yrvskmvscost():
    df = pd.read_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv")
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Total acres burned line
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Acres Burned (km²)', color='red')
    # seems cyclic/seasonal - goes up and down drastically every other year
    ax1.plot(df['Year'], df['km2'], color='red', marker='o')
    ax1.tick_params(axis='y', labelcolor='red')

    # Suppression cost line
    ax2 = ax1.twinx()
    ax2.set_ylabel('Suppression Cost (Billions $)', color='blue') # constant dollars
    ax2.plot(df['Year'], df['Constant Dollars'], color='blue', marker='s')
    ax2.tick_params(axis='y', labelcolor='blue')

    plt.title('Total Acres Burned vs. Suppression Cost per Year')
    plt.grid(True)
    plt.tight_layout()
    return plt.show()

def kmvscost():
    df = pd.read_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv")
    # Total acres burned vs supression costs
    plt.xlabel('Total Area Burned (km²)')
    plt.ylabel('Supression Cost (Billions $)')
    plt.scatter(df['km2'], df['Constant Dollars'], color='blue', alpha=0.7)

    # regression line
    m, b = np.polyfit(df['km2'], df['Constant Dollars'], 1)
    plt.plot(df['km2'], m * df['km2'] + b, color='red', linestyle='--')

    plt.title('Total Area Burned vs. Suppression Cost')
    plt.grid(True)
    plt.tight_layout()
    return plt.show()

def droughtvsburn():
    return

def numberfires():
    df = pd.read_csv("/Users/stasyaeasley/dsprojects/dsprojects/Yearly_Suppression_Costs_Clean.csv")
    plt.xlabel('Year')
    plt.ylabel('Number of Fires $)')
    plt.scatter(df['Year'], df['Fires'], color='blue', alpha=0.7)
    plt.grid(True)
    plt.tight_layout()
    return plt.show()



# drought index
# cyclic
# government?
# el nino
# how the data is made (like counting number of fires)
# 2023 was less acres but lots of money. did they spend more money to keep the acreage down?
# distribution of fire sizes in eastern vs western us like how big they are - distribution of values, histogram.
# what are we looking for?