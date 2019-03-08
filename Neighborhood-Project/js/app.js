onGMapsError = function() {
  alert('There was an error with the Google Maps. Please try again later.');
};

window.gm_authFailure = () => {
  alert('There was an error with the authentication. Please try again later.');
};

var places = [
    {title: 'Pedra da Gávea', location: {lat: -22.9978723, lng: -43.2847223}},
    {title: 'Escadaria Selarón', location: {lat: -22.9153106, lng: -43.1792038}},
    {title: 'Vista Chinesa', location: {lat: -22.9732422, lng: -43.249444}},
    {title: 'Mirante do Leblon', location: {lat : -22.9899755, lng : -43.2273807}},
    {title: 'Parque Lage', location: {lat: -22.9581535, lng: -43.2116429}},
    {title: 'Píer dos Pedalinhos', location: {lat: -22.975312, lng: -43.201407}},
    {title: 'Cristo Redentor', location: {lat: -22.951580, lng: -43.210122}},
    {title: 'Pico Da Tijuca', location: {lat: -22.9417268, lng: -43.2852504}},
    {title: 'Praia da Reserva', location: {lat: -23.012947, lng: -43.391236}}
];

// This array will style the map
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

var currentInfoWindow = null;

// ------------ FOURSQUARE KEYS --------------
var CLIENT_ID = 'XX1DZGZ0SMRWCAKL1YXPGK40KE1UIA42VDCZQQ3CZ55KQGXW';
var CLIENT_SECRET = 'WIO5ETGFN51FFUZOONSE2Z3LOT5NY0HIMZXFR4G3NYODFOX1';

var createMarker = function(data){
    // Makes sure every that.var belongs to the function
    var that = this;
    that.title = data.title;

    // Create Info Window
    var largeInfowindow = new google.maps.InfoWindow();

    // Creating icon model for each one
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
        // If another InfoWindow is open, clode it and then open the other one
        closeLastOpenedInfoWindow()
        setInfoWindow(this, data, largeInfowindow);
    });
};

var setInfoWindow = function (marker, place, infowindow){
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
      // Starts retrieving data
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
              console.log("Name and ID: "+data.response.venues[0].name+" | "+data.response.venues[0].id);
              this.venueName = data.response.venues[0].name;
              this.venueId = data.response.venues[0].id;
              console.log("Title: " + this.venueName + " | Venue ID: " + this.venueId);
              // A second request for images
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
                  // Retrieves:
                  // User name
                  // User image
                  // Where the image was taken from
                  // Location image

                  var items = data.response.photos.items[0];
                  this.fromName = items.source.name;
                  this.locationPrefix = items.prefix;
                  this.locationSuffix = items.suffix;
                  this.locationImgSrc = this.locationPrefix + '300x300' + this.locationSuffix;
                  this.userFirstName = items.user.firstName;
                  this.userLastName = items.user.lastName;
                  this.userFullName = this.userFirstName+' '+this.userLastName;
                  this.userPrefix = items.user.photo.prefix;
                  this.userSuffix = items.user.photo.suffix;
                  this.userImgSrc = this.userPrefix+'50x50'+this.userSuffix

                  console.log("From: " +this.fromName);
                  console.log("imgSrc: "+this.locationImgSrc);
                  console.log("User name: "+this.userFullName);
                  console.log("userSrc: "+this.userImgSrc);

                  // Fills string with html content for InfoWindow
                  var contentString =
                  '<div class="main">'+
                      '<h3 class="venueName">'+place.title+'</h3>'+
                      '<header class="row" id="user">'+
                          '<picture class="col-md-2 text-left">'+
                              '<img src="'+this.userImgSrc+'" id="userImage">'+
                          '</picture>'+
                          '<div class="col-md-10 text-left text-uppercase identity">'+
                              '<h4 id="userName">'+this.userFullName+'</h4>'+
                              '<h6>Retrieved on: '+this.fromName+'</h6>'+
                          '</div>'+
                      '</header>'+
                      '<div class="cat">'+
                          '<img class="img-fluid text-center" id="mainpic" src="'+this.locationImgSrc+'">'+
                      '</div>'+
                  '</div>';

                  infowindow.setContent(contentString);
                  infowindow.open(map, marker);
                  // Sets currentInfoWindow as active
                  currentInfoWindow = infowindow;

              }).fail(function(data){
                  //console.log(data);
                  //this.resError = data.responseJSON.meta.errorDetail;
                  //console.log(this.resError);
                  alert("Error: There was an error with the connection with Foursquare API. Please try again later");
              });
          }).fail(function(data){
            //console.log(data);
            //this.resError = data.responseJSON.meta.errorDetail;
            //console.log(this.resError);
            alert("Error: There was an error with the connection with Foursquare API. Please try again later");
          });
      }
}

var closeLastOpenedInfoWindow = function() {
    if (currentInfoWindow) {
        currentInfoWindow.close();
    }
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

    // Filters the list of location according to the search and
    // displays the filterd list as well in the map
    this.filteredMarkers = ko.computed(function(){
        return this.allMarkers().filter(function(addPlace){
            var found = addPlace.title.toLowerCase().indexOf(this.query().toLowerCase()) > -1;
            addPlace.marker.setVisible(found);
            return found;
        }, this);
    }, this);
};

// Go
function initMap(){
    ko.applyBindings(new ViewModel());
};
