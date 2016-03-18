function initialize() {

var defaultBounds = new google.maps.LatLngBounds(
	new google.maps.LatLng(55.8642, -4.2518)
);

var options = {
	bounds: defaultBounds,
	componentRestrictions: {country: 'gb'}
};

var inputFrom = document.getElementById('travellingFromInput');
var inputTo = document.getElementById('travellingToInput');
var autocompleteFrom = new google.maps.places.Autocomplete(inputFrom, options);
var autocompleteTo = new google.maps.places.Autocomplete(inputTo, options);
}

google.maps.event.addDomListener(window, 'load', initialize);