let plusOne = function(digits){
	for(let i = digits.length - 1; i >= 0; i--){
		if(digits[i] == 9){
			digits[i] = 0;
		}
		else{
			digits[i] += 1;
			return digits;
		}
	}
	if(digits[0] == 0){
		digits.unshift(1);
	}
	return digits;
}

const readline = require('readline');
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(array){
	array = array.split(' ').map(function(value){
		return Number(value);
	});
	let result = plusOne(array);
	console.log(result);
	read.close();
});

read.on("", function(){
	process.exit(0);
});
