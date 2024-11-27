const pricePrefix = "";

const API = {
    key : "fca_live_BYOK83s2qtf3Lf99SGERrqdon4AlnsNaq9b7wF76",
    serviceUrl : "https://api.freecurrencyapi.com/v1/latest"
}

function convert(quantity, toDivise) {
    let url = API.serviceUrl + "?apikey=" + API.key + "&currencies="+toDivise;
    console.log(url);
    fetch(url).then(response => response.json()).then(json => {
        let data = json.data;
        let divise = Object.keys(data)[0];
        let convertedPrice = quantity * data[divise];
        convertedPrince = Math.round(convertedPrice * 100) / 100;
        precioDiv.innerHTML = convertedPrice + " " + divise;
    });
}

let precioDiv = document.getElementById("precio");
let precio = parseInt(precioDiv.innerHTML);

//Modificar el precio
document.addEventListener('DOMContentLoaded', () => {
    var selectElement = document.getElementById('coin');
    
    selectElement.addEventListener('change', function() {
        var selectedValue = selectElement.value;
        console.log('Selected currency:', selectedValue);
        // Aquí puedes hacer lo que necesites con el valor seleccionado
        console.log(precio);
        convert(precio, selectedValue);
    });
});


precioDiv.innerHTML = precio + " USD";
