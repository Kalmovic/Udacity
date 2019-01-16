var cats = [
    {name: 'Fluffy', count: 0, image: 'images/cat_picture1.jpg'},
    {name: 'Robert', count: 0, image: 'images/cat_picture2.jpg'}
];

var $catname = $('.catname');
var $clicks = $('#clicks');
var $pic = $('#pic');
var $page = $('#page');
var $aside = $('#aside');
var $selectedCat = $('.selectedCat');

for (var i = 0; i < cats.length; i++){
    var cat = cats[i];
    var node = document.createElement("h4");
    node.setAttribute("type", "text");
    var cattext = document.createTextNode(cat.name);
    node.appendChild(cattext);
    document.querySelector('.catname').appendChild(node);
    var imgcat = document.querySelector("#image");
    
    node.addEventListener('click', (function(cattextCopy){
        return function() {
            $selectedCat.text(cattextCopy.nodeValue);
            $clicks.text(parseInt(cat.count));
            imgcat.setAttribute("src", cat.image);
            document.img.appendChild(imgcat);
            //alert(cattextCopy.nodeValue);
        };
    })(cattext));

}
