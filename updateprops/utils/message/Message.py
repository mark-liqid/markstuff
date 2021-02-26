class Message(object):
    def __init__(self, text):
        self.print_message(text)

    @staticmethod
    def print_message(text):
        print('-' * 30)
        print(text)
        print('-' * 30)
