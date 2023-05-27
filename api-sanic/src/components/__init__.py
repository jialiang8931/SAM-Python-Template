from sanic import Sanic
from sanic.response import json
from mangum import Mangum
from constants import setting


app = Sanic(name="Test123")

from components import routes
handler = Mangum(app)
