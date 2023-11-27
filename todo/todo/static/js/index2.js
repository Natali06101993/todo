let pokupka = {
    "агуша": 1,
    "виноград": 1,
    "вискас": 1,
    "огурцы": 1,
    "пельмени": 1,
    "плов": 1,
    "порошок": 1,
    "сыр": 1,
    "холодильник": 1,
    "шампунь": 1

};

document.onclick = event => {
    if (event.target.classList.contains("plus")) {
        //console.log(event.target.dataset.id);
        plusFunction(event.target.dataset.id);
    }
    if (event.target.classList.contains("minus")) {
        minusFunction(event.target.dataset.id);
    }
}
//увеличение кол-ва товарва
const plusFunction = id => {
    //console.log(goods);
    pokupka[id]++;
    renderPokupka();
}

//уменьшение товара
const minusFunction = id => {
    if (to[id] - 1 == 0) {
        deleteFunction(id);
        return true;
    }
    pokupka[id]--;
    renderPokupka();
}
//удаление товара
const deleteFunction = id => {
    delete pokupka[id];
    renderPokupka();
}

const renderPokupka = () => {
    console.log(pokupka);
}

renderPokupka();




function save() {

}

function itogo() {

}