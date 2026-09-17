SELECT *
FROM transcripts;

-- 1. Total number of transcripts
SELECT COUNT(*) AS total_transcripts
FROM transcripts;

-- 2. Total words across all transcripts
SELECT SUM(word_count) AS total_words
FROM transcripts;

-- 3. Average transcript duration
SELECT AVG(duration_sec) AS avg_duration
FROM transcripts;

-- 4. Number of transcripts by language
SELECT language, COUNT(*) AS transcript_count
FROM transcripts
GROUP BY language;

-- 5. Number of words by speaker
SELECT speaker, SUM(word_count) AS total_words
FROM transcripts
GROUP BY speaker
ORDER BY total_words DESC;

-- 6. Average duration by language
SELECT language, AVG(duration_sec) AS avg_duration
FROM transcripts
GROUP BY language
ORDER BY avg_duration DESC;

-- 7. Number of short transcripts
SELECT COUNT(*) AS short_transcripts
FROM transcripts
WHERE short_transcript = 1;

-- 8. Count of invalid durations
SELECT COUNT(*) AS invalid_durations
FROM transcripts
WHERE invalid_duration = 1;

CREATE TABLE speakers (
    speaker TEXT PRIMARY KEY,
    team TEXT
);

INSERT INTO speakers (speaker, team)
VALUES
    ('Speaker A', 'Sales'),
    ('Speaker B', 'Support'),
    ('Speaker C', 'Operations'),
    ('Speaker D', 'Sales'),
    ('Speaker E', 'Support');