#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define PAGE_SIZE 1000
#define NUM_PAGES 8
#define MEM_SIZE (PAGE_SIZE * NUM_PAGES)

int find_lru_page(int *page_table, int *last_used, int num_pages) {
    int lru_page = 0;
    int lru_time = last_used[0];
    for (int i = 1; i < num_pages; i++) {
        if (last_used[i] < lru_time && page_table[i] != -1) {
            lru_page = i;
            lru_time = last_used[i];
        }
    }
    return lru_page;
}

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
    int *last_used = malloc(NUM_PAGES * sizeof(int));
    if (last_used == NULL) {
        printf("Error: Failed to allocate last used array!\n");
        free(memory);
        free(page_table);
        return 1;
    }
    for (int i = 0; i < NUM_PAGES; i++) {
        page_table[i] = -1; 
        last_used[i] = -1; 
    }

    int num_page_faults = 0;
    for (int i = 0; i < 1000; i++) {
        int page_number = rand() % NUM_PAGES;
        if (page_table[page_number] == -1) {
            int lru_page = find_lru_page(page_table, last_used, NUM_PAGES);
            if (lru_page != -1) {
                printf("Evicting page %d and loading page %d...\n", lru_page, page_number);
                for (int j = 0; j < PAGE_SIZE; j++) {
                    memory[lru_page * PAGE_SIZE + j] = 0; 
                }
                for (int j = 0; j < PAGE_SIZE; j++) {
                    memory[page_number * PAGE_SIZE + j] = rand() % 256; 
                }
                page_table[lru_page] = -1; // mark evicted page as not loaded
                page_table[page_number] = i; // mark new page as loaded
                last_used[page_number] = i; // update last used time for new page
                num_page_faults++;
            }
        }
        else last_used[page_number] = i; // Page is already loaded, so update last used time
    }

    printf("Number of page faults: %d\n", num_page_faults);

    free(memory);
    free(page_table);
    free(last_used);

    return 0;
}
