/*
Input Format:

First line contains an integer Q denoting the number of queries . 
A Query Q is of 4 Types
(i)    1 1 x    (a query of this type means  pushing 'x' into the stack 1)
(ii)   1 2      (a query of this type means to pop element from stack1  and print the poped element)
(iii)  2 1 x  (a query of this type means pushing 'x' into the stack 2)
(iv)  2 2     (a query of this type means to pop element from stack2 and print the poped element)
The second line contains Q queries seperated by space.

Example:

6
1 1 2 1 1 3 2 1 4 1 2 2 2 2 2
*/

#include<bits/stdc++.h>
using namespace std;

class twoStacks
{
    int *arr;
    int size;
    int top1, top2;
public:
   twoStacks(int n=100){size = n; arr = new int[n]; top1 = -1; top2 = size;}
 
   void push1(int x);
   void push2(int x);
   int pop1();
   int pop2();
};



int main(){
    
    twoStacks *sq = new twoStacks();

    int Q;
    cin>>Q;
    while(Q--){
        int stack_no;
        cin>>stack_no;
        int QueryType=0;
        cin>>QueryType;
        
        if(QueryType==1)
        {
            int a;
            cin>>a;
            if(stack_no ==1)
            sq->push1(a);
            else if(stack_no==2)
            sq->push2(a);

        }else if(QueryType==2){

        	if(stack_no==1)
            cout<<sq->pop1()<<" ";
            else if(stack_no==2)
            cout<<sq->pop2()<<" ";

        }
    }
    cout<<endl;
    
}






//Function to push an integer into the stack1.
void twoStacks :: push1(int x)
{
    arr[++top1] = x;
}
   
//Function to push an integer into the stack2.
void twoStacks ::push2(int x)
{
    arr[--top2] = x;
}
   
//Function to remove an element from top of the stack1.
int twoStacks ::pop1()
{
    if (top1 == -1) return -1;
    return arr[top1--];

}

//Function to remove an element from top of the stack2.
int twoStacks :: pop2()
{
    if (top2 == size) return -1;
    return arr[top2++];

}

