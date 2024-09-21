# 🌍 Surface Temperature Analysis of North and South America's Largest Countries

This project provides an analysis of surface temperatures across the largest countries in North and South America, spanning from the 1960s to 2022. The visualizations compare temperature trends across decades and calculate the average temperature for each decade, helping to identify patterns and possible climate changes in different regions.

## 🔥 Features

- **Countries Analyzed**:
  - North America: 🇨🇦 **Canada**, 🇺🇸 **USA**, 🇲🇽 **Mexico**
  - South America: 🇦🇷 **Argentina**, 🇧🇷 **Brazil**, 🇵🇪 **Peru**

- **Data Range**: 
  - 1960s to 2020-2022
  
- **Visualization**: 
  - Line plots for each country showing the temperature trend.
  - Stem plots showing the average temperature trends of all three countries combined in both North and South America.

- **Purpose**: 
  - Analyze and compare how surface temperatures in the largest countries in both continents have evolved over time.

## 📊 Libraries Used

- **NumPy**: For numerical computations and handling arrays.
- **Pandas**: To work with tabular data.
- **Matplotlib**: For data visualization and plotting.

## 🚀 Getting Started

### Data

The project uses a dataset stored in an Excel file named `wide_format_annual_surface_temp[1].csv`. Each row in the dataset corresponds to a country, and temperature data for different decades is stored in specific columns.

## 📈 Visualizations

### South America

- **Countries**: Argentina, Brazil, and Peru
- **Plot**: A line plot showing surface temperatures for each country across decades.
- **Trend**: The trend highlights how surface temperatures have changed over time in South America.

![South America Temperature Trends](path-to-south-america-plot.png)

### North America

- **Countries**: Canada, USA, and Mexico
- **Plot**: A line plot showing surface temperatures for each country across decades.
- **Trend**: The trend showcases temperature evolution in North America.

## 🔧 Code Explanation

The Python script is structured as follows:

1. **Import Libraries**: Load the required libraries (`NumPy`, `Pandas`, `Matplotlib`).
2. **Load Data**: Read the `wide_format_annual_surface_temp[1].csv` file into a Pandas DataFrame.
3. **Define Helper Function**: `hesapla()` is used to calculate the mean temperature for a country across decades.
4. **Plot South America**: Plot the temperature trends for Argentina, Brazil, and Peru.
5. **Plot North America**: Plot the temperature trends for Canada, USA, and Mexico.
6. **Calculate and Plot Averages**:
   - Compute the average surface temperature for the three largest countries in North and South America.
   - Plot these averages using stem plots.

### Functions

- `hesapla(a)`: Calculates the average surface temperature for the country indexed by `a` in the dataset, across the decades.
  
  **Example**:
  ```python
  hesapla(8)  # For Argentina
  hesapla(20) # For Brazil
  hesapla(129) # For Peru
  ```

## 🔗 Resources

- **Global Warming Trends Dataset**: [Dataset Source](https://www.kaggle.com/datasets/jawadawan/global-warming-trends-1961-2022?resource=download&select=wide_format_annual_surface_temp.csv)

---
