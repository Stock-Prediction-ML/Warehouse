# Planning

Plan details for the project

## Initial Data Gathering

The data will be gathered using python. 
APIs will be used when available. 
As data is gathered, it will be stored locally, as buffer, then batch uploaded to AWS (S3).
Later this will be moved to automatic data ingestion pipeline.

### Data Sources

- [ ] [Twitter](https://developer.twitter.com/en/docs)
- [ ] [StockNewsAPI](https://stocknewsapi.com/)
- [ ] [AlphaVantage](https://www.alphavantage.co/)

### Source Details

* Twitter - Collect daily tweets from notable finance related accounts such as `@jimcramer`
* StockNewsAPI - Provides pre-labeled news stories
* AlphaVantage - The stock data source

#### Twitter Details

* Twitter
  * Scrape tweets from handles daily
  * Store tweets in JSON, files named: <screen_name>_<time_created>.txt
  * Store 'important' features ~~in tsv file, named: <screen_name>_<date>.txt~~ query JSON with Hive?
    * tweet_id
    * text
    * hashtags
    * mentions
    * urls
    * created_at
    * user_id
    * screen_name
    * emojis
  * Push results to an S3 bucket

## Data Ingestion

NiFi will be used to bring in data from web sources. This data will be pushed to an S3 bucket for long-term storage.

## Storage

Data will be stored in an amazon S3 bucket for long term storage. 
S3 buckets can be easily integrated with other AWS tools such as EMR. 
The datalake will be setup on-demand with Amazon EMR and Hive.

## Other Ideas

* Scrape with multiple agents
* Bring in data from other sources
  * NYT (API)
  * Reddit (API)
  * Other alternative data such as weather events
* Preprocess text
  * Clean the text
  * Vectorize with a pretrained tool
    * [AllanNLP](https://allennlp.org/)
    * [IXA Pipelines](http://ixa2.si.ehu.es/ixa-pipes/)
* Use a continuous data ingestion platform
