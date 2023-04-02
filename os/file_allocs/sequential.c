#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 1024
#define MAX_BLOCKS 1024
#define MAX_FILES 1024
#define FILENAME_SIZE 32

typedef struct {
    int start_block;
    int num_blocks;
} file_allocation;

typedef struct {
    char filename[FILENAME_SIZE];
    int size;
    file_allocation allocation;
} file_entry;

file_entry files[MAX_FILES];
char disk[MAX_BLOCKS][BLOCK_SIZE];

int num_files = 0;
int num_blocks_used = 0;


int allocate_blocks(int num_blocks) {
    int start_block = -1;
    int blocks_found = 0;
    for (int i = 0; i < MAX_BLOCKS; i++) {
        if (blocks_found == 0) {
            if (strcmp(disk[i], "") == 0) {
                start_block = i;
                blocks_found++;
            }
        } else {
            if (strcmp(disk[i], "") == 0) {
                blocks_found++;
            } else {
                blocks_found = 0;
                start_block = -1;
            }
        }
        if (blocks_found == num_blocks) {
            break;
        }
    }
    if (blocks_found == num_blocks) {
        for (int i = start_block; i < start_block + num_blocks; i++) {
            strcpy(disk[i], "allocated");
        }
        num_blocks_used += num_blocks;
        return start_block;
    } else {
        return -1;
    }
}

void create_file(char* filename, int size) {
    if (num_files >= MAX_FILES) {
        printf("Error: maximum number of files reached.\n");
        return;
    }
    int num_blocks_needed = size / BLOCK_SIZE + (size % BLOCK_SIZE == 0 ? 0 : 1);
    int start_block = allocate_blocks(num_blocks_needed);
    if (start_block == -1) {
        printf("Error: not enough free space on disk.\n");
        return;
    }
    file_entry new_file;
    strcpy(new_file.filename, filename);
    new_file.size = size;
    new_file.allocation.start_block = start_block;
    new_file.allocation.num_blocks = num_blocks_needed;
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
    for (int i = files[index].allocation.start_block; i < files[index].allocation.start_block + files[index].allocation.num_blocks; i++) {
        strcpy(disk[i], "");
    }
    num_blocks_used -= files[index].allocation.num_blocks;
    for (int i = index; i < num_files - 1; i++) {
        files[i] = files[i + 1];
    }
    num_files--;
    printf("File deleted successfully.\n");
}

/*MAIN*/
void list_files() {
    printf("Filename\tSize\tStart Block\tNum Blocks\n");
    for (int i = 0; i < num_files; i++){
        printf(
            "%s\t\t%d\t%d\t\t%d\n", 
            files[i].filename, 
            files[i].size, 
            files[i].allocation.start_block, 
            files[i].allocation.num_blocks
        );
    }
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