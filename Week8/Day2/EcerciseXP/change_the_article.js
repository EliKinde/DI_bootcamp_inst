//🌟 Exercise 1 : Change The Article

// 1. Using a DOM property, retrieve the h1 and console.log it.
let h1 = document.getElementsByTagName('h1')[0];
console.log(h1);


// 2. Using DOM methods, remove the last paragraph in the <article> tag.
let pp = document.getElementById('pp');
pp.remove('pp');

// 3. Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
let h2 = document.getElementsByTagName('h2')[0];
h2.addEventListener('click', color);
function color() {
    h2.style.color = "red";
}


// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let h3 = document.getElementsByTagName('h3')[0];
h3.addEventListener('click', hideOnClick);
function hideOnClick() {
    h3.style.display = 'none';
}

// 5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click', boldFont)
let arti = document.querySelectorAll('p');
function boldFont() {
    for (let index = 0; index < arti.length; index++) {
        arti[index].style.fontWeight = 'bold';
    }
}

// 6. BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
function getRandomSize() {
    return Math.floor(Math.random() * 101);
}

h1.addEventListener('mouseover', randomSize);
function randomSize() {
    randomFontSize = getRandomSize();
    h1.style.fontSize = `${randomFontSize}px`;
};

// 7. BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)


