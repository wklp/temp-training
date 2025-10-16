from langchain.agents import Tool, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import re

# تحميل متغيرات البيئة
load_dotenv()

# 🧮 Tool 1: Calculator
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

# 🔍 Tool 2: Search (محاكاة بحث)
def search_tool(query: str) -> str:
    return f"🔎 Simulated search results for '{query}'."

# 🌐 Tool 3: Translator
def translator_tool(query: str) -> str:
    return f"🌍 Translated '{query}' to arabic (simulation)."

# 🧠 إعداد الذاكرة
memory = ConversationBufferMemory(memory_key="chat_history")

# 🧰 الأدوات
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use for math operations between numbers."
    ),
    Tool(
        name="Search",
        func=search_tool,
        description="Use for general knowledge or recent events."
    ),
    Tool(
        name="Translator",
        func=translator_tool,
        description="Use to translate Arabic sentences into English."
    ),
]

# 🤖 إعداد النموذج
llm = ChatOpenAI(temperature=0)

# 🧩 إنشاء Agent محادثي (يدعم التذكّر)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True,
    memory=memory
)

# 🚀 تجربة المحادثة
if __name__ == "__main__":
    print("\nQ1:", "my name is abdullah")
    print(agent.run("my name is abdullah"))

    print("\nQ2:", "i am 21 years old")
    print(agent.run("i am 21 years old"))

    print("\nQ3:", "What is 2 + 5")
    print(agent.run("What is 2 + 5"))

    print("\nQ4:", "how old am i?")
    print(agent.run("how old am i?"))
