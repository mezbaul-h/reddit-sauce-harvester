import itertools
from test.common import POST_DATA, SUBREDDIT_NAME, TOKEN
from typing import Generator

import pytest
import responses
from responses import matchers

from reddit_sauce_harvester.meta import SortChoice
from reddit_sauce_harvester.reddit_api import RedditDesktopAPI


@pytest.fixture
def register_mock_requests() -> Generator:
    with responses.RequestsMock(assert_all_requests_are_fired=False) as mock:
        for sort, token in itertools.product(*[list(SortChoice), [None, TOKEN]]):
            match_params = {
                **RedditDesktopAPI.COMMON_QUERY_PARAMS,
            }
            sort = sort.value

            if sort.startswith("top_"):
                match_params["sort"] = "top"
                match_params["t"] = sort.split("_")[-1]
            else:
                match_params["sort"] = sort

            if token:
                match_params["after"] = token

            mock.add(
                method=responses.GET,
                url=f"{RedditDesktopAPI.SUBREDDIT_URL_BASE}/{SUBREDDIT_NAME}",
                json={
                    "posts": POST_DATA,
                    "token": token,
                },
                match=[matchers.query_param_matcher(match_params)],
            )

        for key, value in POST_DATA.items():
            mock.add(
                method=responses.GET,
                url=f"{RedditDesktopAPI.COMMENT_URL_BASE}/{key}",
                json={
                    "comments": value["comments"],
                },
            )

        yield mock
