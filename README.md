# **WHO Mortality Data Analysis and Predictive Modeling**

This project analyzes mortality data from the World Health Organization (WHO), focusing on deaths by cause, age group, region, and gender. The analysis uses Python with the pandas and matplotlib libraries for data manipulation and visualization. Additionally, the project includes a predictive modeling component using scikit-learn to forecast mortality numbers.

## **Table of Contents**

1. [Project Description](https://www.google.com/search?q=%23project-description)  
2. [Data Sources](https://www.google.com/search?q=%23data-sources)  
3. [Data Cleaning and Processing](https://www.google.com/search?q=%23data-cleaning-and-processing)  
4. [Analysis and Visualization](https://www.google.com/search?q=%23analysis-and-visualization)  
5. [Data Preparation for Modeling](https://www.google.com/search?q=%23data-preparation-for-modeling)  
6. [Model Generation](https://www.google.com/search?q=%23model-generation)  
7. [Requirements](https://www.google.com/search?q=%23requirements)  
8. [Usage](https://www.google.com/search?q=%23usage)  
9. [Output](https://www.google.com/search?q=%23output)

## **Project Description**

The project's primary goal is to provide a comprehensive understanding of global mortality trends. It processes multiple WHO mortality datasets, cleans and prepares the data, and generates key visualizations to highlight patterns across different causes, age groups, regions, and genders. The final phase of the project involves preparing the cleaned data for a predictive model to forecast future mortality figures.

## **Data Sources**

The analysis is designed to use the following datasets, which should be placed in the ./data/ directory:

* Injury\_deaths.csv  
* Communicable\_maternal\_perinatal\_nutritional\_conditions\_deaths.csv  
* Noncommunicable\_diseases\_deaths.csv

For demonstration purposes, the provided script will generate placeholder data to ensure it is runnable.

## **Data Cleaning and Processing**

The data\_analysis.py script performs the following steps to ensure data quality and consistency:

1. **Data Consolidation**: Combines the multiple CSV files into a single, unified pandas DataFrame.  
2. **Missing Value Handling**: Imputes missing values by filling single occurrences with 0 and removing rows with more than one missing value.  
3. **Column Standardization**: Cleans and standardizes column names by stripping whitespace and special characters.  
4. **Data Filtering**: Excludes aggregate data, retaining only entries for 'Male' and 'Female'.  
5. **Index Assignment**: Adds a unique ID column to serve as an index for each record.  
6. **Type Conversion**: Converts the death rate column to a numeric data type for mathematical operations.  
7. **Duplicate Removal**: Identifies and removes any duplicate rows to maintain data integrity.  
8. **Categorical Binning**: Groups age ranges and years into broader, more manageable bins (0-20, 21-40, etc.) for simplified analysis.  
9. **Data Export**: Saves the final cleaned and processed DataFrame as data.csv in the data/output directory for subsequent use.

## **Analysis and Visualization**

The data\_analysis.py script generates five distinct visualizations, saved as .png files, to illustrate key mortality trends.

1. **Cause of Death by Broad Age Group**: A line chart showing how different causes of death change across age groups.  
2. **Cause of Death by Region**: A bar chart comparing the primary causes of death across various regions.  
3. **Death Rate by Gender**: A bar chart highlighting the difference in overall death rates between males and females.  
4. **Death Rate by Year**: A bar chart visualizing how death rates have trended over time across different causes.  
5. **Death Rate by Year by Gender**: A stacked bar chart showing the breakdown of death rates by gender over time.

## **Predictive Modeling**

The model\_generation.py script focuses on building a machine learning model to predict mortality numbers.

## **Data Preparation for Modeling**

The model\_generation.py script performs the following steps to prepare data for a machine learning model:

1. **Data Loading**: The cleaned data.csv file is loaded as the primary dataset.  
2. **Feature and Target Selection**: The script identifies the input features (Age Group, Region Name, Year, Sex, Cause) and the target variable (Numbers of deaths).  
3. **One-Hot Encoding**: Categorical features are converted into a numerical format suitable for machine learning algorithms using one-hot encoding.  
4. **Data Splitting**: The dataset is split into training and testing sets to evaluate the model's performance on unseen data.

## **Model Generation**

The model\_generation.py script continues with the following steps to generate the predictive model:

1. **Model Training**: A RandomForestRegressor model is trained on the training data. This model is chosen for its robustness and ability to handle complex feature interactions.  
2. **Model Evaluation**: The model's predictions on the test set are evaluated using two key metrics:  
   * **Mean Squared Error (MSE)**: Measures the average squared difference between the actual and predicted values.  
   * **R-squared (**R2**)**: Represents the proportion of the variance in the dependent variable that is predictable from the independent variables.

## **Requirements**

To run this project, you need Python and the following libraries. The re library is a built-in module.

pip install pandas matplotlib scikit-learn

## **Usage**

1. Place your raw data CSV files in a data directory.  
2. Run the data\_analysis.py script to perform data cleaning and generate the visualizations. This will also create the cleaned data.csv file and an output folder with the plots.  
3. Run the model\_generation.py script to train and evaluate the predictive model.

python data\_analysis.py  
python model\_generation.py  
