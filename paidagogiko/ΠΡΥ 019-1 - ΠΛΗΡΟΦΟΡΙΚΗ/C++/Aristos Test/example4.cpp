#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

void example4()
{
    int sumDiairetes;

    for(int number = 2; number <= 20000; number++){

        sumDiairetes = 0;

        // find all diairetes
        for(int diairetis = 1; diairetis < number; diairetis++){

            // is diairetis
            if(number%diairetis == 0){
                sumDiairetes = sumDiairetes + diairetis;
            }

        }

        // if sum(diairetes) = i -> print it
        if(sumDiairetes == number){
            cout << "Perfect number:" << number << endl;
        }
    }


}
