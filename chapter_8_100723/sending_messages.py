msgs = ['hey', 'hi', 'how are you?', 'ungabunga baby']

def show_messages(messages):
	for msg in msgs:
		print(msg)

sent_messages = []
def send_messages(messages):
	while messages:
		current_message = messages.pop(0)
		print(current_message)
		sent_messages.append(current_message)
send_messages(msgs)
print(msgs)
print(sent_messages)