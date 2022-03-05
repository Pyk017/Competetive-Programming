
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

/* Function to print an array */
function printArray(arr, size)
{
    let i;
    let s='';
    for (i=0; i < size; i++) {
        s += arr[i] + " ";
    }
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let input_ar0 = readLine().split(' ').map(x=>parseInt(x));
        let n = input_ar0[0];
        let arr = new Array(n);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++)
            arr[i] = input_ar1[i];
        let obj = new Solution();
        obj.sort012(arr, n);
        printArray(arr, arr.length);
    }
}
/**
 * @param {number[]} arr
 * @param {number} N
 * @returns {number[]}
*/

class Solution {
    
    sort012(arr, n)
    {
        let i = 0;

        while (i < n && arr[i] == 0){
            i += 1
        }
            
        

        let j = i
        
        while (j < n){
            while (j < n && arr[j] != 0){
                j += 1
            }
                
                

            if (j < n){
                let temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i += 1;
                j += 1;
            }
        }
        
        let k = 0;
        while (k < n && arr[k] == 0){
            k += 1
        }
            
        i = k
        
        while (i < n && arr[i] == 1){
            i += 1
        }
            
        
        j = i
        
        while (j < n){
            while (j < n && arr[j] != 1){
                j += 1
            }
                
            if (j < n){
                let temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i += 1;
                j += 1;
            }
        }
        
    }
}