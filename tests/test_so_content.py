import pytest

import flosh

from helper_funcs import load_so_content


content_text = load_so_content()

def test_get_infos():
    so_content = flosh.SOContent(content_text)
    infos = so_content.get_infos()

    assert len(infos) == 8


