from services.langchain_utils import get_llm

llm = get_llm()
print(llm.invoke("What is Autopilot CEO?"))
