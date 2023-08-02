/*
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> List(N);
	for (int i = 0; i < N; ++i) {
		cin >> List[i];
	}
	sort(List.begin(), List.end());
	for (int j = 0; j < N; ++j) {
		cout << List[j] << endl;
	}
	return 0;
}
*/
#include <cstdio>
#include <vector>
#include <algorithm>


int main() {
	int N;
	scanf("%d", &N);
	std::vector<int> List(N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &List[i]);
	}
	std::sort(List.begin(), List.end());
	for (int j = 0; j < N; ++j) {
		print("%d\n", List[j]);
	}
	return 0;
}