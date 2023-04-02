#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 1024
#define MAX_BLOCKS 1024
#define MAX_FILES 1024
#define FILENAME_SIZE 32

typedef struct block {
    int index;
    struct block* next;
} block;

typedef struct {
    char filename[FILENAME_SIZE];
    int size;
    block* first_block;
} file_entry;

file_entry files[MAX_FILES];
char disk[MAX_BLOCKS][BLOCK_SIZE];

int num_files = 0;
int num_blocks_used = 0;

block* allocate_block() {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        if (strcmp(disk[i], "") == 0) {
            disk[i][0] = 'a' + (char)i; // for debug purposes only
            num_blocks_used++;
            block* new_block = malloc(sizeof(block));
            new_block->index = i;
            new_block->next = NULL;
            return new_block;
        }
    }
    return NULL;
}

void free_blocks(block* first_block) {
    block* current_block = first_block;
    while (current_block != NULL) {
        int index = current_block->index;
        strcpy(disk[index], "");
        num_blocks_used--;
        block* next_block = current_block->next;
        free(current_block);
        current_block = next_block;
    }
}

void create_file(char* filename, int size) {
    if (num_files >= MAX_FILES) {
        printf("Error: maximum number of files reached.\n");
        return;
    }
    int num_blocks_needed = size / BLOCK_SIZE + (size % BLOCK_SIZE == 0 ? 0 : 1);
    block* current_block = NULL;
    block* previous_block = NULL;
    for (int i = 0; i < num_blocks_needed; i++) {
        current_block = allocate_block();
        if (current_block == NULL) {
            printf("Error: not enough free space on disk.\n");
            free_blocks(previous_block);
            return;
        }
        if (previous_block == NULL) {
            files[num_files].first_block = current_block;
        } else {
            previous_block->next = current_block;
        }
        previous_block = current_block;
    }
    file_entry new_file;
    strcpy(new_file.filename, filename);
    new_file.size = size;
    new_file.first_block = files[num_files].first_block;
    files[num_files] = new_file;
    num_files++;
    printf("File created successfully.\n");
}

void delete_file(char* filename) {
    int index = -1;
    for (int i = 0; i < num_files; i++) {
        if (strcmp(files[i].filename, filename) == 0) {
            index = i;
            break;
        }
    }
    if (index == -1) {
        printf("Error: file not found.\n");
        return;
    }
    free_blocks(files[index].first_block);
    for (int i = index; i < num_files - 1; i++) {
        files[i] = files[i + 1];
    }
    num_files--;
    printf("File deleted successfully.\n");
}

void list_files() {
    printf("Filename\tSize\tFirst Block\n");
    for (int i = 0; i < num_files;i++) printf("%s\t\t%d\t%p\n", files[i].filename, files[i].size, files[i].first_block);
}

int main() {
    char command[16];
    char filename[FILENAME_SIZE];
    int size;
            
    while (1) {
        printf("Enter command (create <filename> <size>, delete <filename>, list, exit): ");
        scanf("%s", command);
        if (strcmp(command, "create") == 0) {
            scanf("%s %d", filename, &size);
            create_file(filename, size);
        } else if (strcmp(command, "delete") == 0) {
            scanf("%s", filename);
            delete_file(filename);
        } else if (strcmp(command, "list") == 0) {
            list_files();
        } 
        else if (strcmp(command, "exit") == 0) break;
        else printf("Invalid command.\n");
    }
    return 0;
}
