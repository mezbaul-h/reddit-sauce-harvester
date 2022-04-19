# reddit-sauce-harvester

[![ci](https://github.com/mehq/reddit-sauce-harvester/workflows/ci/badge.svg?branch=master)](https://github.com/mehq/reddit-sauce-harvester/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mehq/reddit-sauce-harvester/branch/master/graph/badge.svg)](https://codecov.io/gh/mehq/reddit-sauce-harvester)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](https://github.com/mehq/reddit-sauce-harvester/blob/master/LICENSE.txt)

A command program tool to harvest links (sauces) from reddit post comments.

## Installation
### From PyPI
```bash
pip install reddit-sauce-harvester
```

### From Source
```bash
git clone https://github.com/mehq/reddit-sauce-harvester.git
cd reddit-sauce-harvester
python setup.py install
```


## Usage

```bash
rsharvester [OPTIONS] SUBREDDIT
```
### Options
```bash
-v, --version                   Show the version and exit.
-d, --delay FLOAT               Delay between requests in seconds.
-s, --sort [hot|new|rising|top_all|top_hour|top_day|top_week|top_month|top_year]
                                Sort order of subreddit posts.
-u, --url-pattern TEXT          Only match provided url pattern(s) (has
                                precedence over --exclude-url-pattern).
-x, --exclude-url-pattern TEXT
                                Exclude provided url pattern(s).
--help                          Show this message and exit.
```
