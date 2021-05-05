from helpers.config.setup import Setup
from helpers.config.server import Server

setup = Setup()
server = Server()

server.setupCors()
server.startRoutes()
server.startApp()
