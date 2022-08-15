const team = {
  _games: [
    { opponent: "Lily", teamPoints: 5, opponentPoints: 3 },
    { opponent: "Robin", teamPoints: 6, opponentPoints: 2 },
    { opponent: "Tracy", teamPoints: 1, opponentPoints: 4 },
  ],

  _players: [
    { firstName: "Ted", lastName: "Mosby", age: 30 },
    { firstName: "Marshal", lastName: "Erikson", age: 30 },
    { firstName: "Barney", lastName: "Stinson", age: 31 },
  ],

  get players() {
    return this._players;
  },

  get games() {
    return this._games;
  },

  addPlayer(newFirstName, newLastName, newAge) {
    let newPlayer = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge,
    };
    this.players.push(newPlayer);
  },

  addGame(newOpponent, newTeamPoints, newOpponentPoints){
    let newGame = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints 
    }
    this.games.push(newGame);
  }
};

team.addPlayer('bugs', 'bunny', 76);
team.addGame('Titans', 100, 98);

console.log(team.games[3])
