#!/usr/bin/env python3 

from http.server import HTTPServer,BaseHTTPRequestHandler


tasks =["Task1","Task2","Task3","Task4","Task5"]

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/tasklist"):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            

            out = ""
            out += "<html><body>"
            out += "<h1>Task List</h1>"
            out += "<h3><a href='/tasklist/new'> Add New Tasks</a><h3>"
            for task in tasks:
                out += task
                out += "</br>"
            out += "</body></html>"
            self.wfile.write(out.encode())
        
        if self.path.endswith("/tasklist/new"):

            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            

            out = ""
            out += "<html><body>"
            out += "<h1>ADD NEW TASK</h1>"
            
            out += "<form method='POST' enctype='multipart/form-data' action='/tasklist/new'> "
            out += "<input name='task' type='test' placeholder='Add new task'>"
            out += "<input type='submit' value='Add'>"
            out += "</form>"
            out += "</body></html>"
            
            self.wfile.write(out.encode())
    

def main():
    PORT = 8000
    server = HTTPServer(("",PORT), helloHandler)
    print("Server running on port {}".format(PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()