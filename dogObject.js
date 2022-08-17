// Write your code here:
function dogFactory(name, breed, weight){
  //check that each parameter is a valid type
  if ((typeof name != 'string') && (typeof breed != 'string')){
    console.log('name and breed must be strings');
  }else if(typeof weight != 'number'){
    console.log('weight must be a number');
  }else{
    return {
      _name: name,
      _breed: breed,
      _weight: weight,

      // Getters for each property
      get name(){
        return this._name;
      },

      get breed(){
        return this._breed;
      },

      get weight(){
        return this._weight;
      },

      // Setters for each property, make sure each property is a valid type
      set name(newName){
        if(typeof newName != 'string'){
          console.log('Name must be a string');
        }
        this._name = newName;
      },

      set breed(newBreed){
        if(typeof newBreed != 'string'){
          console.log('Breed must be a string');
        }
        this._breed = newBreed;
      },

      set weight(newWeight){
        if(typeof newWeight != 'number'){
          console.log('Weight must be a number');
        }
        this._weight = newWeight;
      },

      // Dog Methods
      bark(){ 
        return 'ruff! ruff!';
      },

      eatTooManyTreats(){
        this.weight++;
      }
    }
  }
}

  
