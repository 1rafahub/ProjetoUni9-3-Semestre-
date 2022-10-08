from flask import Flask
from datetime import timedelta


app = Flask(__name__, static_folder="./static", template_folder="templates")
app.config["SECRET_KEY"] = 'secret'
# Config session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.permanent_session_lifetime = timedelta(days=1)



#Rotas precisa ficar depois das condigurações

from controllers import routes