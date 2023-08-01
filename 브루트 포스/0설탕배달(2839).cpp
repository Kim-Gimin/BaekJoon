#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    int count_5kg = N / 5;  
    int remain = N % 5;     

   
    if (remain % 3 == 0) {
        cout << count_5kg + remain / 3 << endl;
    } else {
        while (count_5kg > 0) {
            count_5kg--;
            remain += 5;
            if (remain % 3 == 0) {
                cout << count_5kg + remain / 3 << endl;
                return 0;
            }
        }
        cout << -1 << endl;
    }

    return 0;
}
