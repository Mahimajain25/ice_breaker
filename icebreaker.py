from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agents import lookup as linkedin_lookup_agent

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY_"]

if __name__ == "__main__":
    print("Hello LangChain!")

    linkedin_profile_url = linkedin_lookup_agent(name = "Eden Macro udemy")

    summary_template = """
        given the informtion {information} about a person from I want you to create:
        1. a short summary 
        2. two intersting fact about them 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo"
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    LinkedIn_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    print(chain.run(information=LinkedIn_data))
