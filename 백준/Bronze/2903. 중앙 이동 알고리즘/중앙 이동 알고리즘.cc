#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int N;
    cin >> N;
    
    int temp = pow(2, N) + 1;
    
    cout << temp * temp << endl;
    
    return 0;
}