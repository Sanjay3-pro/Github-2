import pandas as pd

df = pd.read_csv("data/students.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nAverage marks:")
print(df["marks"].mean())

print("\nGender-wise average marks:")
print(df.groupby("gender")["marks"].mean())
import matplotlib.pyplot as plt

gender_avg = df.groupby("gender")["marks"].mean()

gender_avg.plot(kind="bar", title="Average Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

