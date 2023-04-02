#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

typedef struct{
    int pid;      // process ID
    int arrival;  // arrival time
    int burst; // burst
    int remain_time;
} pcb_t;



void sjf(pcb_t *rQueue, int n){

    int completed =0;
    int curr_time=0;
    int total_waiting_time = 0;
    int prev_pid = -1;
    
    
    printf("Gantt Chart:\n");
    printf("-----------\n");
    printf("|");
    while (completed < n){
        // selecting the shortest job
        
        int min_pid = -1;
        int min_burst = INT_MAX;
        for(int i=0;i<n;i++){
            if (rQueue[i].arrival > curr_time) break;
            
            if (rQueue[i].remain_time < min_burst && rQueue[i].remain_time >0){
                min_burst = rQueue[i].remain_time;
                min_pid = i;
            }
        }
        if (min_pid == -1) {
            curr_time++;
            continue;
        }

        if(min_pid != prev_pid){
            printf(" %dms| P%d",curr_time,min_pid+1);
            prev_pid = min_pid;
        }

        
        rQueue[min_pid].remain_time--;
        curr_time++;
        if (rQueue[min_pid].remain_time == 0){
            total_waiting_time += curr_time - rQueue[min_pid].arrival - rQueue[min_pid].burst;
            completed++;
        }

        
    }
    printf(" %dms|\n",curr_time);

    printf("Average waiting time: %f\n",(float)total_waiting_time/n);
    
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

        (*rQueue)[i].arrival = (end_time-start_time)-check;
        
        (*rQueue)[i].remain_time = (*rQueue)[i].burst;
        (*rQueue)[i].pid = i+1;
                
    }
    return n;
}


int main() {
    // pcb_t *rQueue;
    // int n = process_adder(&rQueue);
    
    pcb_t rQueue[] = {
        {1,0,8,8},
        {2,1,4,4},
        {3,2,9,9},
        {4,3,5,5}
    };
    int n = 4;

    printf("PID\tArrival\tBurst\n");
    printf("---\t-------\t-----\n");
    for(int i=0;i<n;i++){
        printf("%d\t%d\t%d\n",rQueue[i].pid, rQueue[i].arrival, rQueue[i].burst);
    }
    
    printf("\n\nPreemptive SJF Scheduling: \n");
    sjf(rQueue, n);

    // free(rQueue);
    
    return 0;
}
