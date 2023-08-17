from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name:str)->str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """for {name_of_person} find twitter profile. I want you to get me a link to their twitter Profile Page, and extract from it their username. Agent Action Input - "{name_of_person} Twitter profile". After profile page url, extract username from profile url
       In Your Final answer only the person's username"""
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url,
            description="useful for when you need get the Twitter Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    
    return twitter_username