var burguer = document.querySelector('#burguer');
var menu = document.querySelector('.menu');
var header = document.querySelector('#header');

burguer.addEventListener('click', click_menu);

function click_menu() {
  if (menu.style.display === 'block') {
    menu.style.display = 'none';
    header.style.boxShadow = '';
  } else {
    menu.style.display = 'block';
    header.style.boxShadow = 'none';
  }
}
