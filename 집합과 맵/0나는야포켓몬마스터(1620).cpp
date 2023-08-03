#include <map>
#include <algorithm>
#include <string>
#include <cctype>
#include <iostream>

using namespace std;

string poketmon[100000];

int main() {
	map<string, int> P;
	int N, M;
	string name;
	int num;

	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> poketmon[i];
		P.insert(make_pair(poketmon[i], i));
	}

	for (int i = 0; i < M; i++) {
		cin >> name;

		if (isdigit(name[0]) != 0) {
			num = stoi(name) - 1;
			cout << poketmon[num] << "\n";
		}
		else {
			auto index = P.find(name);
			cout << index->second + 1 << "\n";
		}
	}
	return 0;
}