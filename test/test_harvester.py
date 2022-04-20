import re
from typing import Generator, Tuple

import pytest

from reddit_sauce_harvester.harvester import Harvester, HarvesterConfig
from reddit_sauce_harvester.meta import SortChoice

from .common import DOMAIN_A, DOMAIN_A_WWW, DOMAIN_B, DOMAIN_B_WWW, SUBREDDIT_NAME

DOMAIN_COMBINATIONS = [(), (DOMAIN_A,), (DOMAIN_A, DOMAIN_B_WWW), (DOMAIN_A_WWW, DOMAIN_B)]


@pytest.mark.parametrize("sort", list(SortChoice))
@pytest.mark.parametrize("url_patterns", DOMAIN_COMBINATIONS)
@pytest.mark.parametrize("exclude_url_patterns", DOMAIN_COMBINATIONS)
def test_harvester(
    sort: SortChoice,
    url_patterns: Tuple[str],
    exclude_url_patterns: Tuple[str],
    register_mock_requests: Generator,  # pylint: disable=unused-argument
) -> None:
    config = HarvesterConfig(
        delay=None,
        sort=sort,
        url_patterns=url_patterns,
        exclude_url_patterns=exclude_url_patterns,
    )
    with Harvester(SUBREDDIT_NAME, config=config) as harvester:
        harvester.run()
        items = harvester.items

        for item in [source for item in items for source in item[1]]:
            if url_patterns:
                assert any((re.search(pattern, item) for pattern in url_patterns))
            elif exclude_url_patterns:
                assert all((re.search(pattern, item) for pattern in exclude_url_patterns))


@pytest.mark.parametrize("delay", [0.5, 1])
def test_harvester_delay(
    delay: float,
    register_mock_requests: Generator,  # pylint: disable=unused-argument
) -> None:
    config = HarvesterConfig(
        delay=delay,
        sort=SortChoice.HOT,
    )

    with Harvester(SUBREDDIT_NAME, config=config) as harvester:
        harvester.run()
