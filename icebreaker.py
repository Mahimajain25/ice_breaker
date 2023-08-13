from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agents import lookup as linkedin_lookup_agent
from third_parties.twitter import scrape_user_tweets
from agents.twitter_lookup_agents import lookup as twitter_lookup_agent

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY_"]

name = "Harison Chase"

if __name__ == "__main__":
    print("Hello LangChain!")

    linkedin_profile_url = linkedin_lookup_agent(name = name)
    LinkedIn_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    twitter_username = twitter_lookup_agent(name = name)
    tweets = scrape_user_tweets(username=twitter_username,num_tweets=5)
    summary_template = """
        given the Linkedin informtion {linked_information} and twitter informaton {twitter_information}about a person from I want you to create:
        1. a short summary 
        2. two intersting fact about them 
        3. A topic that may interest them
        4. 2 Creative Ice breaker to open a conversation with them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linked_information","twitter_information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo"
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(linked_information=LinkedIn_data,twitter_information=tweets))
