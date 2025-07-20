#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    char filename[100];
    printf("Dateiname: ");
    scanf("%s", filename);

    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Fehler beim Öffnen der Datei");
        return 1;
    }

    int figures, books;
    fscanf(file, "%d", &figures);
    fscanf(file, "%d", &books);

    int *shelf = malloc(books * sizeof(int));
    if (!shelf) {
        perror("Fehler bei Speicherreservierung");
        fclose(file);
        return 1;
    }

    for (int i = 0; i < books; ++i) {
        fscanf(file, "%d", &shelf[i]);
    }

    fclose(file);

    qsort(shelf, books, sizeof(int), compare_ints);

    int curmin = shelf[0];
    for (int i = 0; i < books; ++i) {
        if (shelf[i] - curmin > 30) {
            curmin = shelf[i];
            figures--;
        }
    }

    if (figures < 0) {
        printf("Geht nicht\n");
    } else {
        printf("Geht\n");
    }

    free(shelf);
    return 0;
}