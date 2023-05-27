from . import app
from sanic.response import json

@app.route("/t", name="foo")
async def test(request):
    return json({"hello": "world"})
