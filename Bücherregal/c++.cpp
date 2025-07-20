#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    std::string filename;
    std::cout << "Dateiname: ";
    std::getline(std::cin, filename);

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Fehler beim Öffnen der Datei!" << std::endl;
        return 1;
    }

    int figures, books;
    file >> figures >> books;

    std::vector<int> shelf(books);
    for (int i = 0; i < books; ++i) {
        file >> shelf[i];
    }

    file.close();

    std::sort(shelf.begin(), shelf.end());
    int curmin = shelf[0];

    for (int book : shelf) {
        if (book - curmin > 30) {
            curmin = book;
            figures--;
        }
    }

    if (figures < 0) {
        std::cout << "Geht nicht" << std::endl;
    } else {
        std::cout << "Geht" << std::endl;
    }

    return 0;
}