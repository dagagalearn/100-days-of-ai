from google.colab import userdata
import os

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature=0.7)
my_prompt = input("What is in your mind.... ")
prompt = PromptTemplate.from_template(my_prompt)
chain = prompt | llm | StrOutputParser()
result = chain.invoke({})

print(f"Question: {my_prompt}")
print(f"Answer: {result}")

