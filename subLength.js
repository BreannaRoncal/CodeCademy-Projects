
/*
    Write a function subLength() that takes 2 parameters, a string and a single character. 
    The function should search the string for the two occurrences of the character and return 
    the length between them including the 2 characters. If there are less than 2 or 
    more than 2 occurrences of the character the function should return 0.
*/

function subLength(str, char){
  // Check if there is less than 2 or more than 2 occurrences of the char
  let charCount = 0;
  for (let i = 0; i < str.length; i++){
    if ( str[i] === char){
      charCount++;
    }
  }
  if (charCount != 2){
    return 0;
  }

  let count = 0;
  for (let i = 0; i < str.length; i++){
    charCount = 0;

    if (str[i] === char){
      count = 0;
      charCount++;
    }
    for (let j = i + 1; j < str.length; j++){
      count++;
      if (str[j] === char){
        charCount++;
      }
      if(charCount === 2 || 
        (str[j] === str[j + 1])){

        return count;
      }
    }
  }

  return count;
}

console.log(subLength('Saturday', 'a')); // returns 6
console.log(subLength('summer', 'm')); // returns 2
console.log(subLength('digitize', 'i')); // returns 0
console.log(subLength('cheesecake', 'k')); // returns 0);
