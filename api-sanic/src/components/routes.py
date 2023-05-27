from . import app
from sanic.response import json
from utils.routes.test import TestView

@app.route("/t", name="foo")
async def test(request):
    return json({"hello": "world"})


app.add_route(TestView.as_view(), "/qq123")