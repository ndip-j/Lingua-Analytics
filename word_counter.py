import csv

def count_words(text):
    if not text:
        return 0
    return len(text.split())

try:
    with open("linguaspan_mock_transcripts.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            word_count = count_words(row["text"])

            print(
                row["transcript_id"],
                row["speaker"],
                word_count
            )

except FileNotFoundError:
    print("Transcript file not found.")