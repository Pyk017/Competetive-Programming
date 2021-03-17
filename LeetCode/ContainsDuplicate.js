var containsDuplicate = function(nums) {
    let set = new Set();
    
    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i])) {
            return true;
        }
        set.add(nums[i]);
    }
    return false;
};

let readline = require('readline');
let read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(array){
	array = array.split(' ').map((value) => {
		return Number(value);
	});
	let result = containsDuplicate(array);
	console.log(result);
	read.close();
});