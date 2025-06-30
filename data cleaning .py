import pandas as pd

# Load data
df = pd.read_csv("student_college_list.csv")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing essential info
df.dropna(subset=["Name", "College"], inplace=True)

# Strip whitespace and unify case
df["Name"] = df["Name"].str.strip().str.title()
df["College"] = df["College"].str.strip().str.upper()

# Remove invalid emails
df = df[df["Email"].str.contains(r"[^@]+@[^@]+\.[^@]+", na=False)]

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned data
df.to_csv("cleaned_student_college_list.csv", index=False)
