#include <iostream>

using namespace std;

int getSumDigit(int num){
    int sum = 0;
    while (num > 0){

        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int main(){
    int N;
    cin >> N;
    int answer = 0;
    for (int i = 1; i < N; ++i){
        if( i + getSumDigit(i) == N){
            answer = i;
            break;
    }
    }

    cout << answer << endl;

    return 0;
}