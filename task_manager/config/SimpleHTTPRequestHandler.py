import json
import logging as log
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from tasks.controller.TaskController import TaskController


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.task_controller = TaskController()
        super().__init__(*args, **kwargs)

    def _set_response(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_components = parsed_path.path.split('/')

        if path_components[1] == 'tasks':
             if len(path_components) > 2:
                task_id = path_components[2]
                log.info(f"Received a GET request in /tasks/{task_id}")
                response = self.task_controller.get_task(task_id)
                self._set_response(200)
             else:
                 response = self.task_controller.get_tasks()
                 self._set_response(200)
        else:
                 self._set_response(404)
                 response = {'message': 'Task not found'}

        if path_components[1] == '/category':
            self._set_response(404)
            response = {'message': 'Category not found'}


        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if self.path == '/tasks':
            self._set_response(201)
            response = self.task_controller.create_task(data)
        else:
            self._set_response(404)
            response = {'message': 'Not found'}

        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path == '/tasks':
            task_id = query_params.get('id', [None])[0]
            self._set_response(200)
            response = self.task_controller.update_task(task_id,data)
        else:
            self._set_response(404)
            response = {'message': 'Not found'}

        self.wfile.write(json.dumps(response).encode('utf-8'))


    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path == '/tasks':
            task_id = query_params.get('id', [None])[0]
            self._set_response(200)
            response = self.task_controller.delete_task(task_id)
        else:
            self._set_response(404)
            response = {'message': 'Not found'}

        self.wfile.write(json.dumps(response).encode('utf-8'))
