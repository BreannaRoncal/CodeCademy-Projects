// Format numbers with correct commas (a comma ',' character between every 3rd digit)

// export single function
export const formatNumber = num => {
  // turn num into a string to get rid of decimals
  let strNum = String(Math.floor(num));

  // add a comma every 3 digits starting at the end
  for (let i = strNum.length - 3; i > 0; i -= 3){
    strNum = strNum.slice(0, i) + ',' + strNum.slice(i);
  }
  return strNum;
}
