var cats = [
    {name: 'Fluffy', count: 0, image: 'images/cat_picture1.jpg'},
    {name: 'Robert', count: 0, image: 'images/cat_picture2.jpg'},
    {name: 'Tiger', count: 0, image: 'images/cat_picture3.jpg'},
    {name: 'Oscar', count: 0, image: 'images/cat_picture4.jpg'},
    {name: 'Max', count: 0, image: 'images/cat_picture5.jpg'}
];

var $catname = $('.catname');
var $clicks = $('#clicks');
var $pic = $('#image');
var $page = $('#page');
var $aside = $('#aside');
var $selectedCat = $('.selectedCat');

for (var i = 0; i < cats.length; i++){
    var cat = cats[i];
    $catname.append('<li id="cat'+ i +'">'+ cat.name +'</li>');
    $('#cat'+i).click((function(catCopy){
        return function() {
            $selectedCat.text(catCopy.name);
            $clicks.text(parseInt(catCopy.count));
            $pic.attr("src", catCopy.image);
            $pic.click(function(e){
                catCopy.count = $clicks.text();
                $clicks.text(parseInt(catCopy.count)+1);
                return catCopy.count;
            });
        };
    })(cat));
}
