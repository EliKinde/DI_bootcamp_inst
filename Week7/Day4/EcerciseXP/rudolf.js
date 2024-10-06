const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};

let result = '';
for(let keys in details){
  result += `${keys} ${details[keys]} `;
}

console.log(result);
