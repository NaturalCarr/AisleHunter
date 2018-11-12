var express = require('express');
var router = express.Router();
const sqlite3 = require('sqlite3').verbose();
var url = require('url');


router.get('/', function(req, res, next) {
	if (req.query.id != null){
	var items = [""];
	var storeName = "";
	var i = 0;
	var sid = req.query.id;
	let aidb = new sqlite3.Database('./public/database/aislehunter.db', (err) => {
			if (err){
				return console.error(err.message);
		}
		console.log('Database Connection Successfully Established');
	}); //Open Database Connection

	aidb.serialize(() => {
		aidb.each("select ITEM.NAME AS INAME, STORE.NAME AS SNAME FROM ITEM,AISLE,POSITION,STORE WHERE ITEM.NAME = POSITION.ITEM AND STORE.ID = POSITION.STOREID AND POSITION.AISLE_NUMBER = AISLE.NUMBER AND POSITION.STOREID = '" + sid + "';", (err, row) => {
			if (err) {console.error(err.message);}
			store(row.INAME, row.SNAME);
			i++;
		}); // end of database.each
	}); //end of database.serialize

	function store(I, S){
		items[i] = I;
		storeName = S;
	}
	aidb.close((err) => {
		if (err){return console.error(err.message);}
res.render('store', {
			title: 'Aisle Hunter',
			store : storeName,
			items : items
		}); //end of res.render
		console.log('Close The Database Connection');
	}); //end of database.close

	} //end of query if-statement

}); // end of router.get

module.exports = router;
