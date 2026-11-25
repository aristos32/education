#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int calculateRepetitions(int n);

void example5()
{
    int startRange, endRange;

    int repetitions = 0, maxRepetitions = 0;
    int repetitionsNumber = 0;

    cout << "Enter startRange, endRange:" << endl;
    cin >> startRange >> endRange;

    for(int i=startRange; i<= endRange; i++){

        repetitions = calculateRepetitions(i);
        if(repetitions > maxRepetitions){
            repetitionsNumber = i;
            maxRepetitions = repetitions;
        }
    }

    cout << "max repetitions:" << maxRepetitions << ", for number:" << repetitionsNumber;
}

int calculateRepetitions(int n){

    int repetitions = 1;

    cout << endl << endl <<  "starting n is " << n << endl;

    while(n != 1){

        // if perittos
        if(n%2 == 1){
            n = 3*n + 1;
        }
        else{
            n = n/2;
        }

        cout << "n is " << n << endl;

        repetitions++;
    }

    cout << " repetitions is " << repetitions << endl;

    return repetitions;
}
