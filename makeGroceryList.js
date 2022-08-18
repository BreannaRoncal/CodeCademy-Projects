/*
    Write a function groceries() that takes an array of object literals of grocery items. 
    The function should return a string with each item separated by a comma except the last 
    two items should be separated by the word 'and'. Make sure spaces (' ') are inserted 
    where they are appropriate.
*/

function groceries(arr){
  let groceryArr = [];
  arr.forEach(key =>{ 
    return groceryArr.push(key.item)});

    //console.log(groceryArr);
  let list = ''
  if (groceryArr.length > 1){
    list = groceryArr.slice(0, -1).join(', ') + ' and ' + groceryArr.slice(-1);
  }else{
    list = groceryArr.join();
  }
  console.log(list);
  return list;
}

let groceryList =  [{item: 'Bread'}, {item: 'Butter'}];

groceries(groceryList);

/* Examples

groceries( [{item: 'Carrots'}, {item: 'Hummus'}, {item: 'Pesto'}, {item: 'Rigatoni'}] );
// returns 'Carrots, Hummus, Pesto and Rigatoni'
 
groceries( [{item: 'Bread'}, {item: 'Butter'}] );
// returns 'Bread and Butter'
 
groceries( [{item: 'Cheese Balls'}] );
// returns 'Cheese Balls'

*/
