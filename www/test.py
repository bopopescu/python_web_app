import www.orm

from models import User, Blog, Comment
import aiohttp
import asyncio


async def test(loop):
    #全局变量不可以跨模块
    await www.orm.creat_pool(user='czl', password='password', db='awesome',loop=loop)
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    www.orm.avcs.close()
    await www.orm.avcs.wait_closed()




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
