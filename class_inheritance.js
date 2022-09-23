class School{
  constructor(name, level, numberOfStudents){
    this._name = name;
    this._level = level;
    this._numberOfStudents = numberOfStudents;
  }
  get name(){
    return this._name;
  }
  get level(){
    return this._level;
  }
  get numberOfStudents(){
    return this._numberOfStudents;
  }
  set numberOfStudents(newNum){
    if (typeof(newNum) === "number"){
      this._numberOfStudents = newNum;
    }else{
      console.log('Invalid input: numberOfStudents must be set to a Number.');
    }
  }
  quickFacts(){
    console.log(`${this._name} educates ${this._numberOfStudents} at the ${this._level} school level.`);
  }

  static pickSubstituteTeacher(substituteTeachers){
    let lengthOfSubs = substituteTeachers.length;
    let randNum = Math.floor(Math.random() * (lengthOfSubs));
    return substituteTeachers[randNum];
  }
}

// Primary //
class Primary extends School{
  constructor(name, numberOfStudents, pickupPolicy){
    super(name, 'primary', numberOfStudents);
    this._pickupPolicy = pickupPolicy;
  }
  get pickupPolicy(){
    return this._pickupPolicy;
  }
}

// Middle //
class Middle extends School{
  constructor(name, numberOfStudents){
    super(name, 'middle', numberOfStudents);
  }
}

// High //
class High extends School{
  constructor(name, numberOfStudents, sportsTeams){
    super(name, 'high', numberOfStudents);
    this._sportsTeams = sportsTeams;
  }
  get sportsTeams(){
    return this._sportsTeams;
  }
  
}

// Primary School test cases
let subs = ['Jamal Crawford', 'Lou Williams', 'J. R. Smith', 'James Harden', 'Jason Terry', 'Manu Ginobli'];
const lorraineHansbury = new Primary('Lorraine Hansbury', 514, 'Students must be picked up by a parent, guardian, or a family member over the age of 13.');
lorraineHansbury.quickFacts();
let sub = School.pickSubstituteTeacher(subs);
console.log(sub);

// High School test cases
const alSmith = new High('Al E. Smith', 415, ['Baseball', 'Basketball', 'Volleyball', 'Track and Field']);
console.log(alSmith.sportsTeams);
