/* Optimal Page Replacement Implementation*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define PAGE_SIZE 1000
#define NUM_PAGES 8
#define MEM_SIZE (PAGE_SIZE * NUM_PAGES)

int find_optimal_page(int *page_table, int *accesses, int num_pages, int current_time) {
    int optimal_page = -1;
    int max_future_access = -1;
    for (int i = 0; i < num_pages; i++) {
        if (page_table[i] != -1) {
            int future_access = -1;
            for (int j = current_time; j < 1000; j++) {
                if (accesses[j] == i) {
                    future_access = j;
                    break;
                }
            }
            if (future_access == -1) {
                return i; 
            }
            else if (future_access > max_future_access) {
                optimal_page = i;
                max_future_access = future_access;
            }
        }
        else return i; 
    }
    return optimal_page;
}

int main() {
    char *memory = malloc(MEM_SIZE);
    int *page_table = malloc(NUM_PAGES * sizeof(int));

    for (int i = 0; i < NUM_PAGES; i++) page_table[i] = -1;

    int num_page_faults = 0;
    int accesses[1000] = {0};
    for (int i = 0; i < 1000; i++) {
        int page_number = rand() % NUM_PAGES;
        accesses[i] = page_number;
        if (page_table[page_number] == -1) {
            int optimal_page = find_optimal_page(page_table, accesses, NUM_PAGES, i);
            if (optimal_page != -1) {
                printf("Evicting page %d and loading page %d...\n", optimal_page, page_number);
                for (int j = 0; j < PAGE_SIZE; j++) memory[optimal_page * PAGE_SIZE + j] = 0; // clear evicted page data
                
                for (int j = 0; j < PAGE_SIZE; j++) {
                    memory[page_number * PAGE_SIZE + j] = rand() % 420; // initialize new page data (random)
                }
                page_table[optimal_page] = -1; // mark evicted page as not loaded
                page_table[page_number] = i; // mark new page as loaded
                num_page_faults++;
            }
        }
    }

    printf("Number of page faults: %d\n", num_page_faults);

    free(memory);
    free(page_table);

    return 0;
}
