var options = {
  valueNames: [ 'departure', 'destination', 'date', 'time', 'cost', 'seatsAvailable' ]
};

var userList = new List('journey', options);
var month = new Array();
month[0] = "January";
month[1] = "February";
month[2] = "March";
month[3] = "April";
month[4] = "May";
month[5] = "June";
month[6] = "July";
month[7] = "August";
month[8] = "September";
month[9] = "October";
month[10] = "November";
month[11] = "December";

cheapRides.onclick=(function() {
	if(document.getElementById("cheapRides").checked) {
		userList.filter(function(item) {
			if (item.values().cost < 5) {
				return true;
			} else {
				return false;
			}
		});
	} else {
		userList.filter();
	}
});

seatNo.onclick=(function() {
	if(document.getElementById("seatNo").checked) {
		userList.filter(function(item) {
			if (item.values().seatsAvailable > 1) {
				return true;
			} else {
				return false;
			}
		});
	} else {
		userList.filter();
	}
});

todaysRides.onclick=(function() {
	var today = new Date();
	var dd = today.getDate();
	var mm = month[today.getMonth()]; //January is 0!
	var yyyy = today.getFullYear();

	if(dd<10) {
		dd='0'+dd
	} 

	if(mm<10) {
		mm='0'+mm
	} 

	today = mm+' '+dd+', '+yyyy;
	
	if(document.getElementById("todaysRides").checked) {
	userList.filter(function(item) {
		if (item.values().date == today) {
			return true;
		} else {
			return false;
		}
	});
	} else {
		userList.filter();
	}
});