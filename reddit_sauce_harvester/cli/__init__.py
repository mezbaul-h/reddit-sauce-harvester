from typing import Any

import click
from click_params import DomainListParamType

from .. import __version__
from ..harvester import Harvester, HarvesterConfig


@click.command()
@click.version_option(__version__, "-v", "--version")
@click.option("-w", "--when-to-stop", default=None, help="when to stop")
@click.option("-d", "--delay", default=None, help="delay between scraper requests (seconds)")
@click.option("-s", "--sort", default="hot", type=click.Choice(["top", "hot"], case_sensitive=True))
@click.option(
    "-i",
    "--include-domains",
    default=None,
    type=DomainListParamType(),
    help="comma separated list of allowed domains (has precedence over --exclude-domains)",
)
@click.option(
    "-x",
    "--exclude-domains",
    default=None,
    type=DomainListParamType(),
    help="comma separated list of excluded domains",
)
@click.argument("subreddit")
def main(*args: Any) -> int:
    config = HarvesterConfig(
        when_to_stop=args[0],
        delay=args[1],
        sort=args[2],
        include_domains=args[3],
        exclude_domains=args[4],
    )

    with Harvester(args[-1], config) as harvester:
        harvester.run()

    return 0
