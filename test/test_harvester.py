from typing import Generator, List, Optional

import pytest

from reddit_sauce_harvester.harvester import Harvester, HarvesterConfig
from reddit_sauce_harvester.meta import SortChoice

from .common import DOMAIN_A, DOMAIN_A_WWW, DOMAIN_B, DOMAIN_B_WWW, SUBREDDIT_NAME

DOMAIN_LIST = [None, DOMAIN_A, DOMAIN_A_WWW, DOMAIN_B, DOMAIN_B_WWW]


@pytest.mark.parametrize("sort", list(SortChoice))
@pytest.mark.parametrize("include_domains", DOMAIN_LIST)
@pytest.mark.parametrize("exclude_domains", DOMAIN_LIST)
def test_harvester(
    sort: SortChoice,
    include_domains: Optional[List[str]],
    exclude_domains: Optional[List[str]],
    register_mock_requests: Generator,  # pylint: disable=unused-argument
) -> None:
    config = HarvesterConfig(
        delay=None,
        sort=sort,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
    )
    with Harvester(SUBREDDIT_NAME, config=config) as harvester:
        harvester.run()


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
