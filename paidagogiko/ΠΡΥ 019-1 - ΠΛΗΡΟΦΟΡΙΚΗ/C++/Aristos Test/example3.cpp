
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

void example3()
{
    int booksNumber;
    float totalCost = 0;
    float costPerBook[3] = {8, 6.4, 3.5};

    cout << "Enter books number:" << endl;
    cin >> booksNumber;

    if(booksNumber <= 100){
        totalCost = booksNumber * costPerBook[0];
    }
    else{
        booksNumber =
    }

    cout << "Total cost:" << totalCost;

}
