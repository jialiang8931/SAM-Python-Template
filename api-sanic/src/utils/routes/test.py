from sanic.views import HTTPMethodView
from sanic.response import json

class TestView(HTTPMethodView):

  async def get(self, request):
      return json({"hello": "world"})

  async def post(self, request):
      return json({"hello": "world"})
  