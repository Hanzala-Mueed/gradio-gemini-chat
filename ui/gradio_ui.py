import gradio as gr

from auth.login import authenticate
from services.chat_service import ask_question


def login(username, password):

    if authenticate(username, password):
        return "Login Successful"

    return "Invalid Credentials"


def chat_function(message, history):

    response = ask_question(message)
    #history.append((message, response))
    
    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    return history, history


with gr.Blocks() as demo:

    gr.Markdown("# AI PDF Chatbot Vol 1")
    with gr.Tab("Login"):

        username = gr.Textbox(label="Username")

        password = gr.Textbox(
            label="Password",
            type="password"
        )

        login_btn = gr.Button("Login")

        login_output = gr.Textbox(label="Status")

        login_btn.click(
            fn=login,
            inputs=[username, password],
            outputs=login_output
        )

    with gr.Tab("Chatbot"):

        chatbot = gr.Chatbot(type="messages")

        msg = gr.Textbox(
            label="Ask Question"
        )

        send_btn = gr.Button("Send")

        state = gr.State([])

        send_btn.click(
            fn=chat_function,
            inputs=[msg, state],
            outputs=[chatbot, state]
        )


def create_ui():

    return demo