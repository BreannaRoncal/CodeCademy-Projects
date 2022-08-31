/*
Context: 
  You’re part of a research team that has found a new mysterious organism at the bottom of the ocean near hydrothermal vents. 
  Your team names the organism, Pila aequor (P. aequor), and finds that it is only comprised of 15 DNA bases. 
  The small DNA samples and frequency at which it mutates due to the hydrothermal vents make P. aequor an interesting specimen to study. 
  However, P. aequor cannot survive above sea level and locating P. aequor in the deep sea is difficult and expensive. 
  Your job is to create objects that simulate the DNA of P. aequor for your research team to study.

*/


// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)] 
}

const returnComplementBase = base => {
  const comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'};
  return comp[base];
}

// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
}

function pAequorFactory(organismNum, DNAArr){
  return{
    specimenNum: organismNum,
    dna: DNAArr,

    // Mutate one base in the DNA sequence
    mutate(){
      let randIndex = Math.floor(Math.random() * 15);
      //console.log('~~~~~~~~~~~~~ randIndex: ' + randIndex)
      let randBase = this.dna[randIndex];

      // mutate the randBase to be a different base
      let newBase = randBase;
      //console.log('newBase and randBase: ' + newBase);
      while (newBase === randBase){
        newBase = returnRandBase();
      }
      this.dna[randIndex] = newBase;
      //console.log('newnewBase: ' + newBase);
    },

    // Compare 2 pAequor's DNA and print what percent of the bases are identical and in the same locations
    compareDNA(otherOrganism){
      let sameDNA = 0;
      for (let i = 0; i < 15; i++){
        if (this.dna[i] === otherOrganism.dna[i]){
          sameDNA++;
        }
      }
      let sameDNAPercent = sameDNA / 15;
      console.log(`specimen #${this.specimenNum} and specimen #${otherOrganism.specimenNum} have ${sameDNAPercent.toFixed(3)}% DNA in common.`);
    },

    // willLikelySurvive if DNA is is made up of at least 'C' or 'G'
    willLikelySurvive(){
      let cOrG = 0;
      for (let i = 0; i < 15; i++){
        //console.log(this.dna[i])
        if ((this.dna[i] === 'C') || (this.dna[i] === 'G')){
          cOrG++;
        }
      }
      let CGPercent = cOrG / 15;
      //console.log(CGPercent);
      return CGPercent >= 0.60 ? true : false;
    },

    // will return a complementary strand:
    // 'A' <--> 'T'
    // 'C' <--> 'G'
    complementStrand(){
      let compStrand =[];
      for (let i = 0; i < 15; i++){
        //console.log(this.dna[i])
        compStrand.push(returnComplementBase(this.dna[i]));
      }
      return compStrand;
    } 
  };
}

/* Test pAequorFactory*/

// Create test org1
let org1MockStrand = mockUpStrand();
let org1 = pAequorFactory(1, org1MockStrand);
// Make sure the pAequorFactory correctly creates the object
console.log(org1.dna);

//Check that .complementStrand() returns the correct complement
console.log('complementaryStrand: ' + org1.complementStrand());

// Create test org2
let org2MockStrand = mockUpStrand();
let org2 = pAequorFactory(2, org2MockStrand);
console.log(org2.dna);
console.log('complementaryStrand: ' + org2.complementStrand());

// Check that .mutate() mutates only one random base
org1.mutate();

// Check that .compareDNA correctly compares 2 specimens
org1.compareDNA(org2);

// Check that .willLikelySurvive returns true or false if the DNA strand has 60% or more 'C' or 'G' in its strand
console.log(org1.willLikelySurvive())
console.log(org2.willLikelySurvive())

// Create 30 instances of pAequor and store them in an array

let pAequorArray = [];
for (let i = 0; i < 30; i++){
  let newP = pAequorFactory(i, mockUpStrand())

  pAequorArray.push(newP);
}

// Check that the entries were pushed to the array
for (elm in pAequorArray){
  console.log(`${elm}: ${pAequorArray[elm].dna}`);
}





