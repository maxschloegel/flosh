import typing

import bs4

from .so_answer import SOAnswer


class SOContent:
    """Class handling StackOverflow content."""
    def __init__(self, content: bytes):
        self.content = content
        self.soup = bs4.BeautifulSoup(content)

        self.answers = self.get_answers()

        self.accepted_answer = self.get_accepted_answer()
        self.most_upvoted_answer = self.get_most_upvoted_answer()

    def get_answers(self):
        infos = self._get_infos()
        bodies = self._get_bodies()

        answers = [SOAnswer(info, body, pos) 
                   for pos, (info, body) in enumerate(zip(infos, bodies))]

        return answers

    def _get_infos(self):
        infos = self.soup.find_all(
                "div",
                class_=lambda tag: tag and "answer js-answer" in tag)
        return infos

    def _get_bodies(self):
        bodies = self.soup.find_all(
                "div",
                {"class": "answercell post-layout--right"})

        return bodies

    def get_most_upvoted_answer(self):
        return self.answers[0]

    def get_accepted_answer(self):
        for ans in self.answers:
            if ans.is_accepted():
                return ans
        else:
            return None

    def accepted_has_most_upvotes(self):
        return self.accepted_answer == self.most_upvoted_answer

    def has_answer(self):
        return len(self) > 0 

    def has_accepted_answer(self):
        return bool(self.get_accepted_answer())

    def __len__(self):
        return len(self.answers)
