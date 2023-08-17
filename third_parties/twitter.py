import os

# from datetime import datetime, timezone
import tweepy
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("twitter")

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )

    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)

    return tweet_list


def scraped_user_tweets():
    tweets_list = [
        {
            "text": "We introduced the ParentDocumentRetriever last week to strike a balance between:- using small chunks during indexing- passing larger chunks to the LLM great overview and diagram by @clusteredbytes",
            "url": "https://twitter.com/hwchase17/status/1691179199594364928",
        },
        {
            "text": "Excited to collaborate with @assaf_elovic to bring multiple LLM providers + an integration with LangSmith to GPT Researcher - the best research agent I know of! I'd highly encourage folks to try it out - it's very impressive",
            "url": "https://twitter.com/hwchase17/status/1691084934113288192",
        },
        {
            "text": "Love to see more apps adding support for open source models!",
            "url": "https://twitter.com/hwchase17/status/1691134497713229824",
        },
        {
            "text": "Excited to be speaking at AWS Gen AI day! Lot's of awesome integrations with AWS platform, was fun to highlight them all https://genaiday.virtual.awsevents.com/register?trk=57dbe57a-49c3-432b-a93b-0988d5011812&sc_channel=sm",
            "url": "https://twitter.com/hwchase17/status/1691101620376117248",
        },
        {
            "text": "Really cool to be able to see the logs & complex prompts that went into the Generative Agents simulation! https://smith.langchain.com/public/a4b09aaf-99ec-4ad0-a58c-2c07741f611b/r",
            "url": "https://twitter.com/hwchase17/status/1690830749921083392",
        },
    ]
    return tweets_list
