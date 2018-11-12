var express = require('express');
var router = express.Router();
const sqlite3 = require('sqlite3').verbose();
var url = require('url');


router.get('/', function(req, res, next) {
	if (req.query.id != null){
	var items = [""];
	var storeName = "";
	var storeAddress = "";
	var storeZip = "";
	var Sun = "Sunday: ";
	var Mon = "Monday: ";
	var Tue = "Tuesday: ";
	var Wed = "Wednesday: ";
	var Thu = "Thuesday: ";
	var Fri = "Friday: ";
	var Sat = "Saturday: ";
	var i = 0;
	var sid = req.query.id;
	let aidb = new sqlite3.Database('./public/database/aislehunter.db', (err) => {
			if (err){
				return console.error(err.message);
		}
		console.log('Database Connection Successfully Established');
	}); //Open Database Connection

	aidb.serialize(() => {
		aidb.each("SELECT ITEM.NAME AS INAME, STORE.NAME AS SNAME FROM ITEM, AISLE, POSITION, STORE WHERE POSITION.STOREID = STORE.ID AND AISLE.STOREID = STORE.ID AND POSITION.STOREID = AISLE.STOREID AND POSITION.ITEM = ITEM.NAME AND AISLE.NUMBER = POSITION.AISLE_NUMBER AND STORE.ID = '" + sid + "';", (err, row) => {
			if (err) {console.error(err.message);}
			storeItems(row.INAME, row.SNAME);
			i++;
		}); // end of database.each

		aidb.each("SELECT SUN_O as SUN_O, SUN_C AS SUN_C, MON_O As MON_O, MON_C AS MON_C, TUE_O AS TUE_O, TUE_C AS TUE_C, WED_O AS WED_O, WED_C AS WED_C, THU_O as THU_O, THU_C as THU_C, FRI_O AS FRI_O, FRI_C AS FRI_C, SAT_O AS SAT_O, SAT_C AS SAT_C, Address as addr, ZIP as zip FROM STORE WHERE STORE.ID = '" + sid + "';", (err, row) =>{
			if (err) {console.error(err.message);}
			storeInfo(row.SUN_O, row.SUN_C, row.MON_O, row.MON_C, row.TUE_O, row.TUE_C, row.WED_O, row.WED_C, row.THU_O, row.THU_C, row.FRI_O, row.FRI_C, row.SAT_O, row.SAT_C, row.addr, row.zip);
		}); //end of database.each

		aidb.each
	}); //end of database.serialize

	function storeInfo(SUN_O, SUN_C, MON_O, MON_C, TUE_O, TUE_C, WED_O, WED_C, THU_O, THU_C, FRI_O, FRI_C, SAT_O, SAT_C, addr, zip){
		Sun += SUN_O + " - " + SUN_C;
		Mon += MON_O + " - " + MON_C;
		Tue += TUE_O + " - " + TUE_C;
		Wed += WED_O + " - " + WED_C;
		Thu += THU_O + " - " + THU_C;
		Fri += FRI_O + " - " + FRI_C;
		Sat += SAT_O + " - " + SAT_C;
		storeAddress = addr;
		storeZip = zip;
	}
	function storeItems(I, S){
		items[i] = I;
		storeName = S;
	}
	aidb.close((err) => {
		if (err){return console.error(err.message);}
res.render('store', {
			title : 'AH - ' + storeName,
			store : storeName,
			items : items,
			Sun : Sun,
			Mon : Mon,
			Tue : Tue,
			Wed : Wed,
			Thu : Thu,
			Fri : Fri,
			Sat : Sat,
			add : storeAddress,
			zip : storeZip
		}); //end of res.render
		console.log('Close The Database Connection');
	}); //end of database.close

	} //end of query if-statement

}); // end of router.get

module.exports = router;
