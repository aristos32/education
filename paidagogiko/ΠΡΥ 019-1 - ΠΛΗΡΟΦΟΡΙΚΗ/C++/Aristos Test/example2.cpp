#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

void example2()
{
    int studentNumber, monades, dekades, ekatondades, isArtios;

    cout << "Enter student number:" << endl;
    cin >> studentNumber;

    // integer division by 100 -> get ekatondades
    ekatondades = studentNumber / 100;

    studentNumber = studentNumber - ekatondades * 100;

    // integer division by 10 -> get dekades
    dekades = studentNumber / 10;

    studentNumber = studentNumber - dekades * 10;

    monades = studentNumber;

    isArtios = monades%2 == 0;

    cout << "The student is:" << endl;
    if(isArtios){
        cout << "Boy" << endl;
    }
    else{
        cout << "Girl" << endl;
    }

    if(dekades == 5){
        cout << "Ektopismenos" << endl;
    }
    else{
        cout << "Oxi ektopismenos" << endl;
    }

    if(ekatondades > 7){
        cout << "polyteknos" << endl;
    }
    else{
        cout << "oxi polyteknos" << endl;
    }

}
