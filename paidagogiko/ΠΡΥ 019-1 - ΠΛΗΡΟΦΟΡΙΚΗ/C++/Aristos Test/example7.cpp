#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void example7()
{
    string lineFile1, lineFile2;
    ifstream file1("file1.txt");
    ifstream file2("file2.txt");

    bool filesAreEqual = true;

    // read from file and print to console
    while(!file1.eof() && !file2.eof()){
        getline(file1, lineFile1);
        getline(file2, lineFile2);

        //compare lines from both files
        if(lineFile1==lineFile2){
            cout << "lines are equal" << endl;
            continue;
        }
        else{
            cout << "lines are not equal" << endl;
            filesAreEqual = false;
            break;
        }
    }


    // check if one file has more lines than the other
    if(!file1.eof() || !file2.eof()){
        cout << "One file has more lines" << endl;
        filesAreEqual = false;
    }

    if(filesAreEqual){
        cout << "files are equal" << endl;
    }
    else{
        cout << "files are not equal" << endl;
    }



}


