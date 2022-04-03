from typing import Generator, Optional

import pytest

from reddit_sauce_harvester.meta import SortChoice
from reddit_sauce_harvester.reddit_api import RedditDesktopAPI

from .common import POST_DATA, POST_DATA_LIST, POST_ID_LIST, SUBREDDIT_NAME, TOKEN


@pytest.mark.parametrize("subreddit_name", [SUBREDDIT_NAME])
@pytest.mark.parametrize("token", [None, TOKEN])
@pytest.mark.parametrize("sort", list(SortChoice))
def test_reddit_desktop_api_get_subreddit_posts_success(
    subreddit_name: str,
    token: Optional[str],
    sort: SortChoice,
    register_mock_requests: Generator,  # pylint: disable=unused-argument
) -> None:
    api = RedditDesktopAPI()
    posts, response_token = api.get_subreddit_posts(subreddit_name, token, sort)

    assert list(posts) == POST_DATA_LIST
    assert response_token == token


@pytest.mark.parametrize("post_id", POST_ID_LIST)
def test_reddit_desktop_api_get_post_comments_success(
    post_id: str,
    register_mock_requests: Generator,  # pylint: disable=unused-argument
) -> None:
    api = RedditDesktopAPI()
    comments = api.get_post_comments(post_id)

    assert list(comments) == list(POST_DATA[post_id]["comments"].values())
