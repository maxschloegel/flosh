import pytest

import flosh

from helper_funcs import load_so_content


content_text = load_so_content()
so_content = flosh.SOContent(content_text)


def test_is_accepted():
    ans_acc = so_content.answers[1]

    # check not accepted answers
    ans_most_upvotes = so_content.answers[0]
    ans_few_upvotes = so_content.answers[-1]

    assert ans_acc.is_accepted()
    assert not ans_most_upvotes.is_accepted()
    assert not ans_few_upvotes.is_accepted()


def test_get_text():
    ans = so_content.answers[0]
    text = ans.text  # in byte
    print(text)

    assert text
    assert len(text) == 7
    assert text.text.startswith("\nIf you're writing a project")


def test_get_markdown_text():
    ans = so_content.answers[0]
    md_text = ans.get_markdown_text()

    assert md_text
    assert len(md_text) == 574
    assert md_text.startswith("\nIf you're writing a project")
