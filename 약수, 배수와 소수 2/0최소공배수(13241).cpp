#include <iostream>

long long int gcd(long long int a, long long int b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

long long int lcm(long long int a, long long int b) {
	return (a * b) / gcd(a, b);
}

int main() {
	long long int A, B;
	std::cin >> A >> B;

	long long int result = lcm(A, B);
	std::cout << result << "\n";

	return 0;
}