function generate(numRows: number): number[][] {
  let result = [[1]];

  for (let i = 1; i < numRows; i++) {
    let newArr = [1];
    let prevRow = result[i - 1];

    for (let j = 1; j < prevRow.length; j++) {
      newArr.push(prevRow[j] + prevRow[j - 1]);
    }

    newArr.push(1);
    result.push(newArr);
  }

  return result;
}
