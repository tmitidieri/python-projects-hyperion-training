# Create a class definition for Email with 4 variables
class Email:
    def __init__(self, email_contents, from_address):
        self.has_been_read = False
        self.is_spam = False
        self.email_contents = email_contents
        self.from_address = from_address

    # Create functions for spam and email status
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

# Create a list to store the emails
inbox = []


def create_email():
    # Prompt the user to enter the email contents and sender's address
    email_contents = input("Enter the email contents: ")
    from_address = input("Enter the sender's email address: ")


# Insert a new email object
def add_email(email_contents, from_address):
    inbox.append(Email(email_contents, from_address))

# Returns the number of messages in the store
def get_count():
    return len(inbox)

# Returns the email at the chosen index and mark it as read
def get_email(index):
    email = inbox[index]
    email.mark_as_read()
    return email.email_contents

# Returns the emails that haven't been read
def get_unread_emails():
    unread_emails = []
    for email in inbox:
        if not email.has_been_read:
            unread_emails.append(email.email_contents)
            email.mark_as_read()
    return unread_emails

# Returns the messages marked as spam
def get_spam_emails():
    spam_emails = []
    for email in inbox:
        if email.is_spam:
            spam_emails.append(email.email_contents)
    return spam_emails

# Delete messages by chosen index
def delete(index):
    del inbox[index]



#An Email Simulation
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        pass
        get_unread_emails()
    elif user_choice == "create":
        pass
        create_email()
    elif user_choice == "send":
        pass
        add_email
    elif user_choice == "send":
        pass
        add_email
    elif user_choice == "mark spam":
        pass  # Place your logic here

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
