from crewai import Agent

from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


expert_travel_agent=Agent(
    role='Expert Travel Agent who makes major decisions',
    goal='create a 7 day itinery with detailed per day plans,include budget, packing suggestions and safety tips',
    verbose=True,
    memory=True,
    backstory=("Expert in travel plan and logistics and highly experienced in making travel plans and iteneraries"),
    tool=[],
    allow_delegation=True

)   
City_selection_expert=Agent(
    role='city selection expert',
    goal='select the best city based on the season,prices,weather and traveler interests',
    verbose=True,
    memory=True,
    backstory=("Expert in analysing travel data to pick the ideal destination"),
    tool=[],
    allow_delegation=True

)   

local_tour_guide=Agent(
    role='local tour guide',
    goal='knowledgeable local guide with information about its local customs,attractions and the city',
    verbose=True,
    memory=True,
    backstory=("Expert in making decions regarding the local destiantions"),
    tool=[],
    allow_delegation=True

)   







# def expert_travel_agent(self):
#     return Agent(
#         role="expert_travel_agent",
#         backstory= dedent(f"""Expert in tracel plan and logistics and highly experienced in making travel plans and iteneraries"""),
#         goal=dedent(f"""
#                     create a 7 day itinery with detailed per day plans,include budget,
#                     packing suggestions and safety tips
#                 """

#         ),
#         verbose= True,
#         llm=llm
#     )
# def city_selection_expert(self):
#     return Agent(
#         name="city_selection",
#         description=dedent(
#             """
#             This agent helps you select a city to travel to. It can provide information about popular cities around the world.
#             """
#         ),
#         agent_class=ChatOpenAI,
#         agent_kwargs={"model": "gpt-3.5-turbo", "engine": "davinci-codex"},
#     )
# def local_tour_guide(self):
#     return Agent(
#         name="local_tour_guide",
#         description=dedent(
#             """
#             This agent is a local tour guide. It can help you with information about local attractions, restaurants, and more.
#             """
#         ),
#         agent_class=ChatOpenAI,
#         agent_kwargs={"model": "gpt-3.5-turbo", "engine": "davinci-codex"},
#     )