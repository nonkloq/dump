#include <stdio.h>
#include <stdlib.h>

#define MAX_REQUESTS 100

int main() {
    int requests[MAX_REQUESTS];
    int num_requests = 0;
    int current_position = 0;
    int direction = 1; // 1 up; -1 down
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
    while (1) {
        int next_request = -1;
        int next_index = -1;
        
        for (int i = 0; i < num_requests; i++) {
            if (requests[i] != -1 && requests[i] >= current_position && direction == 1) {
                if (next_request == -1 || requests[i] < next_request) {
                    next_request = requests[i];
                    next_index = i;
                }
            }
            if (requests[i] != -1 && requests[i] <= current_position && direction == -1) {
                if (next_request == -1 || requests[i] > next_request) {
                    next_request = requests[i];
                    next_index = i;
                }
            }
        }
        
        if (next_request == -1) {
            if (direction == 1) {
                direction = -1;
                continue;
            } else if (direction == -1) {
                direction = 1;
                continue;
            }
        }
        
        int seek_distance = abs(current_position - next_request);
        total_seek_time += seek_distance;
        current_position = next_request;
        requests[next_index] = -1;
        
        printf("Moved to position %d, seek distance = %d.\n", current_position, seek_distance);
        
        if (num_requests == 1) {
            break;
        }
    }
    
    printf("Total seek time: %d.\n", total_seek_time);
    
    return 0;
}
