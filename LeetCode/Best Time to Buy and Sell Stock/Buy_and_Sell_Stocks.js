let maxProfit = function(prices){
	let max_profit = 0;
	let min_prices = prices[0];

	for(let i = 0; i<prices.length; i++){
		if(min_prices > prices[i])
			min_prices = prices[i];

		if(max_profit < prices[i] - min_prices)
			max_profit = prices[i] - min_prices;
	}
	return max_profit;
}

let readline = require('readline');
let read = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

read.question("", function(array){
	array = array.split(' ').map((value) => {
		return Number(value);
	});
	let result = maxProfit(array);
	console.log(result);
	read.close();
})

read.close('', function(){
	process.exit();
})
