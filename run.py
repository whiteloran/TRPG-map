# -*- coding: utf-8 -*-
from app import create_app

def create_db(app):
    from app import db
    app.app_context().push()
    db.create_all()

if __name__ == '__main__':
    myapp = create_app('develop')
    myapp.run(host="0.0.0.0")