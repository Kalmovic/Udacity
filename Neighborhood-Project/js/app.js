var places = [
    {title: 'Pedra da Gávea', location: {lat: -22.9978723, lng: -43.2847223}},
    {title: 'Secreto da Pedra Bonita', location: {lat: -22.9784277, lng: -43.2849961}},
    {title: 'Escadaria Selarón', location: {lat: -22.9153106, lng: -43.1792038}},
    {title: 'Vista Chinesa', location: {lat: -22.9732422, lng: -43.249444}},
    {title: 'Mirante do Leblon', location: {lat : -22.9899755, lng : -43.2273807}},
    {title: 'Parque Lage', location: {lat: -22.9581535, lng: -43.2116429}},
    {title: 'Píer dos Pedalinhos', location: {lat: -22.975312, lng: -43.201407}},
    {title: 'Cristo Redentor', location: {lat: -22.951580, lng: -43.210122}},
    {title: 'Mirante', location: {lat: -22.9412752, lng: -43.2840333}},
    {title: 'Praia da Reserva', location: {lat: -23.012947, lng: -43.391236}}

];

var styles = [
    {
        featureType: "water",
        elementType: "geometry",
        stylers: [
            { color: "#e9e9e9" },
            { lightness: 17 }
        ]
    },
    {
        featureType: "landscape",
        elementType: "geometry",
        stylers: [
            { color: "#f5f5f5" },
            { lightness: 20 }
        ]
    },
    {
        featureType: "road.highway",
        elementType: "geometry.fill",
        stylers: [
            { color: "#ffffff" },
            { lightness: 17 }
        ]
    },
    {
        featureType: "road.highway",
        elementType: "geometry.stroke",
        stylers: [
            { color: "#ffffff" },
            { lightness: 29 },
            { weight: 0.2 }
        ]
    },
    {
        featureType: "road.arterial",
        elementType: "geometry",
        stylers: [
            { color: "#ffffff" },
            { lightness: 18 }
        ]
    },
    {
        featureType: "road.local",
        elementType: "geometry",
        stylers: [
            { color: "#ffffff" },
            { lightness: 16 }
        ]
    },
    {
        featureType: "poi",
        elementType: "geometry",
        stylers: [
            { color: "#f5f5f5" },
            { lightness: 21 }
        ]
    },
    {
        featureType: "poi.park",
        elementType: "geometry",
        stylers: [
            { color: "#dedede" },
            { lightness: 21 }
        ]
    },
    {
        elementType: "labels.text.stroke",
        stylers: [
            { visibility: "on" },
            { color: "#ffffff" },
            { lightness: 16 }
        ]
    },
    {
        elementType: "labels.text.fill",
        stylers: [
            { saturation: 36 },
            { color: "#333333" },
            { lightness: 40 }
        ]
    },
    /*{
        elementType: "labels.icon",
        stylers: [
            { visibility: "off" }
        ]
    },*/
    {
        featureType: "transit",
        elementType: "geometry",
        stylers: [
            { color: "#f2f2f2" },
            { lightness: 19 }
        ]
    },
    {
        featureType: "administrative",
        elementType: "geometry.fill",
        stylers: [
            { color: "#fefefe" },
            { lightness: 20 }
        ]
    },
    {
        featureType: "administrative",
        elementType: "geometry.stroke",
        stylers: [
            { color: "#fefefe" },
            { lightness: 17 },
            { weight: 1.2 }
        ]
    }
];

var map;

var clickedMarker = new Boolean(false);

var createMarker = function(data){
    var that = this;
    that.title = data.title;

    // Create Info Window
    var largeInfowindow = new google.maps.InfoWindow();

    var icon = {
        "url": "img/instagram.png",
        scaledSize: new google.maps.Size(20, 20), // scaled size
        origin: new google.maps.Point(0,0), // origin
        anchor: new google.maps.Point(0,0) // anchor
    }
    // Create a marker per location, and put into markers array.
    that.marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(data.location.lat, data.location.lng),
        title: that.title,
        icon: icon,
        animation: google.maps.Animation.DROP
    });
    // Create an onclick event to open an infowindow at each marker.
    that.setMarker = function(){
        google.maps.event.trigger(that.marker, 'click');
    };

    that.marker.addListener('click', function(){
        /*if (clickedMarker== false){
            clickedMarker = true;
            setInfoWindow(that, largeInfowindow);
            map.setZoom(15);
            map.setCenter(that.marker.getPosition());
            var cityCircle = new google.maps.Circle({
                strokeColor: '#bc1888',
                strokeOpacity: 0.5,
                strokeWeight: 2,
                fillColor: '#bc1888',
                fillOpacity: 0.001,
                map: map,
                center: that.marker.getPosition(),
                radius: 1000 // 1km
            });

            if (that.marker.getAnimation() !== null){
                that.marker.setAnimation(null);
            } else {
                that.marker.setAnimation(google.maps.Animation.BOUNCE);
            }
        } else {
            that.marker.removeListener('click');
        }*/
        that.marker.addListener('click', function(){
            setInfoWindow(this, largeInfowindow);
        });
    });


};


var setInfoWindow = function (marker, infowindow){
    // Check to make sure the infowindow is not already
    // on this marker
    if (infowindow.marker != marker){
        // Clear the infowindow content to give the streetview time to load.
        infowindow.setContent('');
        infowindow.marker = marker;

        // Make sure the marker property is cleared if the infowindow is closed.
        infowindow.addListener('closeclick', function(){
            infowindow.setMarker = null;
        });
        infowindow.setContent('<div>' + marker.title + '</div>');
        infowindow.open(map, marker);
    };
}

var ViewModel = function(){
    //Makes sure 'self' always refers to ViewModel
    var self = this;

    this.allMarkers = ko.observableArray();

    //Constructor creates a new map - only center and zoom are required
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -22.971711, lng: -43.314694},
        zoom: 12,
        styles: styles,
        mapTypeControl: false
    });

    places.forEach(function(data){
        var addPlace = new createMarker(data);
        self.allMarkers.push(addPlace);
    });

    self.query = ko.observable('');

    this.filteredMarkers = ko.computed(function(){
        return this.allMarkers().filter(function(addPlace){
            var found = addPlace.title.toLowerCase().indexOf(this.query().toLowerCase()) > -1;
            addPlace.marker.setVisible(found);
            return found;
        }, this);
    }, this);
};

function initMap(){
    ko.applyBindings(new ViewModel());
};