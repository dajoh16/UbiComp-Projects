var express = require('express');
var router = express.Router();


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/api/status', function(req, res, next) {

});

router.get('/api/status/:id', function(req, res, next) {

});

router.post('/api/in/:id', function (req, res, next) {

});

router.post('/api/out/:id', function (req, res, next) {

});

module.exports = router;

