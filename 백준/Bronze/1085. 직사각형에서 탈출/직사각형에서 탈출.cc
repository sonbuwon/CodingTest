#include <iostream>

using namespace std;

int main()
{
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    
    int wx = w-x;
    int hy = h-y;
    
    int min = wx;
    if (min > hy) min = hy;
    if (min > x) min = x;
    if (min > y) min = y;
    
    cout << min << endl;
    
    return 0;
}