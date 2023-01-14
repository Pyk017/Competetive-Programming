let removeDublicate = function(nums){
	let i = 0;
	for(let j = 0; j<nums.length; j++){
		if(nums[i] != nums[j]){
			i++;
			nums[i] = nums[j];
		}
	}
	return i + 1;
};

const readline = require('readline');
const read =  readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(array){
	let temp = array.split(" ");
	let arr = temp.map(function(value){
		return Number(value);
	});
	let result = removeDublicate(arr);
	console.log(result);
});

read.on("close", function(){
	process.exit(0);
});