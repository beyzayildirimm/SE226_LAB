#include<iostream>
using namespace std;
int main() {
    int n;
    cout<<"Please enter a positive integer greater than 9:";
    cin>> n;

    int steps=0;
    cout<< n;

    while (n>=10) {
        int sum =0;
        while (n>0) {
            sum+=n%10;
            n/=10;
        }
        n=sum;
        steps++;
        cout<< "-> "<< n;
    }

    cout<< endl;
    cout<<"Final value: "<< n<< endl;
    cout<< "Total steps: "<<steps<< endl;


    //------------------------------------------------

    int a;

    // Input validation
    cout << "Please enter a number between 10 and 100: ";
    cin >> a;

    while (a < 10 || a > 100) {
        cout << "Invalid input. Please enter a number between 10 and 100: ";
        cin >> a;
    }

    int fizz= 0;
    int buzz= 0;
    int fizzbuzz= 0;

    for (int i= 1; i<= a; i++) {

        if (i % 7 == 0) {
            cout << "(" << i<< " is skipped)" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }
        else { cout << i << endl; }
    }
    cout << "--- Summary ---" << endl;
    cout << "Fizz count : " << fizz << endl;
    cout << "Buzz count : " << buzz << endl;
    cout << "FizzBuzz count : " << fizzbuzz << endl;

//-----------------------------------------------------------

    int z;
    cout << "Please enter a number between 3 and 9: ";
    cin >> z;

    while (z< 3 || z> 9) {
        cout << "Please enter a number between 3 and 9: ";
        cin >> z;
    }

    for (int i= 1; i<= 2*z - 1; i++) {

        int d= z - i;

        if (d< 0)
            d= -d;
        int k= z- d;

        for (int j= 1; j <= k; j++) {
            cout << j;
        }

        cout << endl;
    }

    return 0;
}