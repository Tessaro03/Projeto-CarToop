var selectFiltros = document.querySelector('#select_filtros')
var filtros = document.querySelector('#filtros')
var main = document.querySelector('main')
var icone_filtro = document.querySelector('#select_filtros>span')
var menu = document.querySelector('.menu')


var motos = document.querySelectorAll('.motos')
var carros = document.querySelectorAll('.carros')
var vans = document.querySelectorAll('.vans')
var caminhoes = document.querySelectorAll('.caminhoes')


selectFiltros.addEventListener('click',click_filtros)



function click_filtros(){
    if (filtros.style.display == 'block'){
        filtros.style.display = 'none'
        icone_filtro.innerHTML = 'arrow_circle_down'

    } 
    else {
        filtros.style.display = 'block'
        icone_filtro.innerHTML = 'arrow_circle_up'
    }
}
