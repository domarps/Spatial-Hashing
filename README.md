# Spatial-Hashing
---
Encoding geo-locations as spatial-indices for simultaneous text and location searching

1. Read data from CSV
      * Each row is article text (string), X coord (double), Y coord (double)
      * Store rows as objects

2. Create mapping from words to articles
      * Words are tokens from article text, as well as strings corresponding to location E.g., (1.23,4.56) yields strings “1_4”, “12_45”, “123_456”
      * Use stop words, stemming rules (code for Porter stemmer is readily available)
      * Mapping should be in the form of skip lists from words to list of articles (“posting lists”)

3. Implement search engine: inputs is location and words
      * Return articles that are near that location and contain those words
      * Key computation: intersect posting lists

