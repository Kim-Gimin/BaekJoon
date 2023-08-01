#include <iostream>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    int count = 0;
    int num = 666;

    while (true){
        if(to_string(num).find("666") != string::npos) {
            count++;
        }
        if (count == N) {
            break;
        }
        num++;
    }
    cout << num << endl;

    return 0;
}

