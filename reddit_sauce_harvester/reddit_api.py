from typing import Any, Dict, List, Optional

import requests

from reddit_sauce_harvester.meta import SortChoice


class RedditDesktopAPI:
    SUBREDDIT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/subreddits"
    COMMENT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/postcomments"
    COMMON_QUERY_PARAMS = {
        "allow_over18": 1,
        "rtj": "only",
    }

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/98.0.4758.102 Safari/537.36"
            ),
        }

    def get_post_comments(self, post_id: str) -> List[Dict[str, Any]]:
        response = self.session.get(
            f"{self.COMMENT_URL_BASE}/{post_id}",
            params=self.COMMON_QUERY_PARAMS,
        )
        response.raise_for_status()

        return response.json()["comments"].values()

    def get_subreddit_posts(self, subreddit_name: str, token: Optional[str], sort: SortChoice):
        sort_query_params = {}

        if sort == SortChoice.HOT:
            sort_query_params["sort"] = "hot"
        elif sort == SortChoice.NEW:
            sort_query_params["sort"] = "new"
        elif sort == SortChoice.RISING:
            sort_query_params["sort"] = "rising"
        else:  # elif sort in SORT_TOP_CHOICES:
            sort_query_params["sort"] = "top"

            if sort == SortChoice.TOP_ALL_TIME:
                sort_query_params["t"] = "all"
            elif sort == SortChoice.TOP_HOUR:
                sort_query_params["t"] = "hour"
            elif sort == SortChoice.TOP_DAY:
                sort_query_params["t"] = "day"
            elif sort == SortChoice.TOP_WEEK:
                sort_query_params["t"] = "week"
            elif sort == SortChoice.TOP_MONTH:
                sort_query_params["t"] = "month"
            else:  # elif sort == SortChoice.TOP_YEAR:
                sort_query_params["t"] = "year"

        response = self.session.get(
            f"{self.SUBREDDIT_URL_BASE}/{subreddit_name}",
            params={
                "after": token,
                **sort_query_params,
                **self.COMMON_QUERY_PARAMS,
            },
        )
        response.raise_for_status()
        response_data = response.json()

        return response_data["posts"].values(), response_data["token"]
