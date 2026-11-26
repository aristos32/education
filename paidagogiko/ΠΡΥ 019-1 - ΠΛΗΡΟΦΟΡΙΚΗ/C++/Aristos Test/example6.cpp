
#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>

using namespace std;

void example6()
{
    string code, encryptedString;

    cout << "Give code and encrypted string:" << endl;

    cin >> code >> encryptedString;

    int encryptedStringStartingIndex = 0;
    char codeLetter;
    string positions;
    bool codeFound = false, letterFound = false;

    // for each code letter
    for(int i=0; i<code.size(); i++){

        codeLetter = code[i];

        letterFound = false;
        // for each letter in encryptedString
        for(int j=encryptedStringStartingIndex; j<encryptedString.size(); j++){
            // if we have match, update string pointer to current index
            if(codeLetter==encryptedString[j]){
                letterFound = true;
                positions += to_string(j) + " ";
                encryptedStringStartingIndex = j + 1;
                break;
            }

        }

        // continue to next letter
        if(letterFound==true){
            codeFound = true;
            continue;
        }
        // one letter not found -> fail
        else{
            codeFound = false;
            break;
        }


    }

    if(codeFound){
        // print code positions in encrypted string
        cout << "code found, positions " << positions << endl;
    }
    else{
        // print -1
        cout << "not found " << "-1" << endl;
    }




}

