
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

    if (booksNumber > 500)
    {
        totalCost = (booksNumber - 500) * costPerBook[2];
        booksNumber = 500;
    }

    if (booksNumber > 100)
    {
        totalCost = totalCost + (booksNumber - 100) * costPerBook[1];
        booksNumber = 100;
    }

    if (booksNumber > 0)
    {
        totalCost = totalCost + booksNumber * costPerBook[0];
    }

    cout << "Total cost:" << totalCost << endl;

}
