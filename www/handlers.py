import asyncio
from coroweb import get, post
from models import User


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__':'__base__.html',
        'users':users
    }