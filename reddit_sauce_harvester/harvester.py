import time
import timeit
from typing import Any, List, Optional, Tuple
from urllib.parse import urlparse

from .meta import SortChoice
from .reddit_api import RedditDesktopAPI
from .utils import deep_get

Item = Tuple[str, List[str]]


class HarvesterConfig:
    def __init__(self, **kwargs: Any) -> None:
        self.delay: Optional[float] = kwargs.get("delay")
        self.sort: SortChoice = kwargs.get("sort")
        self.include_domains: Optional[List[str]] = kwargs.get("include_domains")
        self.exclude_domains: Optional[List[str]] = kwargs.get("exclude_domains")


class Harvester:
    DOMAIN = "reddit.com"

    def __init__(self, subreddit_name: str, config: HarvesterConfig) -> None:
        self.subreddit_name = subreddit_name
        self.api = RedditDesktopAPI()
        self.config = config
        self.started_at = timeit.default_timer()
        self._items: List[Item] = []

    def __enter__(self) -> "Harvester":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.api.session.close()

    @property
    def items(self) -> List[Item]:
        return self._items

    def is_valid_source(self, source: str) -> bool:
        parsed_url_obj = urlparse(source)
        domain = parsed_url_obj.hostname or self.DOMAIN
        alt_domain = domain.lstrip("www.") if domain.startswith("www.") else f"www.{domain}"
        domains = [domain, alt_domain]

        if self.config.include_domains is not None:
            return any((item in self.config.include_domains for item in domains))

        if self.config.exclude_domains is not None:
            return all((item not in self.config.exclude_domains for item in domains))

        return True

    def get_sources(self, post_id: str) -> List[str]:
        items = self.api.get_post_comments(post_id)
        sources = {}  # Use dict vs list for O(1) lookup

        for item in items:
            paragraphs = deep_get(item, "media.richtextContent.document", default=[])

            while paragraphs:
                paragraph = paragraphs.pop()
                paragraph_type = paragraph.get("e")

                if paragraph_type == "par":
                    paragraphs.extend(paragraph.get("c"))
                elif paragraph_type == "link":
                    source = paragraph.get("u")
                    if source not in sources and self.is_valid_source(source):
                        sources[source] = True

        return list(sources.keys())

    def apply_delay(self) -> None:
        if self.config.delay:
            time.sleep(self.config.delay)

    def iterate_posts_and_harvest(self) -> None:
        has_more = True
        token: Optional[str] = None

        while has_more:
            posts, token = self.api.get_subreddit_posts(self.subreddit_name, token, self.config.sort)
            has_more = token is not None

            for post in posts:
                self.apply_delay()
                sources = self.get_sources(post["id"])

                if sources:
                    self._items.append((post, sources))
                    print(post["title"])

                    for source in sources:
                        print(f"└── {source}")

            self.apply_delay()

    def run(self) -> None:
        self.iterate_posts_and_harvest()
