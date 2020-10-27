#include<bits/stdc++.h>
using namespace std;

bool check_year(int y){
    if((y % 400 == 0) || ((y % 100 != 0) && (y % 4 == 0)))
        return true;
    return false;
}

int main(){
    int year;
    cout << "Enter Year :- " << " ";
    cin >> year;
    check_year(year)? 
        cout << "It is a Leap Year" << endl :
        cout << "It is not a Leap Year" << endl;
    return 0;
}