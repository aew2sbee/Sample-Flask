from flask import Flask
# Flaskアプリケーションオブジェクトの作成
app = Flask(__name__)

import study.main

from study import db
db.create_books_table()
