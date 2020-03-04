var express = require('express');
var pgp = require('pg-promise')({});
var router = express.Router();
var db = pgp('postgres://postgres:dininfo1@167.172.184.103:5432/postgres')

router.post('/create', function(req, res, next) {
    //Name,
    let name = req.body.name;
    db.none("INSERT INTO \"user\" (name) values ($1)", name)
        .then(() => {
            res.status(200).send(`Created user ${name}`);
        })
        .catch(err => {
            res.status(500).send(err)
        });
});

module.exports = router;