# WHO Mortality Data Analysis

This project analyzes mortality data from the World Health Organization (WHO), focusing on deaths by cause, age group, region, and gender. The analysis uses Python, pandas for data manipulation, and matplotlib for visualization.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Data Sources](#data-sources)
3. [Data Cleaning and Processing](#data-cleaning-and-processing)
4. [Analysis and Visualization](#analysis-and-visualization)
5. [Exported Graphs](#exported-graphs)
6. [Requirements](#requirements)
7. [Usage](#usage)
8. [Output](#output)

---

## Project Description
The code processes multiple WHO mortality datasets, cleans the data, and generates visualizations to understand trends in mortality across different causes, age groups, regions, and genders.

---

## Data Sources
The analysis uses the following datasets:

- `Injury` deaths CSV
- `Communicable, maternal, perinatal and nutritional conditions` CSV
- `Noncommunicable diseases` CSV

All CSVs are expected to be in the `./data/` folder.

---

## Data Cleaning and Processing
Steps performed on the datasets:

1. Combine multiple CSV files into a single dataframe.
2. Remove rows with more than one missing value and fill single missing values with 0.
3. Strip and clean column names.
4. Keep only male and female data (exclude 'All').
5. Add an `ID` column as the index.
6. Convert the death rate column to numeric.
7. Remove duplicates.
8. Map age groups to broader bins (`0-20`, `21-40`, `41-60`, `61-80`, `81+`).
9. Map years to broader decades (`1961-1970`, `1971-1980`, etc.).

---

## Analysis and Visualization
The following visualizations are generated:

1. **Cause of Death by Broad Age Group**
   - Pivoted data by age group and cause of death.
   - Graph Type: Line chart
   - Saved as: `Cause_of_death_by_Broad_Age_group.png`

   ![Cause of Death by Broad Age Group](./data/output/Cause_of_death_by_Broad_Age_group.png)  
   *Paste your exported graph here if needed.*

2. **Cause of Death by Region**
   - Pivoted data by region and cause of death.
   - Graph Type: Bar chart
   - Saved as: `Cause of Death by region.png`

   ![Cause of Death by Region](./data/output/Cause of Death by region.png)  
   *Paste your exported graph here.*

3. **Death Rate by Gender**
   - Pivoted data by gender.
   - Graph Type: Bar chart
   - Saved as: `Death rate by Gender.png`

   ![Death Rate by Gender](./data/output/Death rate by Gender.png)  
   *Paste your exported graph here.*

4. **Death Rate by Year**
   - Pivoted data by year and cause of death.
   - Graph Type: Bar chart
   - Saved as: `death rate by Year.png`

   ![Death Rate by Year](./data/output/death rate by Year.png)  
   *Paste your exported graph here.*

5. **Death Rate by Year in Accordance to Gender**
   - Pivoted data by year and gender.
   - Graph Type: Bar chart
   - Saved as: `death rate by Year in accordance to Gender.png`

   ![Death Rate by Year by Gender](./data/output/death rate by Year in accordance to Gender.png)  
   *Paste your exported graph here.*

---

## Requirements
- Python 3.x
- pandas
- matplotlib
- re (built-in)

Install dependencies using:

```bash
pip install pandas matplotlib
