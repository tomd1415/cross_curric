from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
    name="Curriculm Analyser",
    model="gpt-4o",
    instructions="Please find potential cross-curriculum links between Computing and Art for year 7 from the curriculum documents.", # Reference documents: file-kXWgwujMivMUlEhM9KfevPgc file-vGSqdCxfEIy4anUEMEpzyxrs file-KKTK4cKnnug9NkqVXBpZTsCB"},
    tools=[{"type": "file_search"}],
    
)
#print(assistant.choices[0].message)
