let divElement = document.getElementById('navBar');
divElement.setAttribute('id', 'socialNetworkNavigation');

let li = document.createElement('li');
let text = document.createTextNode('Logout');

li.appendChild(text);
let ul = document.querySelector('ul');
ul.appendChild(li);

let firstEle = ul.firstElementChild;
let lastEle = ul.lastElementChild;

console.log(firstEle.textContent;
lastEle.textContent;
