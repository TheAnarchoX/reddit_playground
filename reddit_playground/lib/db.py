import os
import time

from neomodel import (StructuredNode, StringProperty, IntegerProperty, BooleanProperty,RelationshipTo, One, DateTimeProperty)
from praw import models as praw_models

import datetime
from reddit_playground.lib.GlobalContext import GlobalContext
from neomodel import config as neomodel_conf


class Redditor(StructuredNode):
    rid = StringProperty(unique_index=True)
    name = StringProperty(index=True)
    comment_karma = IntegerProperty()
    link_karma = IntegerProperty()
    is_employee = BooleanProperty()
    is_mod = BooleanProperty()
    is_gold = BooleanProperty()
    created_utc = DateTimeProperty(index=True)




class Subreddit(StructuredNode):

    # Labels
    rid = StringProperty(unique_index=True)
    name = StringProperty(index=True)
    display_name = StringProperty(index=True)
    description = StringProperty()
    num_subscribers = IntegerProperty()
    is_nsfw = BooleanProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # # Edges
    # submitters = RelationshipTo('.db.Redditor', 'SUBMITTED')
    # subcribers = RelationshipTo('.db.Redditor', 'IS_SUBSCRIBED')
    # moderators = RelationshipTo('.db.Redditor', 'MODERATES')
    #
    #

class Submission(StructuredNode):
    pass

class Comment(StructuredNode):

    # Labels
    rid = StringProperty(unique_index=True)
    body = StringProperty()
    score = IntegerProperty()
    stickied = BooleanProperty()
    permalink = StringProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # Edges
    # author = RelationshipTo('.Redditor', 'COMMENTED', cardinality=One)
    # submission = RelationshipTo('.Submission', 'COMMENTED_ON', cardinality=One)
    # parent_comment = RelationshipTo('.Comment', 'REPLIED_TO')


def insert_comment(comment: praw_models.Comment):
    neomodel_conf.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'  #this connection method is a shame and i know it

    cmt = Comment(rid=comment.id,
                          body=comment.body,
                          score=comment.score,
                          stickied=comment.stickied,
                          permalink=comment.permalink,
                          created_utc=datetime.datetime.fromtimestamp(comment.created_utc)
                          ).save()

def insert_redditor(redditor: praw_models.Redditor):
    neomodel_conf.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'  #this connection method is a shame and i know it

    rdt = Redditor(rid=redditor.id,
                   name=redditor.name,
                   comment_karma=redditor.comment_karma,
                   link_karma=redditor.link_karma,
                   is_employee=redditor.is_employee,
                   is_mod=redditor.is_mod,
                   is_gold=redditor.is_gold,
                   created_utc=datetime.datetime.fromtimestamp(redditor.created_utc)
                   ).save()


def insert_submission(submission: praw_models.Submission):
    neomodel_conf.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'  #this connection method is a shame and i know it

def insert_subreddit(subreddit: praw_models.Subreddit):
    neomodel_conf.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'  #this connection method is a shame and i know it

    srt = Subreddit(rid=subreddit.id,
                    name=subreddit.name,
                    display_name=subreddit.display_name,
                    description=subreddit.public_description,
                    num_subscribers=subreddit.subscribers,
                    is_nsfw=subreddit.over18,
                    created_utc=datetime.datetime.fromtimestamp(subreddit.created_utc)
                    ).save()
