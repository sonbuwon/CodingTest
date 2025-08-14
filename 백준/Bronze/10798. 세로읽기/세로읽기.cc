#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char arr2d[5][16];
    
    for(int i=0; i<5; i++) {
        cin >> arr2d[i];
    }
    
    int maxLength = 0;
    for(int i=0; i<5; i++) {
        if(maxLength  < strlen(arr2d[i])) {
            maxLength = strlen(arr2d[i]);
        }
    }
    
    for(int i=0; i<maxLength; i++) {
        for(int j=0; j<5; j++) {
            if (i < strlen(arr2d[j])) {
                cout << arr2d[j][i];
            }
        }
    }
    
    return 0;
}