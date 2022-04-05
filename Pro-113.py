from google.colab import files
dataStory = files.upload()
import plotly.express as px
import pandas as pd
import csv 
import st as st
import numpy as np
import plotly.figure_factory as ff
import random
df = pd.read_csv("Savings.csv")
fig = px.scatter(df,y="quant_saved",color = "highschool_completed")
fig.show()
with open("Savings.csv") as f:
  reader = csv.reader(f)
  Savings_data = list(reader)
Savings_data.pop(0)
entryno = len(Savings_data)
tot_remed = 0
for i in Savings_data :
  if int(i[3]) == 1 :
    tot_remed = tot_remed+1
all_savings = []
for data in Savings_data:
  all_savings.append(float(data[0]))
print(f"Mean of savings - {st.mean(all_savings)}")
print(f"Median of savings - {st.median(all_savings)}")
print(f"Mode of savings - {st.mode(all_savings)}")
rem_savings = []
notRem_savings = []
for data in Savings_data:
  if int(data[3])==1:
    rem_savings.append(float(data[0]))
  else:
    notRem_savings.append(float(data[0]))
print("Results for people who were reminded to save") 
print(f"Mean of savings - {st.mean(rem_savings)}")
print(f"median of savings - {st.median(rem_savings)}")
print(f"Mode of savings - {st.mode(rem_savings)}")
print("\n\n")
print(f"Mean of savings - {st.mean(notRem_savings)}")
print(f"median of savings - {st.median(notRem_savings)}")
print(f"Mode of savings - {st.mode(notRem_savings)}")
print(f"Stdev of people not reminded savings - {st.stdev(notRem_savings)}")
print(f"Stdev of people reminded savings - {st.stdev(rem_savings)}")
print(f"Stdev of all savings - {st.stdev(all_savings)}")
q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1

print(f"Q1 - {q1}")
print(f"Q3 - {q3}")
print(f"IQR - {iqr}")

lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr

print(f"Lower Whisker - {lower_whisker}")
print(f"Upper Whisker - {upper_whisker}")

#Creating a new DataFrame
new_df = df[df["quant_saved"] < upper_whisker]
sampling_mean_list = []
mean_sampling = st.mean(sampling_mean_list)
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(all_savings))
  sampling_mean_list.append(st.mean(temp_list))
print(f"Standard deviation of the sampling data - {st.stdev(sampling_mean_list)}")
print(f"Mean of Population - {st.mean(all_savings)}")
print(f"Mean of Sampling Distribution - {mean_sampling}")
reminded_df = new_df.loc[new_df["rem_any"] == 1]
not_reminded_df = new_df.loc[new_df["rem_any"] == 0]
not_reminded_savings = not_reminded_df["quant_saved"].tolist()

sampling_mean_list_not_reminded = []
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(not_reminded_savings))
  sampling_mean_list_not_reminded.append(st.mean(temp_list))

mean_sampling_not_reminded = st.mean(sampling_mean_list_not_reminded)
stdev_sampling_not_reminded = st.stdev(sampling_mean_list_not_reminded)

print(f"Mean of Sampling (Not Reminded) -> {mean_sampling_not_reminded}")
print(f"Standard Deviation of Sampling (Not Reminded) -> {stdev_sampling_not_reminded}")
age = []
savings = []
for data in Savings_data:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))
temp_df = new_df[new_df.age != 0]
correlation = np.corrcoef(age, savings)
age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")
first_std_deviation_start = mean_sampling_not_reminded-stdev_sampling_not_reminded
first_std_deviation_end = mean_sampling_not_reminded+stdev_sampling_not_reminded
second_std_deviation_start = mean_sampling_not_reminded-(2*stdev_sampling_not_reminded)
second_std_deviation_end = mean_sampling_not_reminded+(2*stdev_sampling_not_reminded)
third_std_deviation_start = mean_sampling_not_reminded-(3*stdev_sampling_not_reminded)
third_std_deviation_end = mean_sampling_not_reminded+(3*stdev_sampling_not_reminded)
reminded_savings = reminded_df["quant_saved"].tolist()

sampling_mean_list_reminded = []
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(reminded_savings))
  sampling_mean_list_reminded.append(st.mean(temp_list))

mean_sampling_reminded = st.mean(sampling_mean_list_reminded)
stdev_sampling_reminded = st.stdev(sampling_mean_list_reminded)

print(f"Mean of Sampling (Reminded) -> {mean_sampling_reminded}")
print(f"Standard Deviation of Sampling (Reminded) -> {stdev_sampling_reminded}")
z_score = (mean_sampling_reminded - mean_sampling_not_reminded) / stdev_sampling_not_reminded
print(f"Z-Score is - {z_score}")