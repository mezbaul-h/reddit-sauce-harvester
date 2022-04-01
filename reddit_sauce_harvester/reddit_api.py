import requests


class RedditDesktopAPI:
    SUBREDDIT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/subreddits"
    COMMENT_URL_BASE = "https://gateway.reddit.com/desktopapi/v1/postcomments"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/98.0.4758.102 Safari/537.36"
            ),
        }

    def get_post_comments(self, subreddit_name: str, post_id: str):
        response = self.session.get(
            f"{self.COMMENT_URL_BASE}/{post_id}",
            params={
                "rtj": "only",
                "emotes_as_images": True,
                "redditWebClient": "web2x",
                "app": "web2x-client-production",
                "profile_img": True,
                "allow_over18": 1,
                "include": "",
                "subredditName": subreddit_name,
                "hasSortParam": False,
                "include_categories": True,
                "onOtherDiscussions": False,
            },
        )
        response.raise_for_status()
        return response.json()["comments"].values()

    def get_subreddit_posts(self, subreddit_name: str, token: str = None, sort: str = None):
        sort_query_params = {}

        if sort == "hot":
            sort_query_params["sort"] = "hot"
        elif sort == "top":
            sort_query_params["sort"] = "top"
            sort_query_params["t"] = "all"

        response = self.session.get(
            f"{self.SUBREDDIT_URL_BASE}/{subreddit_name}",
            params={
                "rtj": "only",
                "redditWebClient": "web2x",
                "app": "web2x-client-production",
                "allow_over18": 1,
                "include": "",
                "layout": "classic",
                "after": token,
                **sort_query_params,
            },
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data["posts"].values(), response_data["token"]
