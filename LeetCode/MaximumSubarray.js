let maxSubArray = function(nums){
	let global_max = nums[0];
    let curr_max = nums[0];
    for(let i = 1; i<nums.length; i++){
        curr_max = Math.max(nums[i], curr_max + nums[i]);
        if(curr_max > global_max){
            global_max = curr_max;
        }
    }
    return global_max;
};

const readline = require("readline");
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(array){
	array = array.split(" ").map(function(value){
		return Number(value);
	});
	let result = maxSubArray(array);
	console.log(result);
	read.close();
});

read.on("close"{
	proces.exit(0);
});