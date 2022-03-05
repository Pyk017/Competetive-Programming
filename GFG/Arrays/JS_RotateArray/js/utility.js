function arrayToString(array) {
  return array.join(" ");
}

function stringToArray(array) {
  return array
    .trim()
    .split(" ")
    .map((val) => parseInt(val));
}

export { arrayToString, stringToArray };
