const http = require('node:http');
const server = http.createServer((_req, res) => {
  res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
  res.end('<h1>Hello World from Node.js</h1>');
});
server.listen(3000, '0.0.0.0');
