from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import requests
import re

load_dotenv()

def calculator_tool(query: str) -> str:
    nums = re.findall(r"-?\d+(?:\.\d+)?", query)
    if len(nums) >= 2:
        a = float(nums[0])
        b = float(nums[1])
        result = a + b
        if result.is_integer():
            result = int(result)
        return f"✅ The sum of {a} & {b} = {result}"
    return "No numbers found to add."

def get_weather(city: str) -> str:
    latitude, longitude = 24.7136, 46.6753  # الرياض
    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        )
        data = response.json()
        temp = data["hourly"]["temperature_2m"][0]
        return f"The current temperature in {city} is {temp}°C"
    except:
        return "Sorry, I couldn't fetch the weather data."
    
llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use for math operations between numbers."
    ),
    Tool(
        name="Weather",
        func=get_weather,
        description="Use to get the current temperature in a specified city."
    ),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="conversational-react-description",
    memory=memory,
    verbose=True,
)
if __name__ == "__main__":
    question = "what is the weather in Riyadh?"
    print("Q:", question)
    print(f"\nresult: {agent.run(question)}")