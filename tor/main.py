#!/usr/bin/env python3
# encoding: utf-8

# This file is part of Tower of Rapunzel.
#
# Tower of Rapunzel is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tower of Rapunzel is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Tower of Rapunzel.  If not, see <http://www.gnu.org/licenses/>.

"""
A text-based web game for PyWeek 28.

"""
import argparse
import asyncio
import sys

from aiohttp import web
import pkg_resources

import tor


async def get_frame(request):
    return web.Response(
        text="""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="/css/blmst.css" />
</head>
<body>
Boo!
</body>
</html>""",
        content_type="text/html"
    )


def build_app(args):
    app = web.Application()
    app.add_routes([
        web.get("/", get_frame),
    ])
    app.router.add_static(
        "/css/",
        pkg_resources.resource_filename("tor", "static/css")
    )
    return app


def main(args):
    app = build_app(args)
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    handler = app.make_handler()
    f = loop.create_server(handler, args.host, args.port)
    srv = loop.run_until_complete(f)

    print(
        "Serving on {0[0]}:{0[1]}".format(srv.sockets[0].getsockname()),
        file=sys.stderr
    )
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.close()
        loop.run_until_complete(srv.wait_closed())
    loop.close()

def parser(description=__doc__):
    rv = argparse.ArgumentParser(description)
    rv.add_argument(
        "--version", action="store_true", default=False,
        help="Print the current version number.")
    rv.add_argument(
        "--host", default="127.0.0.1",
        help="Set an interface on which to serve."
    )
    rv.add_argument(
        "--port", default=8080, type=int,
        help="Set a port on which to serve."
    )
    return rv


def run():
    p = parser()
    args = p.parse_args()

    rv = 0
    if args.version:
        sys.stdout.write(tor.__version__)
        sys.stdout.write("\n")
    else:
        rv = main(args)

    if rv == 2:
        sys.stderr.write("\n Missing command.\n\n")
        p.print_help()

    sys.exit(rv)


if __name__ == "__main__":
    run()
