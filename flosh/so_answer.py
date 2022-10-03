import markdownify


class SOAnswer:
    def __init__(self, info, body, pos):
        self.info = info
        self.body = body
        self.pos = pos

        self.text = self.get_text()

    def get_text(self):
        text = self.body.find_all("div", {"class": "s-prose js-post-body"})[0]
        return text

    def get_markdown_text(self):
        return markdownify.markdownify(self.text.renderContents())

    def is_accepted(self):
        return "accepted-answer" in self.info["class"]

