#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

bool compare(const std::string& a, const std::string& b) {
	if (a.length() == b.length())
		return a < b;
	return a.length() < b.length();
}

int main() {
	int N;
	std::cin >> N;

	std::vector<std::string> words(N);
	std::set<std::string> oneWord;

	for (int i = 0; i < N; ++i) {
		std::cin >> words[i];
		oneWord.insert(words[i]);
	}

	std::vector<std::string> sortWord(oneWord.begin(), oneWord.end());
	std::sort(sortWord.begin(), sortWord.end(), compare);

	for (const auto& word : sortWord) {
		std::cout << word << "\n";
	}
	return 0;
}