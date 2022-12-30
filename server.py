from flask import Flask, request

app = Flask(__name__)

request_count = {}
rate_limit = 10

@app.route('/')
def handle_request():
  client_ip = request.remote_addr
  if client_ip in request_count:
    request_count[client_ip] += 1
  else:
    request_count[client_ip] = 1

  if request_count[client_ip] > rate_limit:
    return "Error: Rate limit exceeded", 429
  else:
    return "Response: OK"

if __name__ == '__main__':
  app.run()
