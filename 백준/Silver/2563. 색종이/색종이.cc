#include <iostream>

using namespace std;

int main()
{
    int paper[100][100] = {0};
    
    int n;
    cin >> n;
    
    for(int i=0; i<n; i++) {
        int x, y;
        cin>> x >> y;
        for(int row=y; row<y+10; row++) {
            for(int col=x; col<x+10; col++) {
                paper[row][col] = 1;
            }
        }
    }

    int count = 0;
    for(int i=0; i<100; i++) {
        for(int j=0; j<100; j++) {
            if (paper[i][j] == 1)  {
                count++;
            }
        }
    }
    
    cout << count << endl;
    
    return 0;
}