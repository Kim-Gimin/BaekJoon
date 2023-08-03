#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	int n, m;
	std::cin >> n >> m;

	std::unordered_set<int> setA, setB;

	for (int i = 0; i < n; ++i) {
		int num;
		std::cin >> num;
		setA.insert(num);
	}

	for (int i = 0; i < m; ++i) {
		int num;
		std::cin >> num;
		setB.insert(num);
	}

	int counting = 0;
	for (const auto& num : setA) {
		if (setB.count(num) == 0) {
			++counting;
		}
	}
	for (const auto& num : setB) {
		if (setA.count(num) == 0) {
			++counting;
		}
	}
	std::cout << counting << "\n";
	return 0;
}