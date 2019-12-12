# Planning

Plan details for the project

## Data Collection/Ingestion

* Use NiFi on a EC2 instance to collect the data.
* As data is gathered, it will be stored locally, as buffer, then batch uploaded to AWS (S3).

**TODO**: Add diagram showing this

### Data Sources

- [ ] [Twitter](https://developer.twitter.com/en/docs)
- [ ] [StockNewsAPI](https://stocknewsapi.com/)
- [ ] [AlphaVantage](https://www.alphavantage.co/)
- [ ] Reddit

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

## Storage

Data will be stored in an amazon S3 bucket for long term storage. 
S3 buckets can be easily integrated with other AWS tools such as EMR. 
The datalake will be setup on-demand with Amazon EMR and Hive.

## WareHouse Logical Design

A star schema will be used. 
Should consider providing schemas multiple levels of normalization.

**TODO**: Add schema concept

### Fact Table

The facts will be Timestamp + Symbol.
The Timestamp will be controlled by the intraday stock sampling frequency.

### Dimensions

The dimension of the fact table.

#### Stock

**TODO**

#### Twitter

**TODO**

#### News

**TODO**

#### Reddit

**TODO**

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
