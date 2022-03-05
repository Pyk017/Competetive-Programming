'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let arr = new Array(n-1);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n-1;i++)
            arr[i] = input_ar1[i];
        let obj = new Solution();
        console.log(obj.MissingNumber(arr, n));
        
    }
}

/**
 * @param {number[]} array
 * @param {number} n
 * @returns {number}
*/

class Solution{
    MissingNumber(array,n){
        //code here
        let totalSum = n * (n + 1) / 2;
        let sum = array.reduce((acc,val) => acc + val);
        return totalSum - sum;
    }
}