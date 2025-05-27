function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i=0; i< uiBathrooms.length; i++) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i= 0; i < uiBHK.length; i++) {
        if(uiBHK[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/predict_home_price";
    // var url = "/api/predict_home_price";
    
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location
    },function(data, status) {
        console.log(data.estimate_price);
        uiEstimatePrice.innerHTML = "<h2>" + data.estimate_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}
  
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names";
    // var url = "/api/get_location_names"; 
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        console.log("Response data :",data)
        if(data) {
            var locations = data.location;
            // console.log(locations)
            var uiLocations = document.getElementById("uiLocation");
            $('#uiLocation').empty();
            console.log(uiLocations)
            for(var i= 0; i < locations.length; i++) {
                var opt = new Option(locations[i]);
                $('#uiLocation').append(opt);
            }
        }
    });
}
  
window.onload = onPageLoad;