#include <iostream>
#include <vector>
#include <algorithm>

struct id {
	int x;
	std::string y;
	int index;
};

bool compare(const id& a, const id& b) {
	if (a.x == b.x) {
		return a.index < b.index;
	}
	return a.x < b.x;
}

int main() {
	int N;
	std::cin >> N;
	std::vector<id> member(N);
	
	for (int i = 0; i < N; ++i) {
		std::cin >> member[i].x >> member[i].y;
		member[i].index = i;
	}

	std::sort(member.begin(), member.end(), compare);

	for (const auto& members : member) {
		std::cout << members.x << " " << members.y << "\n";
	}

	return 0;
}