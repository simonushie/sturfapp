from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
from app.config import Config
from flask_migrate import Migrate
# import flask_whooshalchemy as wa


# from app import models





####################
#### extensions ####
####################
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Proxy Configuration for login tracking
app.wsgi_app = ProxyFix(app.wsgi_app)


####################
#### blueprints ####
####################
from app.blueprints.example_blueprint.example_blueprint import example
from app.blueprints.home.views import index_blueprint
from app.blueprints.about_us.views import about_us_blueprint
from app.blueprints.history.views import history_blueprint
from app.blueprints.electricity.views import electricity
from app.blueprints.help.views import help_blueprint
from app.blueprints.feedback.views import feedback_blueprint
from app.blueprints.rent.views import rent_blueprint
from app.blueprints.post.views import post_blueprint
from app.blueprints.roomie.views import roomie_blueprint
from app.blueprints.buy.views import buy_blueprint






app.register_blueprint(example,url_prefix='/example')
app.register_blueprint(index_blueprint,url_prefix='/')
app.register_blueprint(about_us_blueprint,url_prefix='/about-us')
app.register_blueprint(history_blueprint,url_prefix='/history')
app.register_blueprint(help_blueprint,url_prefix='/help')
app.register_blueprint(feedback_blueprint,url_prefix='/feedback')
app.register_blueprint(electricity,url_prefix='/electricity')
app.register_blueprint(rent_blueprint,url_prefix='/rent')
app.register_blueprint(post_blueprint,url_prefix='/post')
app.register_blueprint(roomie_blueprint,url_prefix='/roomie')
app.register_blueprint(buy_blueprint,url_prefix='/buy-and-sell') 





########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return  render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500




from app import views, models













# from app.models import Post


# flask_whooshalchemy Configuration

# must be instantiated after the models are imported

# wa.whoosh_index(app, Post )