import { animals } from "./animals";
import React from "react";
import ReactDOM from "react-dom";

let title = "";

const showBackground = true;

let images = [];
for (const animal in animals) {
  images.push(
    <img
      key={animal}
      className="animal"
      alt={animal}
      src={animals[animal].image}
      ariaLabel={animal}
      role="button"
      onClick={displayFact}
    />
  );
}
let background = (
  <img className="background" alt="ocean" src="/images/ocean.jpg" />
);

const animalFacts = (
  <div>
    <h1>{title || "Click an animal for a fun fact"}</h1>
    {showBackground && background}
    {<div className="animals">{images}</div>}
    <p id="fact"></p>
  </div>
);

function displayFact(e) {
  let selectedAnimal = e.target.alt;
  const animalInfo = animals[selectedAnimal];
  let factIndex = Math.floor(Math.random() * animalInfo.facts.length);
  let fact = animalInfo.facts[factIndex];
  document.getElementById("fact").innerHTML = fact;
}

ReactDOM.render(animalFacts, document.getElementById("root"));
