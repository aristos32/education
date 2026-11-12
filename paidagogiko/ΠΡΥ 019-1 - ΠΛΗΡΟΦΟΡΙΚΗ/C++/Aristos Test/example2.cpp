#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    int x1, y1, x2, y2;
    float distance;

    cout << "Enter x1, y1:" << endl;
    cin >> x1 >> y1;

    cout << "Enter x2, y2:" << endl;
    cin >> x2 >> y2;

    distance = sqrt(std::pow(x2-x1, 2) + std::pow(y2-y1, 2));

    cout << "distance is:" << fixed << setprecision(2) << distance;
    return 0;
}
