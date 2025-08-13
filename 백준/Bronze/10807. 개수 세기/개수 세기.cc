#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    
    int numbers[N];
    
    for(int i=0; i<N; i++) {
        cin >> numbers[i];
    }
    
    int v;
    cin >> v;
    
    int count = 0;
    
    for(int i=0; i<N; i++) {
        if (v == numbers[i]) {
            count++;
        }
    }
    
    cout << count << endl;

    return 0;
}