import asyncio
from coroweb import get, post
from models import User, Blog
import time


@get('/')
async def index(request):
    summary = 'Hello,World.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, create_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, create_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, create_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }