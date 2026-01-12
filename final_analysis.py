import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuration ---
sns.set(style="whitegrid")

# --- 1. Data Loading & Preprocessing ---
def clean_and_load(filename):
    """Loads CSV and standardizes column names/dates."""
    df = pd.read_csv(filename)
    # Standardize column names to lowercase and remove spaces
    df.columns = df.columns.str.lower().str.strip()
    # Parse dates correctly using Indian format (Day-Month-Year)
    df['date'] = pd.to_datetime(
        df['date'],
        dayfirst=True,
        errors='coerce'
    )
    
    return df

# Loading the datasets
try:
    df_demo = clean_and_load('demographic.csv')
    df_bio = clean_and_load('biometric.csv')
    df_enr = clean_and_load('enrolment.csv')
except FileNotFoundError:
    print("Error: Files not found. Please ensure CSV files are in the directory.")
    exit()

# --- 2. Methodology: Data Merging ---
# Merging on composite key: Date + Location to ensure data integrity
merge_keys = ['date', 'state', 'district', 'pincode']
master_df = pd.merge(df_demo, df_bio, on=merge_keys, how='inner')
master_df = pd.merge(master_df, df_enr, on=merge_keys, how='inner')

# --- 3. Analysis: Calculating the Gap ---
# Logic: Gap = Demographic Updates (Age 5-17) - Biometric Updates (Age 5-17)
# Using standardized column names
master_df['biometric_gap'] = master_df['demo_age_5_17'] - master_df['bio_age_5_17']

# Removing negative noise (clipping values < 0 to 0)
master_df['biometric_gap'] = master_df['biometric_gap'].clip(lower=0)

# Aggregating data state-wise for the top-level report
state_gap = master_df.groupby('state')['biometric_gap'].sum().sort_values(ascending=False).head(8)

# --- 4. Visualizations ---

# FIGURE 1: Bar Chart (Top Defaulter States)
plt.figure(figsize=(10, 6))
sns.barplot(x=state_gap.values, y=state_gap.index, palette='magma')
plt.title('States with Highest Missing Mandatory Biometric Updates (Age 5-17)')
plt.xlabel('Count of Missing Updates')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# FIGURE 2: Scatter Plot (Optimized for Large Datasets)
# OPTIMIZATION: The dataset has ~7.5 Lakh rows. Plotting all points causes lag.
# We take a random sample of 5000 points to visualize the trend instantly.
plt.figure(figsize=(9, 9))

if len(master_df) > 5000:
    plot_data = master_df.sample(n=5000, random_state=42) # Consistent sampling
else:
    plot_data = master_df

sns.scatterplot(data=plot_data, x='age_5_17', y='biometric_gap', hue='state', alpha=0.6)
plt.title('Correlation: Enrolment Volume vs. Compliance Gap (Sampled View)')
plt.xlabel('Total Enrolment Activity (Age 5-17)')
plt.ylabel('Biometric Gap (Missing Updates)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Exporting key findings for reference
state_gap.to_csv('final_report.csv')
