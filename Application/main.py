import json
from aiohttp import web
from scripts.server.server import app
from scripts.server.server import get_user
from scripts.server.server import get_order_user
from scripts.server.server import add_new_order
from scripts.server.server import get_shop


def get_config_db() -> tuple:
    """The method getting host and port of configuration file."""
    with open('Application/config.json') as config:
        json_str = config.read()
        json_str = json.loads(json_str)

        host = json_str['server']['host']
        port = json_str['server']['port']
        return (host, port)

host, port = get_config_db()


def main():
    app.router.add_routes([web.post('/get_user', get_user),
                           web.post('/get_order_user', get_order_user),
                           web.put('/add_new_order', add_new_order),
                           web.post('/get_shop', get_shop)])
    web.run_app(app, host=host, port=port) 


if __name__ == "__main__":
    main()