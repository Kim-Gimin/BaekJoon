#include <iostream>
#include <set>
#include <string>

int main() {
	int N, M;
	std::cin >> N >> M;

	std::set<std::string> S;
	for (int i = 0; i < N; ++i) {
		std::string str;
		std::cin >> str;
		S.insert(str);
	}
	int count = 0;
	for (int i = 0; i < M; ++i) {
		std::string str;
		std::cin >> str;
		if (S.find(str) != S.end()) {
			count++;
		}
	}
	std::cout << count << std::endl;

	return 0;
}