from typing import Any

import click
from click_params import DomainListParamType

from .. import __version__
from ..harvester import Harvester, HarvesterConfig
from ..meta import SortChoice


@click.command()
@click.version_option(__version__, "-v", "--version")
@click.option("-d", "--delay", default=None, help="Delay between requests in seconds.", type=float)
@click.option(
    "-s",
    "--sort",
    default=SortChoice.HOT,
    help="Sort order of subreddit posts.",
    type=click.Choice(SortChoice),
)
@click.option(
    "-i",
    "--include-domains",
    default=None,
    type=DomainListParamType(),
    help="Comma separated list of allowed domains (has precedence over --exclude-domains).",
)
@click.option(
    "-x",
    "--exclude-domains",
    default=None,
    type=DomainListParamType(),
    help="Comma separated list of excluded domains.",
)
@click.argument("subreddit")
def main(**kwargs: Any) -> int:
    config = HarvesterConfig(
        delay=kwargs.get("delay"),
        sort=kwargs.get("sort"),
        include_domains=kwargs.get("include_domains"),
        exclude_domains=kwargs.get("exclude_domains"),
    )

    with Harvester(kwargs.get("subreddit"), config) as harvester:
        harvester.run()

    return 0
