const fs = require('fs')
const http = require('http')

http.createServer((req, res)=>{
    fs.readFile('./demo.txt','utf-8',(err, data)=>{
        if (err) {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Error reading file');
            return;
        }

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(data);
    })
}).listen(3001)

fs.appendFile('./demo.txt', 'New Content', (err)=>{
    if(err){
        console.log(err)
    }
})