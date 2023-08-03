#include <iostream>

int gcd(int a, int b);
int lcm(int a, int b);

int main() {
	int T;
	std::cin >> T;

	while (T--) {
		int A, B;
		std::cin >> A >> B;
		std::cout << lcm(A, B) << "\n";
	}

	return 0;
}

int gcd(int a, int b) {
	while (b != 0) {
		int temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

int lcm(int a, int b) {
	return a * b / gcd(a, b);
}
