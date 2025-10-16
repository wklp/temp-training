from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import re

# تحميل متغيرات البيئة من ملف .env -openai api key-
load_dotenv()

def calculator_tool(query: str) -> str:
    # استخراج الأرقام من النص
    nums = re.findall(r"-?\d+(?:\.\d+)?", query)
    if len(nums) >= 2:
        a = float(nums[0])
        b = float(nums[1])
        result = a + b
        if result.is_integer():
            result = int(result)
        return f"the sum of {a} & {b} = {result}"
    return "There is no numbers to add"

# تهيئة نموذج اللغة
llm = ChatOpenAI(temperature=0)

# تعريف الأداة
tools = [
    Tool(
        name="sum-function",
        func=calculator_tool,
        description="useful for when you need to add two numbers together. The input to this tool should be a string containing two numbers to add, for example: 'What is 5.2 + 3?'"
    )
]

# تهيئة الايجنت
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
    )

if __name__ == "__main__":
    question = "What is 10+3.2 ?"
    print("Q:", question)
    print(f"\nresult: {agent.run(question)}")