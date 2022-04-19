from typing import Any

import click

from .. import __version__
from ..harvester import Harvester, HarvesterConfig
from ..meta import SortChoice


@click.command()
@click.version_option(__version__, "-v", "--version")
@click.option("-d", "--delay", default=None, help="Delay between requests in seconds.", type=float)
@click.option(
    "-s",
    "--sort",
    default=SortChoice.HOT.value,
    help="Sort order of subreddit posts.",
    type=click.Choice([choice.value for choice in SortChoice]),
)
@click.option(
    "-u",
    "--url-patterns",
    multiple=True,
    help="Only match provided url pattern(s) (has precedence over --exclude-url-patterns).",
)
@click.option(
    "-x",
    "--exclude-url-patterns",
    multiple=True,
    help="Exclude provided url pattern(s).",
)
@click.argument("subreddit")
def main(**kwargs: Any) -> int:
    config = HarvesterConfig(
        delay=kwargs.get("delay"),
        sort=kwargs.get("sort"),
        url_patterns=kwargs.get("url_patterns"),
        exclude_url_patterns=kwargs.get("exclude_url_patterns"),
    )

    with Harvester(kwargs.get("subreddit"), config) as harvester:
        harvester.run()

    return 0
