// 🌟 Exercise 8 : Juice Bar

function makeJucie(size) {
  let ingredients = [];


  function addIngredients(fIngredient, sIngredient, tIngredient) {
    console.log(`The client wants a ${size} juice, containing ${fIngredient}, ${sIngredient}, ${tIngredient}`);
    ingredients.push(fIngredient, sIngredient, tIngredient);
  }

  function displayJuice() {
    let div = document.createElement('div');

    div.textContent= `The client wants a ${size} juice, containing ${ingredients[0]}, ${ingredients[1]}, ${ingredients[2]}.\n The client wants a ${size} juice, containing ${ingredients[3]}, ${ingredients[4]}, ${ingredients[5]}`;
    document.body.appendChild(div);
  }

  addIngredients('apple', 'lemon', 'greep');
  addIngredients('mango', 'cenimon', 'banana');
  displayJuice();
}

 makeJucie('small');


