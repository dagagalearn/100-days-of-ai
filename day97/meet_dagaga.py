import os
from google.colab import userdata
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
text_data = """
FULL NAME: Dagaga Addisu
NICKNAME/PREFERRED NAME: Tesla/Nikola Tesla
AGE: 18(born Feb 29,2008)
LOCATION: Ethiopia
OCCUPATION: Student
SCHOOL/UNIVERSITY: Wollega University Special Boarding Secondary School(a.k.a WUSBSS)
INTERESTS: Coding, Learning Science, Solving Problems, Watching Movies
TECH STACK: HTML/CSS/JS, Python, tensorflow,Basic ML tools
PERSONALITY: introverted(mostly) and curious
GOALS: becoming what I want, when I want , the way I want , irrespective conditions
FUN FACTS: I was born on  Leap day so I use Ethiopian Calander to celebrate most of my birthdays
CONTACT: dagagaaddisulearn@gmail.com|dagagathecoder@gmail.com|t.me/@et_tesla
FAVORITES: IRON MAN, INTERSTELLAR, OPPENHEIMER
DAILY ROUTINE: depends on the day and works that need to be completed(variable)
WHAT YOU'RE LEARNING NOW: Currently taking two courses: AI and Calculus
"""

document = [Document(page_content=text_data)]
splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=50)
chunks = splitter.split_documents(document)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature=0.3)

vectorstore = Chroma.from_documents(chunks,embeddings)
template = """"
Here is some information about me(Dagaga Addisu), use the information to answer customer's question about me. If you don't know the answer
tell the customer to ask me instead.

Question: {question}
Context: {context}
Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
retrivier = vectorstore.as_retriever()
chain = prompt | llm | StrOutputParser()

def ask_question(question):
  docs = retrivier.invoke(question)
  context = "\n\n".join([doc.page_content for doc in docs])
  answer = chain.invoke({"question": question,"context": context})

  print("="*50)
  print(f"Q: {question}")
  print(f"A: {answer}")
  print("="*50)

ask_question("How can I get Dagaga?")
