#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

int main() {
	int N;
	std::cin >> N;

	std::vector<int> X(N);
	for (int i = 0; i < N; ++i) {
		std::cin >> X[i];
	}

	std::vector<int> sortedx = X;
	std::sort(sortedx.begin(), sortedx.end());
	sortedx.erase(std::unique(sortedx.begin(), sortedx.end()), sortedx.end());

	std::map<int, int> index_map;
	for (int i = 0; i < sortedx.size(); ++i) {
		index_map[sortedx[i]] = i;
	}

	for (int i = 0; i < N; ++i) {
		std::cout << index_map[X[i]] << " ";
	}
	return 0;
}