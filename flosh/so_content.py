import bs4

class SOContent:
    """Class handling StackOverflow content."""
    def __init__(self, content: bytes):
        self.content = content
        self.soup = bs4.BeautifulSoup(content)

        self.infos = self.get_infos()
        self.bodies = self.get_bodies()

        self.info_accepted = self.get_info_accepted()

    def get_infos(self):
        infos = self.soup.find_all(
                "div",
                class_=lambda tag: tag and "answer js-answer" in tag)
        return infos

    def get_bodies(self):
        bodies = self.soup.find_all(
                "div",
                {"class": "answercell post-layout--right"})

        return bodies

    def get_info_accepted(self):
        info = self.soup.find_all(
                "div",
                {"class": "answer js-answer accepted-answer js-accepted-answer"})
        return info

    def has_accepted_answer(self):
        return len(self.info_accepted) > 0

    def position_of_accepted_answer(self):
        if self.has_accepted_answer():
            return int(self.info_accepted[0]["data-position-on-page"])
        else:
            return None

    def get_body_accepted(self):
        if self.has_accepted_answer():
            idx = self.position_of_accepted_answer()
            return self.bodies[idx]
        else:
            return None

    def get_text_accepted(self):
        if self.has_accepted_answer():
            body = self.get_body_accepted()
            text = body.find_all("div", {"class": "s-prose js-post-body"})[0]
            return text
        else:
            return None

    def __len__(self):
        return len(self.answer_list())
