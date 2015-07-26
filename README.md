# osu! Mod-specific Ranking

Rankings for specific mod combinations of all osu! standard players in the top 10 000.

## Instructions
* `python scrape-top10k.py` to create `names.csv`.
* `python fetch-top-plays.py` to create `scores.csv`, which requires an `api_key.py` file to exist that defines a variable `key` that contains your osu! api key.
* `python process-scores.py` to create markdown tables with the filters specified in the file.
