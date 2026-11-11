import os
import gradio as gr

def chatbot(message, history):
    message = message.lower()

    if "laptop" in message:
        return "We have laptops available. Starting price is 80,000 PKR."
    elif "mouse" in message:
        return "Computer mouse price is 4,000 PKR."
    elif "headphone" in message:
        return "Headphone price is 6,000 PKR."
    elif "delivery" in message:
        return "Free delivery in Rawalpindi and Islamabad."
    elif "timing" in message:
        return "Monday to Saturday, 10 AM to 10 PM."
    else:
        return "Welcome to TechZone Store! Ask about laptops, mouse, headphones or delivery."

demo = gr.ChatInterface(
    fn=chatbot,
    title="TechZone Store Assistant",
    description="Your online shopping assistant"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000))
    )
