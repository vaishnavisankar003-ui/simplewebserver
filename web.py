from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        table {
            width: 60%;
            border-collapse: collapse;
            margin: auto;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        th, td {
            border: 1px solid #ccc;
            padding: 12px;
            text-align: center;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        caption {
            font-size: 1.5em;
            margin-bottom: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <table>
        <caption>TCP/IP Protocol Layers</caption>
        <tr>
            <th>Layer</th>
            <th>Description</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>Provides network services to end-users and applications</td>
            <td>HTTP, FTP, SMTP, DNS</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>Responsible for end-to-end communication and error checking</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>Handles logical addressing and routing of data packets</td>
            <td>IP, ICMP, ARP</td>
        </tr>
        <tr>
            <td>Network Access / Link Layer</td>
            <td>Manages physical addressing and media access</td>
            <td>Ethernet, Wi-Fi, PPP</td>
        </tr>
    </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()