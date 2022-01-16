import couchdb

couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")

def DatabaseTest():
    # couch.create('everydaywords')
    # couch.create('technicalwords')
    # couch.create('simplepresenttense')
    # couch.create('presentcontinuous')
    # couch.create('simplepast')
    # couch.create('pastcontinuous')
    # couch.create('presentperfect')
    # couch.create('presentperfectcont')
    # couch.create('pastperfect')
    # couch.create('pastperfectcont')
    # couch.create('simplefuture')
    # couch.create('futurecont')
    couch.create('futureperfect')
DatabaseTest()
