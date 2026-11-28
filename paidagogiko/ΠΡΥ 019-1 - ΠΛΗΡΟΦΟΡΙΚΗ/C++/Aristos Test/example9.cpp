#include <iostream>
#define N 6
using namespace std;

void fill(int arr[]); // prototype
void print(int arr[]); // prototype

void shift_right(int a[], int n){
    int lastElement;

    // shift n times
    for(int i=0; i<n; i++){

        lastElement = a[N-1];

        // shift all elements to the right
        for(int j=N-1; j>0; j--){
            a[j] = a[j-1];
        }

        // set missing first element
        a[0] = lastElement;

    }

}

void example9()
{
    int A[N];
    int n;

    // insert elements
    fill(A);

    // read number of shift positions
    cout << "Enter the number of positions to shift: ";
    cin >> n;

    // shift elements
    shift_right(A, n);

    // display shifted table
    print(A);

}

void fill(int arr[]){
    cout << "Insert " << N << " elements: ";

    for(int i=0; i<N; i++){
        cin >> arr[i];
    }
}

void print(int arr[]){
    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}
