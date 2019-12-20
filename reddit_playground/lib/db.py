import os
import time

from neomodel import (StructuredNode, StringProperty, IntegerProperty, BooleanProperty,RelationshipTo, One, DateTimeProperty)
class Redditor(StructuredNode):
    pass


class Subreddit(StructuredNode):

    # Labels
    id = StringProperty(unique_index=True)
    name = StringProperty(index=True)
    description = StringProperty()
    num_subscribers = IntegerProperty()
    is_nsfw = BooleanProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # Edges
    submitters = RelationshipTo('.Redditor', 'SUBMITTED')
    subcribers = RelationshipTo('.Redditor', 'IS_SUBSCRIBED')
    moderators = RelationshipTo('.Redditor', 'MODERATES')



class Submission(StructuredNode):
    pass

class Comment(StructuredNode):

    # Labels
    id = StringProperty(unique_index=True)
    body = StringProperty()
    score = IntegerProperty()
    stickied = BooleanProperty()
    permalink = StringProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # Edges
    author = RelationshipTo('.Redditor', 'COMMENTED', cardinality=One)
    submission = RelationshipTo('.Submission', 'COMMENTED_ON', cardinality=One)
    parent_comment = RelationshipTo('.Comment', 'REPLIED_TO')

