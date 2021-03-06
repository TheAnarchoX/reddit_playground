#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `reddit_playground` package."""


import unittest
from click.testing import CliRunner

from reddit_playground import cli


class Testreddit_playground(unittest.TestCase):
    """Tests for `reddit_playground` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
