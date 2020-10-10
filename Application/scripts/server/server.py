import sys
sys.path.insert(0, 'Application')
import aiohttp
from aiohttp import web, request
from logger.log import MyLogging
from scripts.logic.logic import HandlerServer


app = web.Application()


super_logger = MyLogging().setup_logger('server',
                                        'Application/logger/logfile.log')


async def get_user(request):
    """The method handle 'get_user' route requests."""
    try:
        async with aiohttp.ClientSession() as session:
            data = await request.post()
            handler = HandlerServer(data)
            response = await handler.hand_get_user()
            return web.json_response(response)

    except Exception:
        super_logger.error('Error get_user', exc_info=True)


async def get_order_user(request):
    """The method handle 'get_order_user' route requests."""
    try:
        async with aiohttp.ClientSession() as session:
            data = await request.post()
            handler = HandlerServer(data)
            response = await handler.hand_get_order_user()
            return web.json_response(response)

    except Exception:
        super_logger.error('Error get_order_user', exc_info=True)


async def add_new_order(request):
    """The method handle 'add_new_order' route requests."""
    try:
        async with aiohttp.ClientSession() as session:
            data = await request.post()
            handler = HandlerServer(data)
            response = await handler.hand_add_new_order()
            return web.json_response(response)

    except Exception:
        super_logger.error('Error add_new_order', exc_info=True)


async def get_shop(request):
    """The method handle 'get_shop' route requests."""
    try:
        async with aiohttp.ClientSession() as session:
            data = await request.post()
            handler = HandlerServer(data)
            response = await handler.hand_get_shop()
            return web.json_response(response)

    except Exception:
        super_logger.error('Error get_shop', exc_info=True)
