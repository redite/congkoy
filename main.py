#!/usr/bin/env python
from engine.http import initialize
from engine.config import CongkoyConfig

server = initialize()


if __name__ == '__main__':
    server.run(port=CongkoyConfig.PORT)