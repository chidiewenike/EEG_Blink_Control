'use strict';
var http = require('http');
var port = process.env.PORT || 1337;
var thinkgear = require('../index.js');
var client = thinkgear.createClient();
client.connect();

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });

    client.on('blink_data', function (blink_data)
    {
        res.end(JSON.stringify(blink_data));
    });

}).listen(port);







