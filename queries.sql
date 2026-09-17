SELECT *
FROM transcripts;

SELECT speaker, language, duration_sec
FROM transcripts;

SELECT *
FROM transcripts
WHERE language = 'English';

SELECT *
FROM transcripts
WHERE duration_sec > 100;

SELECT *
FROM transcripts
WHERE language = 'Hausa'
AND duration_sec > 100;

SELECT *
FROM transcripts
ORDER BY duration_sec DESC;

SELECT *
FROM transcripts
WHERE speaker = 'Speaker A';

SELECT *
FROM transcripts
WHERE word_count > 15;