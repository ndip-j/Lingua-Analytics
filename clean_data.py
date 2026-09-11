import pandas as pd

df = pd.read_csv("linguaspan_mock_transcripts_dirty.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())
print(df["speaker"].unique())
print(df["language"].unique())

# %%
df["speaker"] = (
    df["speaker"]
    .str.strip()
    .str.replace("-", " ", regex=False)
    .str.replace("_", " ", regex=False)
    .str.title()
)

# %%
print(df["speaker"].unique())

# %%
language_map = {
    "EN": "English",
    "english": "English",
    "English ": "English",

    "HA": "Hausa",
    "hausa": "Hausa",
    " Hausa": "Hausa",

    "YO": "Yoruba",
    "yoruba": "Yoruba",
    "Yoruba ": "Yoruba",

    "IG": "Igbo",
    "igbo": "Igbo",
    " Igbo": "Igbo"
}

df["language"] = df["language"].replace(language_map)

print(df["language"].unique())

# %%
df = df.drop_duplicates()   # handle duplicates
df["text"] = df["text"].fillna("")  # handle missing values in transcript text
df["word_count"] = df["text"].str.split().str.len() # create a new column for word count
df["short_transcript"] = df["word_count"] < 10  # create a new column to flag short transcripts

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
) # convert timestamp to datetime format, coerce errors to NaT

df["invalid_duration"] = (
    (df["duration_sec"] <= 0) |
    (df["duration_sec"] > 1000) |
    (df["duration_sec"].isna())
) # create a new column to flag invalid/suspicious durations

df.to_csv("cleaned_transcripts.csv", index=False)   # save the cleaned data to a new CSV file

# print summary statistics after cleaning
print("Rows after cleaning:", len(df))
print("Missing values:")
print(df.isnull().sum())

print("Short transcripts:")
print(df["short_transcript"].value_counts())

print("Invalid durations:")
print(df["invalid_duration"].value_counts()) 