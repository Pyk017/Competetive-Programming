// { Driver Code Starts
//Initial Template for javascript
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
        let sq = new TwoStacks();
        let q = parseInt(readLine());
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        let index = 0;
        let res = '';
        while(q--){
            let stack_no = input_ar1[index++];
            let QueryType = input_ar1[index++];
            if(QueryType == 1){
                let a = input_ar1[index++];
                if(stack_no == 1)
                    sq.push1(a);
                else
                    sq.push2(a);
            }
            else{
                if(stack_no == 1)
                    res += sq.pop1() + " ";
                else
                    res += sq.pop2() + " ";
            }
        }
        console.log(res);
        
    }
}// } Driver Code Ends


//User function Template for javascript

class TwoStacks
{
    
    constructor(){
        this.arr = new Array(100);
        this.size = 100;
        this.top1 = -1;
        this.top2 = 100;
    }
    
    /**
     * @param {number} x
    */
    //Function to push an integer into the stack1.
    push1(x){
        this.arr[++this.top1] = x;
    }
    
    /**
     * @param {number} x
    */
    //Function to push an integer into the stack2.
    push2(x){
        this.arr[--this.top2] = x;
    }
    
    /**
     * @returns {number}
    */
    //Function to remove an element from top of the stack1.
    pop1(){
        if (this.top1 == -1) return -1;
        
        return this.arr[this.top1--];
    }
    
    /**
     * @returns {number}
    */
    //Function to remove an element from top of the stack2.
    pop2(){
        if (this.top2 == this.size) return -1;
        
        return this.arr[this.top2++];
    }
}
