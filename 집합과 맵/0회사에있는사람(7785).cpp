#include <iostream>
#include <set>
#include <string>

int main() {
    int n;
    std::cin >> n;

    std::set<std::string> employee;
    for (int i = 0; i < n; ++i) {
        std::string name, status;
        std::cin >> name >> status;

        if (status == "enter") { 
            employee.insert(name);
        }
        else if (status == "leave") { 
            employee.erase(name);
        }
    }

    for (auto it = employee.rbegin(); it != employee.rend(); ++it) {
        std::cout << *it << "\n";
    }

    return 0;
}
