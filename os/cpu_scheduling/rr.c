#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct{
    int pid;      // process ID
    int arrival;  // arrival time
    int burst; // burst
    int remain_time;
} pcb_t;

void rr(pcb_t *rQueue, int n,int quantum){
    int completed = 0;
    int total_waiting_time = 0;
    int curr_time=0;
    int j=0;
    int curr_pid=0;    

    printf("Gantt Chart:\n");
    printf("-----------\n");
    printf("|0ms|");
    int tmp;
    while(completed < n){
        tmp = curr_pid;
        while(1){
            if (j<n && rQueue[j].arrival <= curr_time) j++; // the arrival should be in increasing order
            curr_pid = (curr_pid+1)%j;
            if (rQueue[curr_pid].remain_time != 0) break;
            if (tmp == curr_pid) curr_time++;
        }
        

        if (rQueue[curr_pid].remain_time <= quantum){
            curr_time += rQueue[curr_pid].remain_time; 
            rQueue[curr_pid].remain_time = 0;
            completed++;
            total_waiting_time += curr_time  - rQueue[curr_pid].arrival-rQueue[curr_pid].burst;
            
        } else {
            curr_time += quantum;
            rQueue[curr_pid].remain_time -= quantum;
        }
        printf(" P%d %dms |",curr_pid+1,curr_time);
        
    }
    printf("\n");

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
    pcb_t *rQueue;
    int n = process_adder(&rQueue);
    
    // pcb_t rQueue[] = {
    //     {1,0,24,24},
    //     {2,0,3,3},
    //     {3,0,3,3},
    // };
    // int n = 3;
    int quantum = 10; // 4;
    
    
    printf("PID\tArrival\tBurst\n");
    printf("---\t-------\t-----\n");
    for(int i=0;i<n;i++){
        printf("%d\t%d\t%d\n",rQueue[i].pid, rQueue[i].arrival, rQueue[i].burst);
    }
    
    printf("\n\nRR Scheduling: \n");
    rr(rQueue, n,quantum);

    free(rQueue);
    
    return 0;
}