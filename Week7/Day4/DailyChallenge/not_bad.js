//Daily Challenge: Not Bad


let sentence = 'This dinner is not that bad ! You cook well';
//let sentence = 'This denner is bad!';
let wordNot = sentence.search("not");
let wordBad = sentence.search("bad");

if(wordNot === -1) {
  console.log(sentence);
}else if (wordNot < wordBad) {
  let firstPart = sentence.slice(0, wordNot);
  let secondPart = sentence.slice(wordBad + 3);
  console.log(firstPart + "good" + secondPart);
} else {
  console.log(sentence);
}
