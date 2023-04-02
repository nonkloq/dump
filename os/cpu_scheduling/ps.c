#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <math.h>

typedef struct{
    int pid;
    int arrival;
    int burst;
    int alive;
    int priority;
} pcb_t;


void ps(pcb_t* rQueue,int n){
    int completed = 0;
    int total_waiting_time = 0;
    int curr_time=0;
    printf("Gantt Chart:\n");
    printf("-----------\n");
    printf("|0ms|");

    while(completed < n){
        int pid = -1;
        int high_prior = INT_MAX;
        
        for(int i=0;i<n;i++){
            if (rQueue[i].arrival > curr_time) break;
            
            if (rQueue[i].priority < high_prior && rQueue[i].alive){
                high_prior = rQueue[i].priority;
                pid = i;
            }
        }
        if (pid == -1) {curr_time++; continue;}
        curr_time += rQueue[pid].burst;
        total_waiting_time += curr_time - rQueue[pid].arrival - rQueue[pid].burst;  
        rQueue[pid].alive = 0;
        completed++;

        int k = (int) ceil( rQueue[pid].burst / 2.0);
        for(int space=0;space<k;space++) printf(" "); 
        printf("P%d[%d]",pid+1,high_prior);
        for(int space=0;space<k;space++) printf(" ");
        printf("%dms|",curr_time);

    }
    printf("\n");

    printf("Average waiting time: %f\n",(float)total_waiting_time/n);


}



int process_adder(pcb_t **rQueue){
    int n;
    clock_t start_time = clock(), end_time;
    
    printf("N P0 Pr0 ... PN PrN(burst): ");
    scanf("%d", &n);

    *rQueue = (pcb_t*) malloc(sizeof(pcb_t) * n);
    int check;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &(*rQueue)[i].burst,&(*rQueue)[i].priority);
        end_time = clock();
        
        if (i==0) check = end_time-start_time;
        (*rQueue)[i].alive = 1;
        (*rQueue)[i].arrival = (end_time-start_time)-check;
        (*rQueue)[i].pid = i+1;
                
    }
    return n;
}


int main() {
    // pcb_t *rQueue;
    // int n = process_adder(&rQueue);
    
    pcb_t rQueue[] = {
        {1,0,10,1,3},
        {2,0,1,1,1},
        {3,0,2,1,4},
        {4,0,1,1,5},
        {5,0,5,1,2},
    };
    int n = 5;
    
    
    printf("PID\tArrival\tBurst\tPriority\n");
    printf("---\t-------\t-----\t--------\n");
    for(int i=0;i<n;i++){
        printf("%d\t%d\t%d\t%d\n",rQueue[i].pid, rQueue[i].arrival, rQueue[i].burst,rQueue[i].priority);
    }
    
    printf("\n\nPriority Scheduling: \n");
    ps(rQueue, n);

    // free(rQueue);
    
    return 0;
}