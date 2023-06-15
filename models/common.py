from app import db

def select(query):
    result = db.session.execute(query)
    return result.fetchall()

def insert(model_instance):
    db.session.add(model_instance)
    db.session.commit()

def update():
    db.session.commit()

def delete(model_instance):
    db.session.delete(model_instance)
    db.session.commit()

def begin_transaction():
    db.session.begin()

def commit_transaction():
    db.session.commit()

def rollback_transaction():
    db.session.rollback()
