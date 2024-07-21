import gradio as gr

def greet(name):
    return "Hello " + name + "!"

# Create the Gradio interface
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Launch the interface with default settings
demo.launch(share=True)
