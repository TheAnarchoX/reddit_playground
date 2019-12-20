import configparser
import os
import time

from neomodel import config as neomodel_conf
from praw import Reddit
from redis import Redis
from rq import Queue


def test():
    return None

class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

class GlobalContext(Singleton):

    def __init__(self):
        """The Global Context of the Playground"""

        self.verbose = os.getenv("PLAYGROUND_VERBOSE") == "TRUE"

        #Instantiate the config
        config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..','config','config.ini')

        if self.verbose:
            print(f"Loading Config from {config_path}")

        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..','config','config.ini'))


        self.debug = self.config.get('PLAYGROUND', 'DEBUG')

        #Instantiate the Reddit client
        if self.verbose:
            print(f"Connecting to Reddit")
        self.Reddit = Reddit()

        if self.verbose:
            print(f"Connected as: {self.Reddit.user.me()}")

        #Create database engine
        neomodel_conf.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'  #this connection method is a shame and i know it
        if self.verbose:
            print(f"Connected to Neo4j DB")

        # Connect to redis
        if self.verbose:
            print(f"Connecting to redis")
        self.redis = Redis(host='127.0.0.1')

        # Set up queues
        if self.verbose:
            print(f"Setting up queues")

        self.test_queue = Queue('test', connection=self.redis)
        self.redditor_queue = Queue('redditors', connection=self.redis)
        self.subreddit_queue = Queue('subreddits', connection=self.redis)
        self.submission_queue = Queue('submissions', connection=self.redis)
        self.comment_queue = Queue('comments', connection=self.redis)
