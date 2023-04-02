#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct {
    int pid;      // process ID
    int arrival;  // arrival time
    int burst;    // burst time
} pcb_t;

void fcfs(pcb_t *rQueue, int n) {
    int time = 0;
    double avg_wait_time = 0.0;
    
    for (int i = 0; i < n; i++) {
        int wait_time = time - rQueue[i].arrival;
        if (wait_time < 0) {
            wait_time = 0;
        }
        avg_wait_time += wait_time;
        
        time += rQueue[i].burst; // simulate the execution in n ms
        
        printf("Process %d; arrived at %dms; burst time %dms; completed at time %dms\n", rQueue[i].pid,rQueue[i].arrival,rQueue[i].burst, time);
    }
    
    avg_wait_time /= n;
    printf("Average waiting time: %.2f\n", avg_wait_time);
}



int process_adder(pcb_t **rQueue){
    int n;
    clock_t start_time = clock(), end_time;
    
    printf("N P0 ... PN (burst): ");
    scanf("%d", &n);

    *rQueue = (pcb_t*) malloc(sizeof(pcb_t) * n);
    int check;
    for (int i = 0; i < n; i++) {
        scanf("%d", &(*rQueue)[i].burst);
        end_time = clock();

        if (i==0) check = end_time-start_time;
        (*rQueue)[i].arrival = (end_time-start_time) - check;
        (*rQueue)[i].pid = i + 1;
    }
    return n;
}



int main() {
    // pcb_t *rQueue;
    // int n = process_adder(&rQueue);
    
    pcb_t rQueue[] = {
        {1,0,8},
        {2,1,4},
        {3,2,9},
        {4,3,5}
    };
    int n = 4;

    printf("\n\nFCFS Scheduling: \n");
    fcfs(rQueue, n);

    // free(rQueue);
    
    return 0;
}
