const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let name = '';
let k = 0;

for(let i=0; i < names.length; i++) {
  name += names[i][k];
}

name = name.split('').sort().join('');
console.log(name);
