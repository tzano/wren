# How to train & build a News Chatbot

Wren is a tool that enables users to discover and explore daily news stories. The tool can monitor and capture news content from a list of news sources, use NLP technology to enrich news discovery, and store data to easily source and search the enriched news data through conversational interfaces. The general view of the system is depicted in Figure 1.

![ScreenShot](/docs/images/wren_news_analytics.png)
**Figure 1.** Wren Technical Architecture 

As part of the project, we built a News Chatbot that is able to understand the intentions behind the user's queries, and provide releavant news stories. However, Chatbots are only as good as the training they are given. Building a representative set of intents is an important process and one that requires iteration.

In order to determine the intents, we talked to a group of people to understand how they use home assistants (like Alexa, Google Home) to discover and explore news. At the end of the session, we came out with a generic scenario. On a specific time during the day, users look for News Content (`Articles`, `Podcasts`, `TV shows`) based on different factors (They look for a specific `Topic`, news in certain `Time` or `Place`, or articles that discusses a `Person`). Once they find the right headline, they select a content Item to read, listen or watch it. After interacting with the content, users try to bookmark it or share the content item on social platforms.

Based on this scenario, we summarized the set of intents that we built for our chatbot. We use [`Fountain`](https://github.com/tzano/fountain) a Natural Language Data Augmentation Tool for Conversational Systems to generate the training dataset.


If you are a researcher, a data journalist or a developer, you can directly download and use the [**News Chatbot Training Dataset**](https://github.com/tzano/wren/blob/master/wren/data/wren_utterances.json) or expand the `Fountain` template [that can be accessed here](https://github.com/tzano/wren/blob/master/wren/data/wren_training_gen_fountain.yaml) and add more intents in a way that meets your requirements. 

All the technical steps required to build and train the model are described [here](https://github.com/tzano/wren). We also included a containerized version of [the tool in this folder](https://github.com/tzano/wren/tree/master/docker). You can build it using [`docker-compose`](https://github.com/tzano/wren#getting-started). Figure 2. shows a screen shot of Wren Slack Chatbot.

![ScreenShot](/docs/images/wren_slack.png)
**Figure 2.** Wren Slack Chatbot

Below, you find a summary on all the intents used in the project. 

## Find News Content (articles/podcasts/TV shows) or filter based on `Time`, `Place`, `People` & `Topic`

### INTENT: findNewsContent

- **SLOTS**:
```
- findNewsContent_orgName (e.g.: CNN, BBC, Bloomberg, ..etc)
- findNewsContent_authorName (e.g.: Kate Adie, ..etc)
- findNewsContent_contentType  (e.g.: articles, podcasts, TV shows, TV programs)
- findNewsContent_locationName (e.g.: NYC, Alaska, .. etc)
- findNewsContent_spatialRelation (e.g.: nearby, .. etc)
- findNewsContent_userPlace (e.g.: town, .. etc)
- findNewsContent_topicName (e.g.: Sports, .. etc)
- findNewsContent_personName (e.g.: Barack Obama, .. etc)
- findNewsContent_eventName (e.g.: US Election, .. etc)
- findNewsContent_contentItemName (e.g.: Deporting Dreamers, .. etc)
- findNewsContent_time (e.g.: yesterday, .. etc)
- findNewsContent_selectCriteria (e.g.: first, latest, .. etc)
```

- **SAMPLES**:
- Search for news published by a News organization
```
- Hey, find out what's in the news on [BBC](findNewsContent_orgName)
- What's in the news on [BBC](findNewsContent_orgName)
- What is [BBC](findNewsContent_orgName) saying happened today
- What's happening in [New York City](findNewsContent_locationName), [BBC](findNewsContent_orgName)
- Search for [New York City](findNewsContent_locationName) news using [BBC](findNewsContent_orgName)
- What is [BBC](findNewsContent_orgName) saying about [US election](findNewsContent_eventName)
- Has [BBC](findNewsContent_orgName) been saying anything about [US election](findNewsContent_eventName)
- [US election](findNewsContent_eventName) is happening, what is [BBC](findNewsContent_orgName) saying
```

- Search for news published by a Journalist
```
- Search for [article](findNewsContent_contentType) written by [David Brooks](findNewsContent_authorName)
- What did [Thomas Friedman](findNewsContent_authorName) said about [US election](findNewsContent_eventName)
```


- Search for news based on type of content (Podcast, TV show, Video​)
```
- Search for [article](findNewsContent_contentType) news using [BBC](findNewsContent_orgName)
- What new [article](findNewsContent_contentType) is coming out this [week](findNewsContent_timeFrame)
- What's the news saying about [article](findNewsContent_contentType) today
- Has/Have [article](findNewsContent_contentType) been featured in the news recently
- Show me the news for [article](findNewsContent_contentType)
- What's [BBC](findNewsContent_orgName) saying about [article](findNewsContent_contentType)
- Which [podcast](findNewsContent_contentType) is worth listening to
- What good [articles](findNewsContent_contentType) are there
- Best [articles](findNewsContent_contentType) according to [BBC](findNewsContent_orgName)

```

- Search for news using the title of a content
```
- Is there anything new for ["Deporting Dreamers"](findNewsContent_contentItemName)
- Look up [Sports](findNewsContent_topicName) and tell me if there's anything from the past [3 days](findNewsContent_timeFrame)
- What is the news saying about [Sports](findNewsContent_topicName)
- Tell me what [New York Times](findNewsContent_orgName) has been saying about ["Deporting Dreamers"](findNewsContent_contentItemName)
- Find news about [Sports](findNewsContent_topicName)
- I am looking for an [article](findNewsContent_contentType) entitled ["Deporting Dreamers"](findNewsContent_contentItemName)
```

- Search for news in a specific Location
```
- What happened in [New York City](findNewsContent_locationName), [today](findNewsContent_timeFrame)
- [New York City](findNewsContent_locationName) news
- [New York City](findNewsContent_locationName) news from [BBC](findNewsContent_orgName)
- News for [New York City](findNewsContent_locationName) on [BBC](findNewsContent_orgName)
- What's going on in [New York City](findNewsContent_locationName)
- Find out what happened in [New York City](findNewsContent_locationName)
- Is [New York City](findNewsContent_locationName) in the news
```

- Search for news based on Time
```
- What's in the news from [March 10, 2018](findNewsContent_timeFrame) to [March 20, 2018](findNewsContent_timeFrame)
- Show me the news from [today](findNewsContent_timeFrame)
- News from [today](findNewsContent_timeFrame)
- [today](findNewsContent_timeFrame)'s news
- What happened in the news [today](findNewsContent_timeFrame)
```

- Search for news based on a specific Topic
```
- [US Elections](findNewsContent_topicName) news
- News about [US Elections](findNewsContent_topicName)
- Show me [US Elections](findNewsContent_topicName) news
- What's the news saying about [US Elections](findNewsContent_topicName)
- When was the last time [US Elections](findNewsContent_topicName) was in the news
- Has [BBC](findNewsContent_orgName) featured anything about [US Elections](findNewsContent_topicName)
- Has [US Elections](findNewsContent_topicName) been in the news recently
- What's happening with [US Elections](findNewsContent_topicName)
- Is the news saying anything about [US Elections](findNewsContent_topicName)
```

- Search for news that discusses a person
```
- News about [Barak Obama](findNewsContent_personName)
- [Barak Obama](findNewsContent_personName) news
- Show me what's in the news about [Barak Obama](findNewsContent_personName)
- What's [BBC](findNewsContent_orgName) saying about [Barak Obama](findNewsContent_personName)
- Has [Barak Obama](findNewsContent_personName) been in the news
- What's the latest news about [Barak Obama](findNewsContent_personName)
- Latest about [Barak Obama](findNewsContent_personName)
- Has [BBC](findNewsContent_orgName) said anything about [Barak Obama](findNewsContent_personName)
- What's going on with [Barak Obama](findNewsContent_personName)
- Did anything happen with [Barak Obama](findNewsContent_personName)
- Has [Barak Obama](findNewsContent_personName) been in the news recently
- Spoiler free news for [Barak Obama](findNewsContent_personName)
- [Barak Obama](findNewsContent_personName) news, no spoilers
```

- Search for news that discusses an event.
```
- What's new about [US election](findNewsContent_eventName)
- Search the news for [US election](findNewsContent_eventName)
- Has the news said anything about [US election](findNewsContent_eventName)
- What's [BBC](findNewsContent_orgName) have to say about [US election](findNewsContent_eventName)
- Has [US election](findNewsContent_eventName) been in the news lately
- Latest news on [US election](findNewsContent_eventName)
- Look up the latest about [US election](findNewsContent_eventName)
- News about [US election](findNewsContent_eventName)
- What's happening with [US election](findNewsContent_eventName)
- Is there anything new about [US election](findNewsContent_eventName)
- Show me everything about [US election](findNewsContent_eventName)
- New posts about [US election](findNewsContent_eventName)
- I am looking for an [article](findNewsContent_contentType) entitled [“Deporting Dreamers”](findNewsContent_contentItemName)
```

## Select a content Item

### INTENT: getContentInfo
- **SLOTS**:
```
- getContentInfo_selectCriteria (e.g.: Who, when)
- getContentInfo_contentItemName (e.g.: Deporting Dreamers, .. etc)
- getContentInfo_contentType (e.g.: articles, podcasts, TV shows, TV programs)

```

- **SAMPLES**:
```
- [What](getContentInfo_selectCriteria) is the title of the [article](getContentInfo_contentType) 
- [Where](getContentInfo_selectCriteria)  did this [article](getContentInfo_contentType) has been published
- [When](getContentInfo_selectCriteria)  did this [article](getContentInfo_contentType) come out
- [Who](getContentInfo_selectCriteria)  has been mentioned in this [article](getContentInfo_contentType) 
- [What](getContentInfot_selectCriteria)  are the places that have been mentioned in this [article](getContentInfo_contentType) 
- [Who](getContentInfo_selectCriteria)  published this [article](getContentInfo_contentType) 
- [Who](getContentInfo_selectCriteria)  published this [article](getContentInfo_contentType) 
- [What](getContentInfo_selectCriteria)  is the topic covered in this [article](getContentInfo_contentType)

- Where did this [article](getContentInfo_contentType) has been published
```


### INTENT: getHeadlines
- **SLOTS**:
```
- getHeadlines_contentType 
- getHeadlines_selectCriteria
- getHeadlines_orgName
```

- **SAMPLES**:
```
- Give me headlines
- Give me briefing
- What are the [latest](getHeadlines_selectCriteria) headlines 
- What are the [last](getHeadlines_selectCriteria) headline from [BBC](getHeadlines_orgName)
- Give me summary of [this](getHeadlines_selectCriteria) [article](getHeadlines_contentType) 
```

## Interact (read, listen or watch) with a content Item

### INTENT: readingArticle
- **SLOTS**:
```
- readArticle_command
- readArticle_contentItemName
- readArticle_position
- readArticle_selectCriteria
- readArticle_contentType

```

- Start reading article
```
- Start reading [this](readArticle_selectCriteria)  [article](readingArticle_contentType) 
- [Read](readArticle_command) [this](readArticle_selectCriteria)  [article](readArticle_contentType) 
- [Read](readArticle_command) [article](readArticle_contentType) ["Deporting Dreamers"](readArticle_contentItemName)
```

- Resume reading article
```
- [Resume](readArticle_command) reading [this](readArticle_selectCriteria)  [article](readArticle_contentType) 
- [Resume](readArticle_command) reading [article](readArticle_contentType) ["Deporting Dreamers"](readArticle_contentItemName)
 
```

- Pause reading article

```
- [Suspend](readArticle_command) reading [this](readArticle_selectCriteria) [article](readArticle_contentType) 
- [Suspend](readArticle_command) reading [article](readArticle_contentType) ["Deporting Dreamers"](readArticle_contentItemName)

```

- Stop reading article

```
- [Stop](readArticle_command) reading [this](readArticle_selectCriteria) [article](readArticle_contentType) 
- [Stop](readArticle_command) reading [article](stopReadingArticle_contentType) ["Deporting Dreamers"](readArticle_contentItemName)

```


### INTENT: listenPodcast
- **SLOTS**:
```
- listenPodcast_command
- listenPodcast_contentItemName
- listenPodcast_position
- listenPodcast_selectCriteria
- listenPodcast_contentType
```

- Start listening podcast
```
- [start](listenPodcast_command) listening to [this](listenPodcast_selectCriteria) [podcast](listenPodcast_contentType) 
- [start](listenPodcast_command) listening [podcast](listenPodcast_contentType) ["The Daily"](listenPodcast_contentItemName)

```

- Resume listening podcast
```
- [resume](listenPodcast_command) listening to [this](listenPodcast_selectCriteria) [podcast](listenPodcast_contentType) 
- [resume](listenPodcast_command) listening [podcast](listenPodcast_contentType) ["The Daily"](listenPodcast_contentItemName)

```

- Pause listening podcast
```
- [suspend](listenPodcast_command) listening to [this](listenPodcast_selectCriteria) [podcast](listenPodcast_contentType) 
- [suspend](listenPodcast_command) listening [podcast](listenPodcast_contentType) ["The Daily"](listenPodcast_contentItemName)

```

- Stop listening podcast
```
- [stop](listenPodcast_command) listening to [this](listenPodcast_selectCriteria) [podcast](listenPodcast_contentType) 
- [stop](listenPodcast_command) listening [article](listenPodcast_contentType) ["The Daily"](listenPodcast_contentItemName)
```



### INTENT: watchVideo
- **SLOTS**:
```
- watchVideo_command
- watchVideo_contentItemName
- watchVideo_position
- watchVideo_selectCriteria
- watchVideo_contentType
```

- Start watching video

```
- [start](watchVideo_command) watching [this](watchVideo_selectCriteria) [TV show](watchVideo_contentItemName)
```

- Resume watching video
```
- [resume](watchVideo_command) watching [this](watchVideo_selectCriteria) [TV show](watchVideo_contentType) 
- [resume](watchVideo_command) watching [video](watchVideo_contentType) ["LastWeekTonight"](watchVideo_contentItemName)

```

- Pause watching video
```
- [suspend](watchVideo_command) watching [this](watchVideo_selectCriteria) [TV show](watchVideo_contentType) 
- [suspend](watchVideo_command) watching [video](watchVideo_contentType) ["LastWeekTonight"](watchVideo_contentItemName)

```

- Stop watching video
```
- [stop](watchVideo_command) watching [this](watchVideo_selectCriteria) [TV show](watchVideo_contentType) 
- [stop](watchVideo_command) watching [video](watchVideo_contentType) ["LastWeekTonight"](watchVideo_contentItemName)

```


## Engage (like, bookmark, add to a list ) with the content Item.


### INTENT: addContentItemToCollection
- **SLOTS**:
```
- addContentItemToCollection_collectionName
- addContentItemToCollection_contentItemName
- addContentItemToCollection_contentType
- addContentItemToCollection_topicName
- addContentItemToCollection_selectCriteria
- addContentItemToCollection_userOwner
```

- **SAMPLES**:
```
- Please add the [article](addContentItemToCollection_contentType) ["Deporting Dreamers"](addContentItemToCollection_contentItemName) to ["Morning Read"](addContentItemToCollection_collectionName) list 
- Include the [article](addContentItemToCollection_contentType) ["Deporting Dreamers"](addContentItemToCollection_contentItemName) to ["Morning Read"](addContentItemToCollection_collectionName) list 
- Add another [article](addContentItemToCollection_contentType) ["Deporting Dreamers"](addContentItemToCollection_contentItemName) to ["Morning Read"](addContentItemToCollection_collectionName) collection 
- Add the [article](addContentItemToCollection_contentType) ["Deporting Dreamers"](addContentItemToCollection_contentItemName) to [my](addContentItemToCollection_userOwner) ["Morning Read"](addContentItemToCollection_collectionName) collection
- Add the [article](addContentItemToCollection_contentType) ["Deporting Dreamers"](addContentItemToCollection_contentItemName) to ["Morning Read"](addContentItemToCollection_collectionName)
- Add ["Sport"](addContentItemToCollection_topicName) [articles](addContentItemToCollection_contentType) to ["Morning Read"](addContentItemToCollection_collectionName) collection 
- Add [latest](addContentItemToCollection_selectCriteria) ["Sport"](addContentItemToCollection_topicName) [videos](addContentItemToCollection_contentType) to ["Friday Read"](addContentItemToCollection_collectionName) collection 

```

### INTENT: bookmarkContentItem
- **SLOTS**:
```
- bookmarkContentItem_contentItemName
- bookmarkContentItem_selectCriteria
- bookmarkContentItem_contentType
```

- **SAMPLES**:
```
- bookmark [this](bookmarkContentItem_selectCriteria) [TV show](bookmarkContentItem_contentType) 
- bookmark [article](bookmarkContentItem_contentType) entitled [“Deporting Dreamers”](bookmarkContentItem_contentItemName)
- bookmark [“LastWeekTonight”](bookmarkContentItem_contentItemName) [video](bookmarkContentItem_contentType)

```

### INTENT: rateContentItem
- **SLOTS**:
```
- rateContentItem_contentItemName
- rateContentItem_selectCriteria
- rateContentItem_contentType
- rateContentItem_ratingValue
```

- **SAMPLES**:
```
- rate [“LastWeekTonight”](rateContentItem_contentItemName) [video](rateContentItem_contentType) [5 ](rateContentItem_ratingValue) stars
```

### INTENT: shareContentItem
- **SLOTS**:
```
- shareContentItem_contentItemName
- shareContentItem_selectCriteria
- shareContentItem_contentType
- shareContentItem_socialNetwork
```

- **SAMPLES**:
```
- share [article](shareContentItem_contentType) entitled [“Deporting Dreamers”](shareContentItem_contentItemName) on [Twitter](shareContentItem_socialNetwork)
```


### INTENT: emailContentItem
- **SLOTS**:
```
- emailContentItem_contentItemName
- emailContentItem_contentType
- emailContentItem_selectCriteria
- emailContentItem_recipient
```

- **SAMPLES**:
```
- Send [this](emailContentItem_selectCriteria) [article](emailContentItem_contentType) entitled [“Deporting Dreamers”](emailContentItem_contentType) to [John](emailContentItem_receipent)
```

### INTENT: favoriteContentItem
- **SLOTS**:
```
- favoriteContentItem_contentItemName
- favoriteContentItem_contentType
- favoriteContentItem_selectCriteria
```

- **SAMPLES**:
```
- Favorite [this](favoriteContentItem_selectCriteria) [article](favoriteContentItem_contentType) entitled [“Deporting Dreamers”](favoriteContentItem_contentItemName)
  Favorite [this](favoriteContentItem_selectCriteria) [article](favoriteContentItem_contentType)

```
