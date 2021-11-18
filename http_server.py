import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from user import User
from user_repository import UserRepository

port = 9999

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/members":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html charset=utf-8')
            self.end_headers()
            users = UserRepository.find_all()
            user_list_str = '\n'.join(list(map(lambda u: f'<li>{str(u)}</li>', users)))
            self.wfile.write(f'''
            <html>
            <head>
              <meta charset="utf-8" />
              <title>user list</title>    
            </head>
            <body>
              <ul>
                {user_list_str}
              </ul>
            </body>
            </html>
            '''.encode('utf-8'))

    def do_POST(self):
        if self.path == "/members/save":
            content_length = self.headers.get("Content-Length")
            body = self.rfile.read(int(content_length)).decode('utf-8')
            p_dict = {}
            for param in body.split('&'):
                print(param)
                (key, value) = param.split('=')
                p_dict[key] = value
            try:
                user = User(p_dict['id'], p_dict['password'], p_dict['name'])
                UserRepository.create_user(user)
                print(f'user joined : {user}')
                self.send_response(201)
                self.send_header('Content-Type', "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(p_dict).encode('utf-8'))
            except Exception as e:
                print(e)



httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
print(f'Server running on port:{port}')
httpd.serve_forever()