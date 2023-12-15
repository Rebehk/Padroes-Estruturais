class Content:
    def display(self):
        pass


class RealContent(Content):
    def __init__(self, message):
        self.message = message
        self.load_message()

    def display(self):
        print(f"displaying message: {self.message}")

    def load_message(self):
        print("loading message...")


class ProxyContent(Content):
    def __init__(self, message):
        self.message = message
        self.real_content = None

    def display(self):
        if self.real_content is None:
            self.real_content = RealContent(self.message)
        self.real_content.display()


message1 = ProxyContent("text 4 test")
message2 = ProxyContent("testando proxy")
message1.display()
message1.display()
message2.display()
