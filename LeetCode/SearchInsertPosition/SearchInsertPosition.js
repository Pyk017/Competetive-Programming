let searchInsert = function (nums, target) {
	
  let index = 0;
  if (target > nums[nums.length - 1]) return nums.length;
  
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      return i;
    }
    if (nums[i] > target) {
      return i;                                         
    }
    index = i;
  }
  return index + 1;
};



const readline = require('readline');
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(arr){
	read.question('', function(target){
		arr = arr.split(' ').map(function(value){
			return Number(value);
		});
		let result = searchInsert(arr, target);
		console.log(result);
		read.close();
	});
});