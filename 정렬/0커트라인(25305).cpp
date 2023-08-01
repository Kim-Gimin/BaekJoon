#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N, k;
	cin >> N >> k;
	vector<int> source(N);
	for (int i = 0; i < N; ++i) {
		cin >> source[i];
	}
	sort(source.begin(), source.end(), greater<int>());
	int cutline = source[k - 1];
	cout << cutline << endl;
	return 0;
}
