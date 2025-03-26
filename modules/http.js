const http = require('http')

http.createServer((req, res)=>{
    // res.write('Hello World!')
    res.writeHead(200, {
        'Content-Type': 'text/html'
    })
    res.end('Bye Bye')
}).listen(3000)