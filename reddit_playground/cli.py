# -*- coding: utf-8 -*-

"""Console script for reddit_playground."""
import sys
import click
import configparser
import os
from neomodel import db as neodb
from reddit_playground.lib.GlobalContext import GlobalContext
from reddit_playground.lib.db import Comment

@click.command()
@click.option("-v", "--verbose", is_flag=True, help='run Reddit Playground in verbose mode')
def main(verbose):

    os.environ["PLAYGROUND_VERBOSE"] = str(verbose).upper()
    neodb.set_connection(os.getenv('NEO4J_CS'))  #this connection method is a shame and i know it


    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    if os.getenv("PLAYGROUND_VERBOSE") == "TRUE":
        print(f"Starting Reddit Playground (v{config.get('PLAYGROUND', 'VERSION')})")

    # Initialize the GlobalContext
    ctx = GlobalContext()

    sr = ctx.Reddit.subreddit('all')


    for comment in sr.stream.comments():
        ctx.comment_queue.enqueue('reddit_playground.lib.db.insert_comment', comment)
        ctx.redditor_queue.enqueue('reddit_playground.lib.db.insert_redditor', comment.author)
        # ctx.submission_queue.enqueue('reddit_playground.lib.db.insert_submission', comment.submission)
        ctx.subreddit_queue.enqueue('reddit_playground.lib.db.insert_subreddit', comment.submission.subreddit)

    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
