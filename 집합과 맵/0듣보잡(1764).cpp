#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	int N, M;
	std::cin >> N >> M;

	std::unordered_set<std::string> Hear;
	std::unordered_set<std::string> See;
	std::vector<std::string> answer;

	for (int i = 0; i < N; ++i) {
		std::string name;
		std::cin >> name;
		Hear.insert(name);
	}

	for (int i = 0; i < M; ++i) {
		std::string name;
		std::cin >> name;
		See.insert(name);
	}

	for (const auto& name : See) {
		if (Hear.count(name) > 0) {
			answer.push_back(name);
		}
	}

	std::cout << answer.size() << '\n';

	std::sort(answer.begin(), answer.end());
	for (const auto& name : answer) {
		std::cout << name << '\n';
	}

	return 0;
}