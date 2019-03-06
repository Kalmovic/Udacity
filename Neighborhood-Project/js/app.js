var places = [
    {title: 'Pedra da Gávea', location: {lat: -22.9978723, lng: -43.2847223}},
    {title: 'Escadaria Selarón', location: {lat: -22.9153106, lng: -43.1792038}},
    {title: 'Vista Chinesa', location: {lat: -22.9732422, lng: -43.249444}},
    {title: 'Mirante do Leblon', location: {lat : -22.9899755, lng : -43.2273807}},
    {title: 'Parque Lage', location: {lat: -22.9581535, lng: -43.2116429}},
    {title: 'Píer dos Pedalinhos', location: {lat: -22.975312, lng: -43.201407}},
    {title: 'Cristo Redentor', location: {lat: -22.951580, lng: -43.210122}},
    {title: 'Pico Da Tijuca', location: {lat: -22.9417268, lng: -43.2852504}},
    {title: 'Praia da Reserva', location: {lat: -23.012947, lng: -43.391236}},
    {title: 'Mirante do Morro Dois Irmãos', location: {lat : -22.9833037, lng: -43.2519733}}

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

var CLIENT_ID = 'XX1DZGZ0SMRWCAKL1YXPGK40KE1UIA42VDCZQQ3CZ55KQGXW';
var CLIENT_SECRET = 'WIO5ETGFN51FFUZOONSE2Z3LOT5NY0HIMZXFR4G3NYODFOX1';

var createMarker = function(data){
    var that = this;
    that.title = data.title;

    // Create Info Window
    //var largeInfowindow = new google.maps.InfoWindow();

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
        map.setCenter(that.marker.getPosition());
        if (that.marker.getAnimation() !== null){
            that.marker.setAnimation(null);
        } else {
            that.marker.setAnimation(google.maps.Animation.BOUNCE);
            setTimeout(function(){ that.marker.setAnimation(null); }, 1400);
        }
        setInfoWindow(this, data);
    });
};


var setInfoWindow = function (marker, place){
    $.ajax({
        url: 'https://api.foursquare.com/v2/venues/search?ll='+place.location.lat +","+place.location.lng,
        type: 'GET',
        dataType: "json",
        data: {
            name: place.title,
            client_id: CLIENT_ID,
            client_secret: CLIENT_SECRET,
            v: '20190301',
            intent: 'checkin',
            radius: '4'
        }
        }).done(function(data){
            //console.log("Name and ID: "+data.response.venues[i].name+" "+i);
            this.venueName = data.response.venues[0].name;
            this.venueId = data.response.venues[0].id;
            console.log("Title: " + this.venueName + " | Venue ID: " + this.venueId);
            $.ajax({
                url: 'https://api.foursquare.com/v2/venues/'+this.venueId+'/photos',
                type: 'GET',
                dataType: 'json',
                group: 'venue',
                data: {
                    client_id: CLIENT_ID,
                    client_secret: CLIENT_SECRET,
                    v: '20190301'
                }
            }).done(function(data, venueName){
                var items = data.response.photos.items[0];
                this.fromName = items.source.name;
                this.locationPrefix = items.prefix;
                this.locationSuffix = items.suffix;
                this.userFirstName = items.user.firstName;
                this.userLastName = items.user.lastName;
                this.userFullName = this.userFirstName+' '+this.userLastName;
                this.locationImgSrc = this.locationPrefix + '50x50' + this.locationSuffix;
                this.userPrefix = items.user.photo.prefix;
                this.userSuffix = items.user.photo.suffix;
                this.userImgSrc = this.userPrefix+'200x200'+this.userSuffix

                console.log("From: " +this.fromName);
                console.log("imgSrc: "+this.locationImgSrc);
                console.log("User name: "+this.userFullName);
                console.log("userSrc: "+this.userImgSrc);
                var modal = document.getElementsByClassName("modal-content");
                modal.innerHTML = [
                    '<div class="modal-header">'+
                        '<h4 class="venueName modal-title">'+ place.title +'</h4>'+
                    '</div>'+
                    '<div class="modal-body">'+
                        '<div class="row" id="user">'+
                            '<img class="col-md-3" src='+this.userImgSrc+' id="userImage">'+
                            '<span id="userName class="col-md-9">Photo by: '+this.userFullName+'</span>'+
                        '</div>'+
                        '<div class="row">'+
                            '<img class="col-md-12" src='+this.locationImgSrc+' id="mainpic">'+
                        '</div>'+
                    '</div>'+
                    '<div class="modal-footer">'+
                        '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'+
                    '</div>'
                ];
            }).fail(function(data){
                console.log(data);
                this.resError = data.responseJSON.meta.errorDetail;
                console.log(this.resError);
                alert("Error: "+this.resError);
            });
        }).fail(function(data){
            console.log(data);
            this.resError = data.responseJSON.meta.errorDetail;
            console.log(this.resError);
            alert("Error: "+this.resError);
        });
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
