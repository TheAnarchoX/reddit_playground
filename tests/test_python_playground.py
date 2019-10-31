#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_playground` package."""


import unittest
from click.testing import CliRunner

from python_playground import playground
from python_playground import cli


class TestPython_playground(unittest.TestCase):
    """Tests for `python_playground` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'python_playground.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
