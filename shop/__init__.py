from flask import Flask
# import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
# import AdminView from shop/views.py
from shop.views import AdminView


app = Flask(__name__)
app.config['SECRET_KEY'] = 'db5821567f7f382d2883960140f805c2da33e9bffd7b78d6'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<your_password>@localhost/bookstore'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 1
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Import your models after db and login_manager have been created
from shop.models import User, Books, Reviews, Wishlist, Purchases, Purchased_items

admin = Admin(app, name='Admin panel', template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Books, db.session))
admin.add_view(AdminView(Reviews, db.session))
admin.add_view(AdminView(Purchases, db.session))
admin.add_view(AdminView(Purchased_items, db.session))
admin.add_view(AdminView(Wishlist, db.session))

# Don't forget to import routes at the end, after db and login_manager have been created
from shop import routes
