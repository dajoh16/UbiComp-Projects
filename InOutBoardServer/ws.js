var app = require('app');
var http = require('http').createServer(app);
var io = require('socket.io')(http);

module.exports = io;