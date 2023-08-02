#include <cstdio>
#include <algorithm>



int main() {
	int N;
	scanf("%d", &N);

	const int MAX = 10000;
	int count[MAX + 1] = { 0 };
	for(int i = 0; i < N; ++i) {
		int num;
		scanf("%d", &num);
		++count[num];
	}
	for (int i = 1; i <= MAX; ++i) {
		for (int j = 0; j < count[i]; ++j) {
			printf("%d\n", i);
		}
	}
	return 0;
}