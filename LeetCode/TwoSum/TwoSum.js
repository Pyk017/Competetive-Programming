let twoSums = function (arr, target){
	map = {};
	for(let i = 0; i<arr.length; i++){
		temp = target - arr[i];
		if(temp in map){
			return [map[temp], i];
		}
		else{
			map[arr[i]] = i;
		}
	}
};

// User Input using readline module

const readline = require("readline");
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question("Array input: ", function(name){
	read.question("target : ", function(country){
		temp = name.split(' ');
		arr = temp.map(function(value){
			return Number(value);
		});
		let result = twoSums(arr, +country);
		console.log(result);
		read.close();
	});
});

read.on("close", function(){
	process.exit(0);
});