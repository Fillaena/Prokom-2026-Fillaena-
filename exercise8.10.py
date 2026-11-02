def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)


texts = [
    "Hello, how are you?",
    "Hope your college life goes very well.",
    "See you in the semester break!.",
]
sent_messages = []

send_messages(texts, sent_messages)

print("\nIsi texts:", texts)
print("Isi sent_messages:", sent_messages)