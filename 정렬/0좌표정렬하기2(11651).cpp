#include <iostream>
#include <algorithm>
#include <vector>

struct Point {
	int x, y;
};

bool compare(Point a, Point b) {
    if (a.y == b.y)
        return a.x < b.x;
    return a.y < b.y;
}

int main() {
    int N;
    std::cin >> N;

    std::vector<Point> points(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> points[i].x >> points[i].y;
    }

    std::sort(points.begin(), points.end(), compare);
    for (int i = 0; i < N; ++i) {
        std::cout << points[i].x << " " << points[i].y << "\n";
    }
    return 0;
}
