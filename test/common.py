POST_DATA = {
    "post_1": {
        "id": "post_1",
        "comments": {
            "comment_2": {
                "id": "comment_2",
            },
            "comment_3": {
                "id": "comment_3",
            },
        },
    },
    "post_2": {
        "id": "post_2",
        "comments": {
            "comment_1": {
                "id": "comment_1",
            },
        },
    },
    "post_3": {
        "id": "post_3",
        "comments": {
            "comment_1": {
                "id": "comment_1",
            },
            "comment_2": {
                "id": "comment_2",
            },
            "comment_3": {
                "id": "comment_3",
            },
        },
    },
}
POST_DATA_LIST = list(POST_DATA.values())
POST_ID_LIST = list(POST_DATA.keys())
TOKEN = "test_token"  # nosec
SUBREDDIT_NAME = "test_subreddit"
DOMAIN_A = "domain-a.com"
DOMAIN_A_WWW = f"www.{DOMAIN_A}"
DOMAIN_B = "domain-b.com"
DOMAIN_B_WWW = f"www.{DOMAIN_B}"
