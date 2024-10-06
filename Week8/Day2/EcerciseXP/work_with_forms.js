// 1. Retrieve thr form and console.log it.
let form = document.getElementsByTagName('form')[0];
console.log(form);

// 2. Retrieve the inputs by their id and console.log them.
let inputForm = document.querySelectorAll('#fname, #lname');
console.log(inputForm);


// 3. Retrieve the inputs by their name attribute and console.log them.
let fnameAtt = document.querySelector("[name=firstname]");
let lnameAtt= document.querySelector("[name=lastname]");
console.log(fnameAtt, lnameAtt);


// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

