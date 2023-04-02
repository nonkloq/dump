#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

int memory[MAX_SIZE]; // array to represent the memory
int memory_size = MAX_SIZE;

int worst_fit(int size) {     // find the largest free block of memory
    int i, j, start, max_size = -1;
    

    for (i = 0; i < memory_size; i++) {
        if (memory[i] == 0) {
            int block_size = 1;
            for (j = i+1; j < memory_size && memory[j] == 0; j++) {
                block_size++;
            }
            if (block_size >= size && block_size > max_size) {
                max_size = block_size;
                start = i;
            }
        }
    }
    
    if (max_size != -1) {
        for (i = start; i < start+size; i++) {
            memory[i] = 1; // write
        }
        return start;
    }
    
    return -1;
}


int first_fit(int size) { // find the free block of requested size and return
    int i, j, start = -1;
    
    for (i = 0; i < memory_size; i++) {
        if (memory[i] == 0) {
            int block_size = 1;
            for (j = i+1; j < memory_size && memory[j] == 0; j++) {
                block_size++;
            }
            if (block_size >= size) {
                start = i;
                break;
            }
        }
    }
    
    if (start != -1) {
        for (i = start; i < start+size; i++) {
            memory[i] = 1;
        }
        return start;
    }
 
    return -1;
}


int best_fit(int size) { // find the smallest free block that accommadate the request size
    int i, j, start = -1, min_size = memory_size;
    
    for (i = 0; i < memory_size; i++) {
        if (memory[i] == 0) {
            int block_size = 1;
            for (j = i+1; j < memory_size && memory[j] == 0; j++) {
                block_size++;
            }
            if (block_size >= size && block_size < min_size) {
                min_size = block_size;
                start = i;
            }
        }
    }
    
    if (start != -1) {
        for (i = start; i < start+size; i++) {
            memory[i] = 1;
        }
        return start;
    }
    
    return -1;
}


void free_mem(int start, int size) {
    for (int i = start; i < start+size; i++) memory[i] = 0;
}

int main() {
    for (int i = 0; i < memory_size; i++) memory[i] = 0; // init
    
    int size;
    int to_free=0;
    
    while(1){
        printf("Enter size: ");
        scanf("%d",&size);
        int start = best_fit(size); // worst_fit(size); // first_fit(size);
        if (start != -1) printf("Memory allocated at position %d\n", start);
        else {
            printf("Memory allocation failed\nExiting...\n");
            break;
            }


        printf("Free it [1]: ");
        scanf("%d",&to_free);
        if (to_free == 1) free_mem(start,size);
    }

    
    return 0;
}
