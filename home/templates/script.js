// external js: flickity.pkgd.js

var $carousel = $('.carousel').flickity({
  groupCells: true
});

$('.button-group').on( 'click', '.button', function() {
  var index = $(this).index();
  $carousel.flickity( 'selectCell', index );
});