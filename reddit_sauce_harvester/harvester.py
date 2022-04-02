import time
import timeit
from typing import Any, List, Optional, Tuple
from urllib.parse import urlparse

from .meta import SortChoice
from .reddit_api import RedditDesktopAPI
from .utils import deep_get

Item = Tuple[str, List[str]]


class HarvesterConfig:
    def __init__(self, **kwargs: Any):
        self.delay: Optional[float] = kwargs.get("delay")
        self.when_to_stop: Optional[str] = kwargs.get("when_to_stop")
        self.sort: SortChoice = kwargs.get("sort")
        self.include_domains: Optional[List[str]] = kwargs.get("include_domains")
        self.exclude_domains: Optional[List[str]] = kwargs.get("exclude_domains")


class Harvester:
    DOMAIN = "reddit.com"
    SUBREDDIT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/subreddits"
    COMMENT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/postcomments"

    def __init__(self, subreddit_name: str, config: HarvesterConfig) -> None:
        self.subreddit_name = subreddit_name
        self.api = RedditDesktopAPI()
        self.config = config
        self.started_at = timeit.default_timer()

        # when to stop
        self._max_post = None
        self._max_time_seconds = None

    def __enter__(self) -> "Harvester":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.api.session.close()

    @property
    def wts_props(self) -> Tuple[Optional[int], Optional[int]]:
        if not self.config.when_to_stop or (self._max_post or self._max_time_seconds):
            return self._max_post, self._max_time_seconds

        what, when = self.config.when_to_stop.split(":")

        if what.lower() == "p":
            self._max_post = int(when, 10)
        elif what.lower() == "t":
            self._max_time_seconds = int(when, 10)

        return self._max_post, self._max_time_seconds

    def is_valid_source(self, source: str) -> bool:
        parsed_url_obj = urlparse(source)
        domain = parsed_url_obj.hostname or self.DOMAIN
        alt_domain = domain.lstrip("www.") if domain.startswith("www.") else f"www.{domain}"
        domains = [domain, alt_domain]

        if self.config.include_domains is not None:
            return any((item in self.config.include_domains for item in domains))

        if self.config.exclude_domains is not None:
            return any((item not in self.config.exclude_domains for item in domains))

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

    def should_continue(self, items: List[Item]) -> bool:
        max_post, max_time_seconds = self.wts_props

        if max_post is not None:
            return len(items) < max_post

        if max_time_seconds is not None:
            time_elapsed = timeit.default_timer() - self.started_at
            return time_elapsed < max_time_seconds

        return True

    def apply_delay(self):
        if self.config.delay:
            time.sleep(self.config.delay)

    def iterate_posts(self) -> None:
        items: List[Item] = []
        has_more = True
        token = None

        while has_more and self.should_continue(items):
            posts, token = self.api.get_subreddit_posts(self.subreddit_name, token=token, sort=self.config.sort)
            has_more = token is not None

            for post in posts:
                if not self.should_continue(items):
                    break

                self.apply_delay()
                sources = self.get_sources(post["id"])

                if sources:
                    items.append((post, sources))
                    print(f"[{len(items)}] {post['title']}: {sources}")

            self.apply_delay()

    def run(self):
        self.iterate_posts()
