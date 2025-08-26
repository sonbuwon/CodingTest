#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int side_points = pow(2, n) + 1;
    
    int total_points = side_points * side_points;
    
    cout << total_points << endl;
    
    return 0;
}