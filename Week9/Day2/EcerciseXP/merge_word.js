// Exercise 1 : Merge Words

function mergeWords(word1) {
    const words = [word1];

    return function nextString(word){
        if (word) {
            words.push(word);
            return nextString;
        } else {
            return words.join(' ');
        }
    };
}


const greet = mergeWords('Hello')('is')('no')('spoon. ');
console.log(greet());

