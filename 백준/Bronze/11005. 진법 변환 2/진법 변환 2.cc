#include <iostream>
#include <string>

int main()
{
    int N;
    int B;
    std::cin >> N;
    std::cin >> B;
    
    int quot = N;
    int rema = 0;
    
    std::string result;
    
    while(quot >= 1) {
        rema = quot % B;
        quot = quot / B;
        
        char c;
        if (rema >= 0 && rema <= 9) {
            c = '0' + rema;
        }
        else if (rema >= 10 && rema <= 35) {
            c = 'A' + rema - 10;
        }
        result += c;
    }
    
    for(int i=result.length() - 1;i>=0;i--) {
        std::cout << result[i];
    }

    return 0;
}