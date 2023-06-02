var botao_direita = document.querySelector('#mudar_direita');
var botao_esquerda = document.querySelector('#mudar_esquerda');
var miniaturas = document.querySelectorAll('#fotos img');

var index = 0;

function atualizarImagemPrincipal() {
  var elementosFoto = document.querySelectorAll('.card');
  elementosFoto.forEach(function(elemento, elementoIndex) {
    if (elementoIndex === index) {
      elemento.classList.add('ativa');
    } else {
      elemento.classList.remove('ativa');
    }
  });
  var novaImagem = miniaturas[index].src;
  document.querySelector('.card.ativa').src = novaImagem;
}

botao_direita.addEventListener('click', function() {
  index = (index + 1) % miniaturas.length;
  atualizarImagemPrincipal();
});

botao_esquerda.addEventListener('click', function() {
  index = (index - 1 + miniaturas.length) % miniaturas.length;
  atualizarImagemPrincipal();
});

miniaturas.forEach(function(miniatura, miniaturaIndex) {
  miniatura.addEventListener('click', function() {
    index = miniaturaIndex;
    atualizarImagemPrincipal();
  });
});