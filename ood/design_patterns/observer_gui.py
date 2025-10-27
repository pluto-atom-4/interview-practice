import tkinter as tk

from observer import EmailSubscriber, NewsPublisher, SMSSubscriber


class ObserverGUI:
    def __init__(self, root):
        self.publisher = NewsPublisher()
        self.email_subscriber = EmailSubscriber()
        self.sms_subscriber = SMSSubscriber()

        root.title("Observer Pattern Demo")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.email_var = tk.BooleanVar(value=True)
        self.sms_var = tk.BooleanVar(value=True)

        self.email_check = tk.Checkbutton(
            root,
            text="Email Subscriber",
            variable=self.email_var,
            command=self.toggle_email,
        )
        self.sms_check = tk.Checkbutton(
            root, text="SMS Subscriber", variable=self.sms_var, command=self.toggle_sms
        )
        self.email_check.pack()
        self.sms_check.pack()

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

        self.publisher.attach(self.email_subscriber)
        self.publisher.attach(self.sms_subscriber)

    def toggle_email(self):
        if self.email_var.get():
            self.publisher.attach(self.email_subscriber)
        else:
            self.publisher.detach(self.email_subscriber)

    def toggle_sms(self):
        if self.sms_var.get():
            self.publisher.attach(self.sms_subscriber)
        else:
            self.publisher.detach(self.sms_subscriber)

    def publish_news(self):
        message = self.entry.get()
        if message:
            self.publisher.notify(message)
            self.animate_display()

    def animate_display(self):
        self.email_lines = self.email_subscriber.inbox.copy()
        self.sms_lines = self.sms_subscriber.messages.copy()
        self.email_index = 0
        self.sms_index = 0
        self.email_text = ""
        self.sms_text = ""
        self.animate_email()
        self.animate_sms()

    def animate_email(self):
        if self.email_index < len(self.email_lines):
            line = self.email_lines[self.email_index]
            self.email_text += line + "\n"
            self.email_label.config(text=f"Email Inbox:\n{self.email_text}")
            self.email_index += 1
            self.email_label.after(300, self.animate_email)

    def animate_sms(self):
        if self.sms_index < len(self.sms_lines):
            line = self.sms_lines[self.sms_index]
            self.sms_text += line + "\n"
            self.sms_label.config(text=f"SMS Messages:\n{self.sms_text}")
            self.sms_index += 1
            self.sms_label.after(300, self.animate_sms)


if __name__ == "__main__":
    root = tk.Tk()
    app = ObserverGUI(root)
    root.mainloop()
