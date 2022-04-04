POST_DATA = {
    "post_1": {
        "id": "post_1",
        "title": "post 1 title",
        "comments": {
            "comment_2": {
                "id": "comment_2",
                "media": {
                    "richtextContent": {"document": [{"c": [{"e": "text", "t": "Hello world"}], "e": "par"}]},
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
            },
            "comment_3": {
                "id": "comment_3",
                "media": {
                    "richtextContent": {
                        "document": [
                            {
                                "c": [
                                    {"e": "text", "t": "Sauce : "},
                                    {
                                        "u": "https://domain-a.com/video.mp4",
                                        "e": "link",
                                        "t": "https://domain-a.com/video.mp4",
                                    },
                                ],
                                "e": "par",
                            }
                        ]
                    },
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
            },
        },
    },
    "post_2": {
        "id": "post_2",
        "title": "post 2 title",
        "comments": {
            "comment_1": {
                "id": "comment_1",
                "media": {
                    "richtextContent": {
                        "document": [
                            {
                                "c": [
                                    {"e": "text", "t": "Sauce : "},
                                    {
                                        "u": "https://www.domain-a.com/video.mp4",
                                        "e": "link",
                                        "t": "https://www.domain-a.com/video.mp4",
                                    },
                                ],
                                "e": "par",
                            }
                        ]
                    },
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
            }
        },
    },
    "post_3": {
        "id": "post_3",
        "title": "post 3 title",
        "comments": {
            "comment_1": {
                "id": "comment_1",
                "media": {
                    "richtextContent": {
                        "document": [
                            {
                                "c": [
                                    {"e": "text", "t": "Sauce : "},
                                    {
                                        "u": "https://domain-b.com/video.mp4",
                                        "e": "link",
                                        "t": "https://domain-b.com/video.mp4",
                                    },
                                ],
                                "e": "par",
                            }
                        ]
                    },
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
            },
            "comment_2": {
                "id": "comment_2",
                "media": {
                    "richtextContent": {
                        "document": [
                            {
                                "c": [
                                    {"e": "text", "t": "Sauce : "},
                                    {
                                        "u": "https://www.domain-b.com/video.mp4",
                                        "e": "link",
                                        "t": "https://www.domain-b.com/video.mp4",
                                    },
                                ],
                                "e": "par",
                            }
                        ]
                    },
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
            },
            "comment_3": {
                "id": "comment_3",
                "media": {
                    "richtextContent": {
                        "document": [
                            {
                                "c": [
                                    {"e": "text", "t": "Sauce : "},
                                    {
                                        "u": "https://domain-c.com/video.mp4",
                                        "e": "link",
                                        "t": "https://domain-c.com/video.mp4",
                                    },
                                ],
                                "e": "par",
                            }
                        ]
                    },
                    "type": "rtjson",
                    "rteMode": "richtext",
                },
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
