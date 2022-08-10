let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => Math.floor(Math.random() * 10);



function compareGuesses(userGuess, computerGuess, secretTarget){
  let userAbs = Math.abs(userGuess - secretTarget);
  let computerAbs = Math.abs(computerGuess - secretTarget);
  if (userAbs <= computerAbs){
    console.log('the user wins!');
    return true;
  }else{
    console.log('the computer wins');
    return false;
  }
}

const updateScore = winner => winner === 'human' ? humanScore++ : computerScore++;

const advanceRound = () => currentRoundNumber++;
