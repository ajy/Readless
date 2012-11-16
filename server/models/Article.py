from server import db

class Features(db.EmbeddedDocument):
    #TODO:implementation
    pass

class Reader(db.EmbeddedDocument):
    #TODO:implementation
    user = db.ReferenceField('User', dbref = False)# the false setting here will make mongoengine use ObjectId strings here, i think
    score = db.FloatField(min_value = 0, max_value = 1, default = 0.5)

class Article(db.Document):
    source_url = db.URLField(verify_exists = True)
    feed = db.ReferenceField('Feed', dbref = True)#lazily dereferenced on access
    features = db.EmbeddedDocumentField('Features')
    readers = db.ListField(db.EmbeddedDocumentField('Reader'))
