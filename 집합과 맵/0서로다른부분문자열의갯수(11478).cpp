#include <set>
#include <iostream>
#include <string>

int main() {
	std::string S;
	std::cin >> S;

	int N = S.length();
	std::set<std::string> subString;

	for (int len = 1; len <= N; ++len) {
		for (int i = 0; i <= N - len; ++i) {
			std::string sub = S.substr(i, len);
			subString.insert(sub);
		}
	}
	int count = subString.size();

	std::cout << count << "\n";

	return 0;
	
}