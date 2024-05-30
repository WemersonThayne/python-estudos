from http.server import HTTPServer
from config import log_config as logging
from config.SimpleHTTPRequestHandler import HTTPRequestHandler


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8080):
    logging.logging_config()
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.logger.info(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
