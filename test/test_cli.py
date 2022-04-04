from typing import Generator

from click.testing import CliRunner

from reddit_sauce_harvester.cli import main

from .common import DOMAIN_A, SUBREDDIT_NAME


def test_cli(
    register_mock_requests: Generator,  # pylint: disable=unused-argument
):
    runner = CliRunner()
    result = runner.invoke(main, [SUBREDDIT_NAME])
    assert DOMAIN_A in result.stdout
    assert result.exit_code == 0
