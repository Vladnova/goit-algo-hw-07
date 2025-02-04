class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає відповідь до коментаря"""
        self.replies.append(reply)

    def remove_reply(self):
        """Видаляє коментар, залишаючи замість нього стандартне повідомлення"""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        """Рекурсивно виводить коментар та всі його відповіді"""
        print("    " * indent + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 1)


# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
