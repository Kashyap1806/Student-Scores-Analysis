import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
import numpy as np

df = pd.read_csv(r"C:\\Users\\ASUS\\Desktop\\student_scores.csv")
print(df.info())

#Removing 'Unnamed: 0', which is a unnecessary column
df =df.drop('Unnamed: 0', axis=1)
print(df.info())

# NUmber of Females vs Male
female_male = sns.countplot(x='Gender',data=df)
plt.show()

# Parents' Education vs Student's Scores
df_melted = df.melt(id_vars=['ParentEduc'],  # Keep these columns unchanged
                    value_vars=['MathScore', 'ReadingScore', 'WritingScore'],  # Melt only these columns
                    var_name='Subject', value_name='Score')
# Create grouped bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='ParentEduc', y='Score', hue='Subject', data=df_melted)
# Set title and labels
plt.title('Math, Reading, and Writing Scores by Parent Education')
plt.xlabel('Parent Education Level')
plt.ylabel('Scores')
plt.show()

#PArents' Marital Status vs Student's Scores
df_melted = df.melt(id_vars=['ParentMaritalStatus'],  # Keep these columns unchanged
                    value_vars=['MathScore', 'ReadingScore', 'WritingScore'],  # Melt only these columns
                    var_name='Subject', value_name='Score')
print(df_melted.head())
# Create grouped bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='ParentMaritalStatus', y='Score', hue='Subject', data=df_melted)
# Set title and labels
plt.title('Math, Reading, and Writing Scores by Parent Marital Status')
plt.xlabel('Parent Marital Status')
plt.ylabel('Scores')
plt.show()

#Creating boxplots for Scores
plt.figure(figsize=(10, 6))
df.boxplot(column=['MathScore', 'ReadingScore', 'WritingScore'],patch_artist =True)
# Set title and labels
plt.title('Boxplots of Math, Reading, and Writing Scores')
plt.ylabel('Scores')
plt.xlabel('Subjects')
plt.show()

#Creating Bar Plots and Pie Chart to visualize different ethnic groups
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='EthnicGroup', palette='viridis', order='Group A','Group B', 'Group C', 'Group D', 'Group E')
plt.title('Count of Each Ethnic Group')
plt.xlabel('Ethnic Group')
plt.ylabel('Count')
plt.show()

# 2. Create a Pie Chart using Matplotlib
ethnic_counts = df['EthnicGroup'].value_counts()
print(ethnic_counts.head())
plt.figure(figsize=(8, 8))
plt.pie(ethnic_counts, labels=ethnic_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(ethnic_counts)))
plt.title('Distribution of Ethnic Groups')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()
