#include <stdio.h>
#include <stdlib.h>

#define MAX_REQUESTS 100

int main() {
    int requests[MAX_REQUESTS];
    int num_requests = 0;
    int current_position = 0;
    int total_seek_time = 0;
    
    printf("Enter disk requests (end with -1):\n");
    while (1) {
        int request;
        scanf("%d", &request);
        
        if (request == -1) {
            break;
        }
        
        requests[num_requests] = request;
        num_requests++;
        if (num_requests == MAX_REQUESTS) {
            printf("Maximum number of requests reached.\n");
            break;
        }
    }
    
    printf("Starting at position %d.\n", current_position);
    for (int i = 0; i < num_requests; i++) {
        int min_distance = 1000;
        int min_index = -1;
        
        for (int j = 0; j < num_requests; j++) {
            if (requests[j] != -1) {
                int seek_distance = abs(requests[j] - current_position);
                if (seek_distance < min_distance) {
                    min_distance = seek_distance;
                    min_index = j;
                }
            }
        }
        
        total_seek_time += min_distance;
        current_position = requests[min_index];
        requests[min_index] = -1;
        
        printf("Moved to position %d, seek distance = %d.\n", current_position, min_distance);
    }
    
    printf("Total seek time: %d.\n", total_seek_time);
    
    return 0;
}
