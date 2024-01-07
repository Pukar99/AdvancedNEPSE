
# Step 1: Data Preprocessing
- Conduct initial data preprocessing steps such as converting the data into the appropriate format and setting the date column as the index.

### File Location
\`\`\`python
df1 = pd.read_csv('../../datasrc/NepseDataHistorical1997_2024.csv')
\`\`\`
(Copy and paste the code above into your environment to load the dataset.)

# Step 2: Exploratory Data Analysis (EDA)

## Problems Identified:
- Data from the year 2015 is showing `NaN` values.
- I addressed all the data issues in level 2 with the following code:
\`\`\`python
df = pd.read_csv('../../datasrc/NepseDataHistorical1997_2024_sorted.csv')
\`\`\`

## EDA Phase 1:
- After resolving the initial data preprocessing issues, I conducted a statistical analysis as part of the EDA process using:
\`\`\`python
df.describe()
\`\`\`

## EDA Phase 2:
- In this phase, I created `mdf` as the monthly DataFrame and `wdf` as the weekly DataFrame. I then narrowed the data into weekly and monthly intervals to continue the analysis.
- Here's how you can create the monthly and weekly DataFrames:

\`\`\`python
# Weekly DataFrame
wdf = df.resample('W').agg({'open': 'first', 
                            'high': 'max', 
                            'low': 'min', 
                            'close': 'last', 
                            'turnover': 'sum'})

# Monthly DataFrame
mdf = df.resample('M').agg({'open': 'first', 
                            'high': 'max', 
                            'low': 'min', 
                            'close': 'last', 
                            'turnover': 'sum'})
\`\`\`
