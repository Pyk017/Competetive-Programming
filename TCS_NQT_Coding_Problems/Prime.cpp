#include<bits/stdc++.h>
using namespace std;

bool prime(int n){
    if(n <= 1)
        return false;

    if(n == 2)
        return true;

    int i = 2;
    while(i * i <= n){
        if (n % i == 0)
            return false;
        i += 1;
    }
    return true;
}

string check(int n){
    string msg;
    if(n < 0){
        msg = "Enter Valid Number!";
    }
    else{
        if(prime(n))
            msg = "It is a Prime Number";
        else
            msg = "It is not a prime Number";
    }
    return msg;
}


int main(){
    int n;
    cout << "Enter an Integer :- " << " ";
    cin >> n;
    string res = check(n);
    cout << res << endl;
    return 0;
}