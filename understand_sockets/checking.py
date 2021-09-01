import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# ниже после комманды with создается сокет/хост и включается listen
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    # тут мы из _handle_request_noblock попадаем в socket.accept()
    # как я понял, тот принимает соединение на порту, и возвращает
    # себя "socket" при этом хэндлер довольно умный и может все
    # красиво прочитать и распарсить полностью запрос с датой
    # BaseHTTPRequestHandler.parse_request
    # дальше с handle мы вызываем do_GET/POST
    # которые соответсвенно делают крутые штуки с хедерами
    # как я понял, записывая все в файл/IO и отправляя ответ
    # клиенту. Дальше можно возвращаться
    httpd.serve_forever()
