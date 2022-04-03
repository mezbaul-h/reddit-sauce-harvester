import pytest

from reddit_sauce_harvester.utils import deep_get

_SAMPLE_DATA = {"a": {"b": "c"}}


@pytest.mark.parametrize(
    "data, keys, default, expected_output",
    [
        (_SAMPLE_DATA, "a.b", None, "c"),
        (_SAMPLE_DATA, "a.b.c", None, None),
        (_SAMPLE_DATA, "a.b.c", "d", "d"),
        (_SAMPLE_DATA, "a.b.c", [], []),
    ],
)
def test_deep_get(data, keys, default, expected_output):
    assert deep_get(data, keys, default=default) == expected_output
