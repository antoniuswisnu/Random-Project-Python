const http = require('http'), host = 'localhost', port = 3000

const node_server = http.createserver((req,res) => {
    res.end('Hello Fohkin World $(host):$(port)')
})

node_server.listen(port,host,() =>{
    console.log('server berhasil di running...')
})