#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    string N;
    int B;
    cin >> N >> B;
    
    int result = 0;
    
    for(int i=0; i<N.length(); i++) {
        int digit;
        
        if(N[i] >= '0' && N[i] <= '9') {
            digit = N[i] - '0';
        }
        else if(N[i] >= 'A' && N[i] <= 'Z') {
            digit = N[i] - 'A' + 10;
        }
        
        result += digit * pow(B, N.length() - 1 - i);
    }
    cout << result << endl;
    
    return 0;
}