class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

class MessageStack:
    def __init__(self):
        self.stack = []

    def send_message(self, sender, recipient, content):
        message = Message(sender, recipient, content)
        self.stack.append(message)
        print(f"Message from {sender} to {recipient} added to the message stack.")

    def retrieve_messages(self):
        if not self.stack:
            print("Message stack is empty.")
        else:
            latest_message = self.stack[-1]  # Get the latest message (last element of the stack)
            print(f"Latest message: From: {latest_message.sender}, To: {latest_message.recipient}, Content: {latest_message.content}")

    def retrieve_all_messages(self):
        if not self.stack:
            print("Message stack is empty.")
        else:
            print("Retrieving all messages from the message stack:")
            for i, message in enumerate(reversed(self.stack)):
                print(f"{i+1}. From: {message.sender}, To: {message.recipient}, Content: {message.content}")

    def delete_messages(self):
        if not self.stack:
            print("Message stack is already empty.")
        else:
            self.stack.clear()
            print("All messages have been deleted.")

    def delete_message(self, index):
        if not self.stack:
            print("Message stack is already empty.")
        elif index < 1 or index > len(self.stack):
            print("Invalid message index.")
        else:
            deleted_message = self.stack.pop(-index)
            print(f"Message {index} has been deleted: From {deleted_message.sender} to {deleted_message.recipient}, Content: {deleted_message.content}")

    def pop_message(self):
        if not self.stack:
            print("Message stack is empty.")
        else:
            popped_message = self.stack.pop()
            print(f"Message popped: From {popped_message.sender} to {popped_message.recipient}, Content: {popped_message.content}")

    def get_num_messages(self):
        return len(self.stack)

    def display_menu(self):
        print("\nMessage Stack Menu:")
        print("1. Send Message")
        print("2. Retrieve Latest Message")
        print("3. Retrieve All Messages")
        print("4. Delete All Messages")
        print("5. Delete a Message")
        print("6. Pop Message")
        print("7. Number of Messages")
        print("8. Quit")

# Create a message stack
message_stack = MessageStack()

while True:
    message_stack.display_menu()
    try:
        option = int(input("Enter an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if option == 1:
        sender = input("Enter the sender's name: ")
        recipient = input("Enter the recipient's name: ")
        content = input("Enter the message content: ")
        message_stack.send_message(sender, recipient, content)

    elif option == 2:
        message_stack.retrieve_messages()

    elif option == 3:
        message_stack.retrieve_all_messages()

    elif option == 4:
        while True:
            confirm = input("Are you sure you want to delete all messages? (yes/no): ").lower()
            if confirm == "yes":
                message_stack.delete_messages()
                break
            elif confirm == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    elif option == 5:
        while True:
            try:
                index = int(input("Enter the index of the message to delete: "))
                if index < 1:
                    print("Invalid index. Index must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        message_stack.delete_message(index)

    elif option == 6:
        message_stack.pop_message()

    elif option == 7:
        print(f"Number of messages in the stack: {message_stack.get_num_messages()}")

    elif option == 8:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
