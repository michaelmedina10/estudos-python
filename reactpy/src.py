from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

@component
def helloWorld():
    return html.h1("Quem sou eu!")

@component
def helloWorld2():
    return html.h2("Sou outra funcao e agr???")

@component
def PrintButton(display_text, message_text):
    def handle_event(_):
        print(message_text)

    return html.button({"on_click": handle_event}, display_text)

@component
def todo():
    return html.section(helloWorld(),
                        helloWorld2(),
                        PrintButton("SOU LABEL DO BOTAO", "SOU BOTAO TBM"))

app = FastAPI()

configure(app, todo)
