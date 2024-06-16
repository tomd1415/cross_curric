from openai import AssistantEventHandler
from typing_extensions import override

class EventHandler(AssistantEventHandler):
    def __init__(self, html_file):
        super().__init__()
        self.html_file = html_file

    @override
    def on_text_created(self, text) -> None:
        print("\nassistant > ", end="\n", flush=True)

    @override
    def on_text_delta(self, delta, snapshot):
        self.html_file.write(delta.value)

    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print("\n\noutput >", end="\n", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)
