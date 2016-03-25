function initialize() {

var inputFrom = document.getElementById("departure").innerHTML;
var inputTo = document.getElementById("destination").innerHTML;

inputFrom += ", Glasgow";
inputTo += ", Glasgow";

    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix({
        origins: [inputFrom],
        destinations: [inputTo],
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false
    }, function (response, status) {
        if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") {
            var distance = response.rows[0].elements[0].distance.text;
            var duration = response.rows[0].elements[0].duration.text;
            var dvDistance = document.getElementById("matrix");
           dvDistance.innerHTML = "";
            dvDistance.innerHTML += "Distance: " + distance + " - Duration: " + duration;
 
        } else {
            alert("Unable to find the distance via road.");
        }
    });



}

google.maps.event.addDomListener(window, 'load', initialize);