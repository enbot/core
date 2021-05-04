from helpers.config.server import Server

server = Server()

server.startRoutes()
server.setupCors()
server.startApp()
