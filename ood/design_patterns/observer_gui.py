import tkinter as tk

from observer import EmailSubscriber, NewsPublisher, SMSSubscriber


class ObserverGUI:
    def __init__(self, root):
        self.publisher = NewsPublisher()
        self.email_subscriber = EmailSubscriber()
        self.sms_subscriber = SMSSubscriber()

        self.publisher.attach(self.email_subscriber)
        self.publisher.attach(self.sms_subscriber)

        root.title("Observer Pattern Demo")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Publish News", command=self.publish_news)
        self.button.pack(pady=5)

        self.email_label = tk.Label(
            root, text="Email Inbox:", anchor="w", justify="left"
        )
        self.email_label.pack(fill="x", padx=10)

        self.sms_label = tk.Label(
            root, text="SMS Messages:", anchor="w", justify="left"
        )
        self.sms_label.pack(fill="x", padx=10)

    def publish_news(self):
        message = self.entry.get()
        if message:
            self.publisher.notify(message)
            self.update_display()

    def update_display(self):
        email_text = "\n".join(self.email_subscriber.inbox)
        sms_text = "\n".join(self.sms_subscriber.messages)
        self.email_label.config(text=f"Email Inbox:\n{email_text}")
        self.sms_label.config(text=f"SMS Messages:\n{sms_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ObserverGUI(root)
    root.mainloop()
