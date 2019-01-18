
var model = {
    currCat: null,
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
        //model.currCat = null;
        catListView.init();
        catView.init();
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

octupus.init();
