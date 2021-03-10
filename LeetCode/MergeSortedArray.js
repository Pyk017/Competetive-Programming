let merge = function(m, n, nums1, nums2){
	nums1 = nums1.splice(0, m).concat(nums2).sort();
	return nums1;
};

const readline = require("readline");
const read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question('', function(m, n){
	read.question('', function(nums1){
		nums1.split(" ").map(function(value){
			return Number(value);
		});

		read.question('', function(nums2){
			nums2.split(" ").map(function(value){
				return Number(value);
			});
			let result = merge(m, n, nums1, nums2);
			console.log(result);
			read.close();

		});
	});

});