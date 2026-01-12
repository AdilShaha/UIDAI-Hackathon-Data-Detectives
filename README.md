# Project: Bio-Gap Radar (By Team Data Detectives)
# BCA 1st Year - UIDAI Hackathon 2026

Hey! We are Team Data Detectives. Being in our 1st year of BCA, we really wanted to find a real-world problem rather than just doing some basic coding. While we were going through the UIDAI datasets, we found something very strange which we now call the "Silent Gap."

Basically, we saw that lots of kids (between 5 to 17 years) are visiting Aadhaar centers to change their phone numbers or home addresses. But the sad part is, they are leaving the center without doing their Mandatory Biometric Update (MBU), even though they are already there at the counter! This is a huge missed opportunity for the system.



### How our logic works:
We kept things very simple and used Python to find the "Red Zones." 
First, we calculated the Gap by subtracting Biometric updates from Demographic updates. If the Gap is big in any district, it means the center is busy but the mandatory work is being ignored. 
Then, we used these numbers to make charts that show UIDAI exactly where they need to tell their operators to be more careful.



### Tech stuff we used:
- We used Python and Pandas to handle the 7.5 Lakh rows. Honestly, our laptops were lagging a lot, so we used "Data Sampling" to make the code run faster.
- For the visuals, we used Seaborn and Matplotlib to create graphs that highlight the problem districts.

### How to run the Radar:
1. Put the demographic, biometric, and enrolment CSV files in the folder.
2. Just run "python final_analysis.py".
3. You will get the final report and two graphs immediately.

It was a great experience for us to see how a little bit of data analysis can help solve such a big problem for the government. We really hope our Bio-Gap Radar idea helps out!
