"""Site-specific overrides.

These are keyed without the www prefix. The keyed sites must be in lowercase.
"""

NETLOC_OVERRIDES = {
    "aliexpress.com": {
        "user_agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
    },
    "arxiv.org": {"url_subs": [(r"/pdf/(?P<id>.+?)(?:\.pdf)?$", r"/abs/\g<id>")]},
    "bloomberg.com": {"extra_headers": {"Referer": "https://google.com/", "DNT": 1}},
    "cbc.ca": {"bs_title_selector": """bs.select_one('meta[property="og:title"]')['content']"""},
    "cell.com": {
        "url_subs": [
            (r"cell\.com/(?P<path>.+?)/pdf(?:Extended)*/(?P<id>.+?)(?:\.pdf)?$", r"cell.com/\g<path>/fulltext/\g<id>"),
            (r"cell\.com/action/showPdf\?pii=(?P<id>.+)$", r"cell.com/cell/fulltext/\g<id>"),
        ]
    },
    "citeseerx.ist.psu.edu": {
        "url_subs": [(r"/viewdoc/download\?doi=(?P<doi>.+?)\&.+$", r"/viewdoc/summary?doi=\g<doi>")]
    },
    "colab.research.google.com": {
        "url_subs": [
            (r"//colab\.research\.google\.com/drive/(?P<id>[\w\-]+)(?:\#.*)?$", r"//drive.google.com/file/d/\g<id>"),
            (
                r"//colab\.research\.google\.com/github/(?P<repo>\w+/\w+)/blob/(?P<file>[^\#]*?\.ipynb)(?:\#.*)?$",
                r"//raw.githubusercontent.com/\g<repo>/\g<file>",
            ),
        ],
        "title_subs": [(r"(?P<name>.+?) \- Google Drive$", r"\g<name> - Colaboratory")],
    },
    "docs.aws.amazon.com": {
        "bs_title_selector": """bs.select_one(".topictitle").text + " - " + bs.select_one('meta[name="product"]')['content']"""  # pylint: disable=line-too-long
    },
    "eudl.eu": {"url_subs": [(r"/pdf/(?P<id>.+?)$", r"/doi/\g<id>")]},
    "ft.com": {"user_agent": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"},  # Iffy.
    "forum.effectivealtruism.org": {"extra_headers": {"Accept": "*/*"}},
    "fresnobee.com": {"extra_headers": {"Accept": "*/*", "Accept-Encoding": "gzip"}},
    "gastrojournal.org": {
        "url_subs": [(r"gastrojournal\.org/article/(?P<id>.+?)/pdf$", r"gastrojournal.org/article/\g<id>/")]
    },
    "iopscience.iop.org": {
        "url_subs": [(r"iopscience\.iop\.org/article/(?P<id>.+?)/pdf$", r"iopscience.iop.org/article/\g<id>")]
    },
    "jstor.org": {"user_agent": "Mozilla/5.0"},
    "medscape.com": {"user_agent": "Googlebot-News"},
    "miamiherald.com": {"extra_headers": {"Accept": "*/*", "Accept-Encoding": "gzip"}},
    "mobile.twitter.com": {"url_subs": [(r"^https?://mobile\.twitter\.com/", r"https://twitter.com/")]},
    "money.usnews.com": {"extra_headers": {"Cookie": "", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5"}},
    "m.slashdot.org": {"url_subs": [(r"m\.slashdot\.org/(?P<path>.+)$", r"slashdot.org/\g<path>/")]},
    "m.youtube.com": {"user_agent": "Mozilla/5.0"},
    "nationalgeographic.com": {"user_agent": "Googlebot-News"},  # Seems to prevent timeout.
    "nature.com": {"url_subs": [(r"nature\.com/articles/(?P<id>.+?)\.pdf$", r"nature.com/articles/\g<id>")]},
    "ncbi.nlm.nih.gov": {
        "url_subs": [(r"/pmc/articles/PMC(?P<id>.+?)/pdf/?(?:.+?\.pdf)?$", r"/pmc/articles/PMC\g<id>/")]
    },
    "omicsonline.org": {"google_webcache": True},
    "onlinelibrary.wiley.com": {
        "url_subs": [
            (r"onlinelibrary\.wiley\.com/doi/(?P<doi>.+?)/pdf$", r"onlinelibrary.wiley.com/doi/\g<doi>"),
            (r"onlinelibrary\.wiley\.com/doi/pdf/(?P<doi>.+)$", r"onlinelibrary.wiley.com/doi/\g<doi>"),
        ]
    },
    "outline.com": {"user_agent": "Googlebot-News"},
    "pdfs.semanticscholar.org": {
        "url_subs": [
            (
                r"//pdfs\.semanticscholar.org/(?P<id1>.+?)/(?P<id2>.+?)\.pdf$",
                r"//semanticscholar.org/paper/\g<id1>\g<id2>",
            )
        ]
    },
    "pubs.acs.org": {"url_subs": [(r"^https://(?P<url>.+)$", r"http://\g<url>")]},
    "researchgate.net": {
        "url_subs": [
            (
                r"researchgate\.net/profile/(?P<author>.+?)/publication/(?P<pub>.+?)/links/.+?\.pdf$",
                r"researchgate.net/profile/\g<author>/publication/\g<pub>",
            )
        ]
    },
    "seekingalpha.com": {"extra_headers": {"Host": "seekingalpha.com", "Referer": "https://google.com/", "DNT": 1}},
    "swansonvitamins.com": {"user_agent": "FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)"},
    "t.co": {"substitute_url_with_title": True},
    "twitter.com": {"user_agent": "Mozilla/5.0"},
    "trends.google.com": {"url_subs": [(r"^https://(?P<url>.+)$", r"http://\g<url>")]},
    "usnews.com": {"user_agent": "FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)"},
    "youtu.be": {"user_agent": "Mozilla/5.0"},
    "youtube.com": {"user_agent": "Mozilla/5.0"},
}
