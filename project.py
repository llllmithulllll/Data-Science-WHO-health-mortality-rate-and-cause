import os
import pandas as pd
import matplotlib.pyplot as plt
import re

# ------------------------------
# Set base directory
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'output')

# Make sure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Load CSV files
# ------------------------------
df_injuries = pd.read_csv(
    os.path.join(DATA_DIR, 'WHOMortalityDatabase_Deaths_sex_age_a_country_area_year-{filter_item_clustered_column_chart_5_key.selected_filter.valueLabels}_31st August 2025 18_48.csv'),
    skiprows=6, index_col=False
)
df_injuries['cause'] = "Injury"

df_comm = pd.read_csv(
    os.path.join(DATA_DIR, 'WHOMortalityDatabase_Deaths_sex_age_a_country_area_year-Communicable, maternal, perinatal and nutritional conditions_31st August 2025 18_45.csv'),
    skiprows=6, index_col=False
)
df_comm['cause'] = "Communicable"

df_noncomm = pd.read_csv(
    os.path.join(DATA_DIR, 'WHOMortalityDatabase_Deaths_sex_age_a_country_area_year-Noncommunicable diseases_31st August 2025 18_46.csv'),
    skiprows=6, index_col=False
)
df_noncomm['cause'] = "Incommunicable"

# ------------------------------
# Combine and sort
# ------------------------------
df_concat = pd.concat([df_injuries, df_comm, df_noncomm], ignore_index=True)
df_concat = df_concat.sort_values(by=["Region Code", "Year"])

# ------------------------------
# Clean the data
# ------------------------------

# removing rows which have more than 1 columns empty and if one empty, fill it with 0

df_concat = df_concat.dropna(thresh=df_concat.shape[1]-1).fillna(0)
df_concat.columns = df_concat.columns.str.strip().str.replace('"', '')

# removing data for all sex, only taking male and female

df_concat = df_concat[df_concat['Sex'] != 'All']
df_concat = df_concat[df_concat['Age Group'] != '[All]']

#adding id as index

df_concat["ID"] = range(1, len(df_concat) + 1)
df_concat.set_index("ID", inplace=True)

# Convert to numeric (invalid values → NaN → replace with 0)

df_concat["Death rate per 100 000 population"] = pd.to_numeric(
    df_concat["Death rate per 100 000 population"], errors="coerce"
).fillna(0)

#dropping duplicates 

df_concat = df_concat.drop_duplicates()

# Save cleaned data
df_concat.to_csv(os.path.join(OUTPUT_DIR, 'data.csv'))

# ------------------------------
# Helper functions
# ------------------------------
def age_to_number(age_str):
    if pd.isna(age_str):
        return None
    numbers = re.findall(r'\d+', str(age_str))
    return int(numbers[0]) if numbers else None

def map_age_robust(age_str):
    start_age = age_to_number(age_str)
    if start_age is None:
        return 'Unknown'
    elif start_age <= 20:
        return '0-20'
    elif start_age <= 40:
        return '21-40'
    elif start_age <= 60:
        return '41-60'
    elif start_age <= 80:
        return '61-80'
    else:
        return '81+'

def year_map(year):
    int_year = int(year)
    if int_year <= 1970:
        return '1961-1970'
    elif int_year <= 1980:
        return '1971-1980'
    elif int_year <= 1990:
        return '1981-1990'
    elif int_year <= 2000:
        return '1991-2000'
    elif int_year <= 2020:
        return '2001-2020'
    else:
        return '2021-2023'

# ------------------------------
# Apply mappings
# ------------------------------
df_concat['Age Group Broad'] = df_concat['Age Group'].apply(map_age_robust)
df_concat['Year_broad'] = df_concat['Year'].apply(year_map)

# ------------------------------
# Plots
# ------------------------------
# Cause of Death by Broad Age Group
pivot_df = df_concat.pivot_table(index="Age Group Broad", columns="cause", values="Number", aggfunc="sum")
pivot_df.plot(kind="line", figsize=(10,6))
plt.title("Cause of Death by Broad Age Group")
plt.xlabel("Age Group (years)")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=0)
plt.legend(title="Cause of Death")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "Cause_of_death_by_Broad_Age_group.png"))
plt.show()

# Cause of Death by Region
region_df = df_concat.pivot_table(index="Region Name", columns="cause", values="Number", aggfunc="sum")
region_df.plot(kind="bar", figsize=(10,6))
plt.title("Cause of Death by Region")
plt.xlabel("Region")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title="Cause of Death")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'Cause_of_Death_by_region.png'))
plt.show()

# Death rate by Gender in accordance to the Region
gender_region_df = df_concat.pivot_table(index="Region Name", columns="Sex", values="Number", aggfunc="sum")
gender_region_df.plot(kind="bar", figsize=(10,6))
plt.title("Death rate by Gender in accordance to the Region")
plt.xlabel("Region")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'Death_rate_by_Gender.png'))
plt.show()

# Death rate by Year
timeline_df = df_concat.pivot_table(index="Year_broad", columns="cause", values="Number", aggfunc="sum")
timeline_df.plot(kind="bar", figsize=(10,6))
plt.title("Death rate by Year")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title="Cause of Death")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'death_rate_by_Year.png'))
plt.show()

# Death rate by Year and Gender
gender_year_df = df_concat.pivot_table(index="Year_broad", columns="Sex", values="Number", aggfunc="sum")
gender_year_df.plot(kind="bar", figsize=(10,6))
plt.title("Death rate by Year in accordance to Gender")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'death_rate_by_Year_in_accordance_to_Gender.png'))
plt.show()
