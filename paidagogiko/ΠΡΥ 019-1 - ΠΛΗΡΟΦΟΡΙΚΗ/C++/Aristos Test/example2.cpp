#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

void example2()
{
    int studentNumber, monades, dekades, ekatondades;

    cout << "Enter student number:" << endl;
    cin >> studentNumber;

    // integer division by 100 -> get ekatondades
    ekatondades = studentNumber / 100;

    studentNumber = studentNumber - ekatondades * 100;

    // integer division by 10 -> get dekades
    dekades = studentNumber / 10;

    cout << "Answer is:" << dekades;

    // studentNumber = studentNumber - dekades * 10

    // monades = studentNumber





}
