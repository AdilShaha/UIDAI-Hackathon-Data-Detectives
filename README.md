# 🕵️‍♂️ Bio-Gap Radar: UIDAI Hackathon 2026
**Team Name:** Data Detectives  
**Track:** Demographic & Biometric Trends

## 👋 About Our Project
Hi! We are **Team Data Detectives**, 1st-year BCA students. 
For this hackathon, we tried to solve a specific problem: **"Silent Non-Compliance."**

We noticed that many children (Age 5-17) visit Aadhaar centers to update their Name or Address (Demographic details) but often forget to update their **Biometrics**, which is mandatory. Our project uses data to find exactly which states and districts have the highest number of such "missing updates."

## 💡 How It Works (The Logic)
We didn't use complex AI, just smart data analysis using **Python**:
1.  **The Formula:** We calculated `Gap = (People who updated Demographics) - (People who updated Biometrics)`.
2.  **The Result:** If the Gap is high, it means people are visiting centers but leaving without the mandatory update.
3.  **Visualization:** We created graphs to show these "Red Zones" so UIDAI can plan targeted camps there.

## Tech Stack Used
- **Language:** Python
- **Libraries:** Pandas (for data cleaning & merging), Seaborn/Matplotlib (for graphs)
- **Technique:** We used **Data Sampling** because the dataset had 7.5 Lakh+ rows, and this made our code run super fast!

## How to Run the Code
If you want to test our project, please follow these steps:

1.  Make sure you have the CSV files (`demographic.csv`, `biometric.csv`, `enrolment.csv`) in the same folder.
2.  Install required libraries (if not already installed):
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  Run our script:
    ```bash
    python final_analysis.py
    ```
4.  The code will generate:
    - Two HD Graphs (saved as PNG).
    - A `final_hackathon_report.csv` file with the results.

---
*Submitted by Team Data Detectives for UIDAI Hackathon 2026.*
