let removeElement = function(array, val){

	let targetCount = array.filter(x => x == val).length;
	let non_targetCount = array.length - targetCount;
	let i = 0;
	let n = array.length;
	while (i < n){
		if(array[i] == val){
			array.splice(i, 1);
			n -= 1;
		}
		else{
			i += 1;
		}
	}
	// console.log(array);
	return non_targetCount;
};


const readline = require('readline')
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(arr){
	read.question('', function(val){
		arr = arr.split(" ");
		let temp = arr.map(function(value){
			return Number(value);
		});
		let result = removeElement(arr, val);
		console.log(result);
		read.close();
	});
});

read.on("close", function(){
	process.exit(0);
});