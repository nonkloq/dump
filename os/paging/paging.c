#include <stdio.h>
#include <stdlib.h>

#define PAGE_SIZE 1000
#define NUM_PAGES 8
#define MEM_SIZE (PAGE_SIZE * NUM_PAGES)

int main() {
    char *memory = malloc(MEM_SIZE);
    if (memory == NULL) {
        printf("Error: Failed to allocate memory!\n");
        return 1;
    }

    int *page_table = malloc(NUM_PAGES * sizeof(int));
    if (page_table == NULL) {
        printf("Error: Failed to allocate page table!\n");
        free(memory);
        return 1;
    }
    for (int i = 0; i < NUM_PAGES; i++) page_table[i] = -1;

    for (int i = 0; i < NUM_PAGES; i++) {
        int page_number = rand() % NUM_PAGES; // simulate random access pattern
        if (page_table[page_number] == -1) {
            printf("Loading page %d...\n", page_number);
            for (int j = 0; j < PAGE_SIZE; j++) {
                memory[page_number * PAGE_SIZE + j] = rand() % 256; // initialize page data
            }
            page_table[page_number] = i; 
        }
        else {
            printf("Using page %d...\n", page_number);
        }
    }

    free(memory);
    free(page_table);

    return 0;
}
