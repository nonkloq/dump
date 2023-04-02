#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 1024
#define MAX_BLOCKS 1024
#define MAX_FILES 1024
#define FILENAME_SIZE 32
#define MAX_BLOCKS_PER_FILE (BLOCK_SIZE / sizeof(int))

typedef struct {
    char filename[FILENAME_SIZE];
    int size;
    int index_block;
} file_entry;

file_entry files[MAX_FILES];
int disk[MAX_BLOCKS];

int num_files = 0;
int num_blocks_used = 0;

int allocate_block() {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        if (disk[i] == -1) {
            disk[i] = 0; 
            num_blocks_used++;
            return i;
        }
    }
    return -1;
}

void free_blocks(int index_block) {
    for (int i = 0; i < MAX_BLOCKS_PER_FILE; i++) {
        int block_num = disk[index_block + i];
        if (block_num != -1) {
            disk[block_num] = -1;
            num_blocks_used--;
        }
    }
}

void create_file(char* filename, int size) {
    if (num_files >= MAX_FILES) {
        printf("Error: maximum number of files reached.\n");
        return;
    }
    int num_blocks_needed = size / BLOCK_SIZE + (size % BLOCK_SIZE == 0 ? 0 : 1);
    if (num_blocks_needed > MAX_BLOCKS_PER_FILE) {
        printf("Error: file size too large.\n");
        return;
    }
    int index_block = allocate_block();
    if (index_block == -1) {
        printf("Error: not enough free space on disk.\n");
        return;
    }
    for (int i = 0; i < num_blocks_needed; i++) {
        int block_num = allocate_block();
        if (block_num == -1) {
            printf("Error: not enough free space on disk.\n");
            free_blocks(index_block);
            return;
        }
        disk[index_block + i] = block_num;
    }
    file_entry new_file;
    strcpy(new_file.filename, filename);
    new_file.size = size;
    new_file.index_block = index_block;
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
    free_blocks(files[index].index_block);
    for (int i = index; i < num_files - 1; i++) {
        files[i] = files[i + 1];
    }
    num_files--;
    printf("File deleted successfully.\n");
}

void list_files() {
    printf("Filename\tSize\tIndex Block\n");
    for (int i = 0; i < num_files; i++) {
        printf("%s\t\t%d\t%d\n", files[i].filename, files[i].size, files[i].index_block);
    }
}

int main() {
    memset(disk, -1, sizeof(disk));
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