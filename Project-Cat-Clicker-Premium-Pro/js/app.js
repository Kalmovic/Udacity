
var model = {
    currCat: null,
    adminActive: false,
    cats: [
        {
            name: 'Fluffy',
            count: 0,
            image: 'images/cat_picture1.jpg'
        },
        {
            name: 'Robert',
            count: 0,
            image: 'images/cat_picture2.jpg'
        },
        {
            name: 'Tiger',
            count: 0,
            image: 'images/cat_picture3.jpg'
        },
        {
            name: 'Oscar',
            count: 0,
            image: 'images/cat_picture4.jpg'
        },
        {
            name: 'Max',
            count: 0,
            image: 'images/cat_picture5.jpg'
        }
    ]
};

var octupus = {
    init: function(){
        model.currCat = model.cats[0];
        catListView.init();
        catView.init();
        adminView.init();
        adminView.hide();
    },

    getCurrentCat: function(){
        return model.currCat;
    },

    getCats: function(){
        return model.cats;
    },

    setCurrentCat: function(cat){
        model.currCat = cat;
    },

    incrementCounter: function(){
        model.currCat.count++;
        catView.render();
        adminView.render();
    },
    
    displayAdmin: function(){
        if (model.adminActive === false){
            model.adminActive = true;
            adminView.show();
        }
        else if (model.adminActive === true){
            model.adminActive = false;
            adminView.hide();
        }
    },

    changeCat: function(){
        model.currCat.name = adminCatName.value;
        model.currCat.image = adminImg.value;
        model.currCat.count = adminClicks.value;
        catView.render();
        catListView.render();
        adminView.hide();
    },

    cancelAdmin: function(){
        adminView.hide();
    }
    
};

var catView = {
    init: function(){
        this.$clicks = $('#clicks');
        this.$pic = $('#image');
        this.$selectedCat = $('.selectedCat');

        this.$pic.click(function(){
            octupus.incrementCounter();
        });

        this.render();
    },
    render: function(){
        var currCat = octupus.getCurrentCat();
        this.$selectedCat.text(currCat.name);
        this.$clicks.text(currCat.count);
        this.$pic.attr("src", currCat.image);
    }
}

var catListView = {
    init: function(){
        this.catlist = document.getElementById('cat-list');
        this.form = document.getElementById('form');  
        this.render();
    },

    render: function(){
        var cats = octupus.getCats();
        this.catlist.innerHTML = '';
        for (var i = 0; i < cats.length; i++){
            var cat = cats[i];
            var elem = document.createElement('li');
            elem.textContent = cat.name;

            elem.addEventListener('click',(function(catCopy){
                return function(){
                    octupus.setCurrentCat(catCopy);
                    catView.render();
                };
            })(cat));
            this.catlist.appendChild(elem);
        }
    }
};

var adminView = {
    init: function(){
        this.adminCatName = document.getElementById('adminCatName');
        this.adminImg = document.getElementById('adminImg');
        this.adminClicks = document.getElementById('adminClicks');
        this.cancel = document.getElementById('cancel');
        this.change = document.getElementById('change');
        this.showAdmin = document.getElementById('showAdmin');
        var adminArea = document.getElementById('adminArea');

        this.showAdmin.addEventListener('click',function(){
            octupus.displayAdmin();
        });

        this.change.addEventListener('click', function(){
            octupus.changeCat();
        });

        this.cancel.addEventListener('click', function(){
            octupus.cancelAdmin();
        });

        this.render();
    },

    render: function(){
        var currCat = octupus.getCurrentCat();
        this.adminCatName.value = currCat.name;
        this.adminImg.value = currCat.image;
        this.adminClicks.value = currCat.count;
    },

    show: function(){
        adminArea.style.display = 'block';
    },

    hide: function(){
        adminArea.style.display = 'none';
    }
};

octupus.init();
