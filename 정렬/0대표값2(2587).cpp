#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> numbers(5);
    for (int i = 0; i < 5; ++i) {
        cin >> numbers[i];
    }

    sort(numbers.begin(), numbers.end());

    int sum = 0;
    for (int i = 0; i < 5; ++i) {
        sum += numbers[i];
    }

    int average = sum / 5;
    int median;
    if (numbers.size() % 2 == 1) {
        median = numbers[2];
    }
    else {
        median = (numbers[2] + numbers[3]) / 2;
    }

    cout << average << endl;
    cout << median << endl;

    return 0;
}
