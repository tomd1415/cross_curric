import os
from openai import OpenAI
from xhtml2pdf import pisa
from config import Config
from event_handler import EventHandler

def convert_html_to_pdf(source_html, output_filename):
    """Convert HTML content to PDF."""
    with open(output_filename, "w+b") as output_file:
        pisa_status = pisa.CreatePDF(source_html, dest=output_file)
    return pisa_status.err

def generate_html_report():
    """Generate HTML report using OpenAI API."""
    client = OpenAI(api_key=Config.API_KEY)
    assistant = client.beta.assistants.retrieve(Config.ASSISTANT_ID)
    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [Config.VECTOR_STORE_ID]}}
    )
    thread = client.beta.threads.create()

    with open(Config.HTML_FILENAME, "w") as html_file:
        html_file.write(Config.STYLE)
        event_handler = EventHandler(html_file)
        
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant.id,
            max_prompt_tokens=2200,
            max_completion_tokens=2500,
            instructions=f"""Please look through the files in the vector store and find cross-curriculum links between {Config.SUBJECT1} and {Config.SUBJECT2}. I would like the report to be organised by year group with a two sentence summary of the links at the start and then details about the links as bullet points below. I would like it grouped by term within year group as in the examples. I would like you to look at the current {Config.SUBJECT2} curriculum as well as the {Config.SUBJECT1} curriculum to find where there could be links in the same term. I would like as many links as possible for each term and I would like it formatted like the examples. Then I would like a short paragraph explaining how more cross-curricular links could be made. This should be about one page per year group in total length. The HTML used to markup the text is not for use in a web pag and therefore only needs the tags that are in the examples. No other tags should be used. Please just show me {Config.YEAR_GROUP} for now. I will come back for the other year groups. Please produce this is a format as close to the examples as you can. Below are the example outputs:""" + Config.PROMPT_EXAMPLES,
            event_handler=event_handler,
        ) as stream:
            stream.until_done()

        html_file.write("</html>")

def main():
    """Main function to generate HTML report and convert it to PDF."""
    generate_html_report()
    
    with open(Config.HTML_FILENAME, "r") as html_file:
        html_content = html_file.read()

    convert_html_to_pdf(html_content, Config.PDF_FILENAME)
    print(f"Finished! PDF file created: {Config.PDF_FILENAME}")

if __name__ == "__main__":
    main()
