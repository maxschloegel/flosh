import pytest

import flosh

from helper_funcs import load_so_content


content_text = load_so_content()
so_content = flosh.SOContent(content_text)


def test_get_answers():
    answers = so_content.get_answers()

    assert len(answers) == 8
    assert all([isinstance(ans, flosh.SOAnswer) for ans in answers])


def test_get_most_upvoted_answer():
    ans = so_content.get_most_upvoted_answer()

    assert ans.pos == 0 


def test_accepted_has_most_upvotes():
    #TODO: check for example with accepted answer has most upvotes
    assert not (so_content.accepted_has_most_upvotes())


def test_has_accepted_answer():
    #TODO: check for example with no accepted answer
    assert so_content.has_accepted_answer()


def test_has_answer():
    #TODO: check for example with no accepted answer
    assert so_content.has_answer()


def get_accepted_answer():
    ans = so_content.get_accepted_answer()

    assert ans
    assert ans.pos == 1


def test_len():
    assert len(so_content) == 8

