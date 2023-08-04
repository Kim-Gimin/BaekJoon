#include <iostream>
#include <vector>


int gcd(int a, int b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}
int lcm(int a, int b) {
	return (a * b) / gcd(a, b);
}
void simple(int& a, int& b) {
	int d = gcd(a, b);
	a /= d;
	b /= d;
}
void add(int a1, int b1, int a2, int b2, int& resulta, int& resultb) {
	int c = b1 * b2;
	int sum = a1 * b2 + a2 * b1;

	resulta = sum;
	resultb = c;

}

int main() {
	std::vector<int> son(2);
	std::vector<int> mother(2);
	for (int i = 0; i < 2; ++i) {
		std::cin >> son[i] >> mother[i];
	}

	int resultson, resultmother;
	add(son[0], mother[0], son[1], mother[1], resultson, resultmother);
	simple(resultson, resultmother);

	std::cout << resultson << " " << resultmother << "\n";

	return 0;
}
