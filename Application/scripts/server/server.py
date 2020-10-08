import aiohttp
from aiohttp import web, request
import sys
sys.path.insert(0, 'Application')
from logger.log import MyLogging


app = web.Application()


super_logger = MyLogging().setup_logger('server',
                                        'Application/logger/logfile.log')


async def get_user(request):
    try:
        async with aiohttp.ClientSession() as session:
            pass
        return web.json_response({'ok': True})

    except Exception:
        super_logger.error('Error get_user', exc_info=True)


async def get_order_user(request):
    try:
        async with aiohttp.ClientSession() as session:
            pass
        return web.json_response({'ok': True})

    except Exception:
        super_logger.error('Error get_order_user', exc_info=True)


async def add_new_order(request):
    try:
        async with aiohttp.ClientSession() as session:
            pass
        return web.json_response({'ok': True})

    except Exception:
        super_logger.error('Error add_new_order', exc_info=True)


async def get_shop(request):
    try:
        async with aiohttp.ClientSession() as session:
            pass
        return web.json_response({'ok': True})

    except Exception:
        super_logger.error('Error get_shop', exc_info=True)

