#include <iostream>
using namespace std;
int main()
{
    int array2d[9][9];
    int max = -1;
    int max_x = 1, max_y = 1;
    
    for(int i=0; i<9; i++) {
        for(int j=0; j<9; j++) {
            cin >> array2d[i][j];
            if (array2d[i][j] > max) {
                max = array2d[i][j];
                max_x = i+1;
                max_y = j+1;
            }
        }
    }
    
    cout << max << endl;
    cout << max_x << " " << max_y << endl;
    return 0;
}