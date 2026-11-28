#include <iostream>

using namespace std;

void rect(double w, double l, double &e, double &p){
    e = w * l;
    p = 2*(w + l);
}

void example8()
{
    double e, p;

    rect(5, 9, e, p);

    cout << "w=5, l=9:" << "embadon=" << e << ", perimeter=" << p << endl;

}


