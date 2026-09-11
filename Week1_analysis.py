import pandas as pd

df = pd.read_csv("linguaspan_mock_transcripts.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

df["word_count"] = df["text"].fillna("").str.split().str.len()

# Select columns
print(df[["speaker", "language", "word_count"]])

# Filter
print(df[df["language"] == "English"])

# Longer transcripts
print(df[df["duration_sec"] > 60])

# Sort
print(df.sort_values("duration_sec", ascending=False))


# Transcript count by language
print(df.groupby("language").size())

# Total words by speaker
print(
    df.groupby("speaker")["word_count"]
    .sum()
    .sort_values(ascending=False)
)

# Average duration by language
print(
    df.groupby("language")["duration_sec"]
    .mean()
    .sort_values(ascending=False)
)

speaker_info = pd.DataFrame({
    "speaker": ["Speaker A", "Speaker B"],
    "team": ["Sales", "Support"]
})

merged_df = df.merge(
    speaker_info,
    on="speaker",
    how="left"
)

print(merged_df.head())