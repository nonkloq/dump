/* Resource Allocation Graph Implementation*/

#include <stdio.h>
#include <stdbool.h>

#define MAX_RESOURCES 10
#define MAX_PROCESSES 10

typedef struct {
    int available;
    int allocated[MAX_PROCESSES];
    int request[MAX_PROCESSES];
} Resource;

typedef struct {
    int id;
    int requested[MAX_RESOURCES];
    bool finished;
} Process;

void create(Resource* resource, int numResources) {
    int i;
    for (i = 0; i < numResources; i++) {
        printf("Enter the amount of resource %d: ", i+1);
        scanf("%d", &resource->allocated[i]);
        resource->available -= resource->allocated[i];
    }
}

void release(Resource* resource, int numResources) {
    int i;
    for (i = 0; i < numResources; i++) {
        printf("Enter the amount of resource %d: ", i+1);
        scanf("%d", &resource->allocated[i]);
        resource->available += resource->allocated[i];
    }
}

bool check_deadlock(Process processes[], int numProcesses, Resource resources[], int numResources) {
    bool finished[numProcesses];
    int i, j, k;
    for (i = 0; i < numProcesses; i++) {
        finished[i] = processes[i].finished;
    }

    bool deadlock = true;
    while (deadlock) {
        deadlock = false;
        for (i = 0; i < numProcesses; i++) {
            if (!finished[i]) {
                bool can_allocate = true;
                for (j = 0; j < numResources; j++) {
                    if (processes[i].requested[j] > resources[j].available) {
                        can_allocate = false;
                        break;
                    }
                }
                if (can_allocate) {
                    finished[i] = true;
                    deadlock = false;
                    for (j = 0; j < numResources; j++) {
                        resources[j].available += processes[i].requested[j];
                    }
                }
            }
        }
    }

    for (i = 0; i < numProcesses; i++) {
        if (!finished[i]) {
            return true;
        }
    }
    return false;
}

int main() {
    Resource resources[MAX_RESOURCES];
    Process processes[MAX_PROCESSES];
    int numResources, numProcesses;
    int i, j;

    printf("Enter the number of resources: ");
    scanf("%d", &numResources);
    printf("Enter the number of processes: ");
    scanf("%d", &numProcesses);

    for (i = 0; i < numResources; i++) {
        printf("Enter the number of available instances of resource %d: ", i+1);
        scanf("%d", &resources[i].available);
    }

    for (i = 0; i < numProcesses; i++) {
        processes[i].id = i+1;
        processes[i].finished = false;
        printf("Enter the requested resources for process %d:\n", i+1);
        for (j = 0; j < numResources; j++) {
            scanf("%d", &processes[i].requested[j]);
        }
    }

    if (check_deadlock(processes, numProcesses, resources, numResources)) {
        printf("Dead lock detected. Terminating.\n");
        return 1;
    }
    for (i = 0; i < numProcesses; i++) {
        for (j = 0; j < numResources; j++) {
            resources[j].allocated[i] = processes[i].requested[j];
            resources[j].available -= processes[i].requested[j];
        }
    }

    printf("Resource Allocation Graph:\n");
    for (i = 0; i < numProcesses; i++) {
        printf("P%d -> ", i+1);
        for (j = 0; j < numResources; j++) {
            if (processes[i].requested[j] > 0) {
                printf("R%d (%d) ", j+1, processes[i].requested[j]);
            }
        }
        printf("\n");
    }

    for (i = 0; i < numResources; i++) {
        printf("R%d -> ", i+1);
        for (j = 0; j < numProcesses; j++) {
            if (resources[i].allocated[j] > 0) {
                printf("P%d (%d) ", j+1, resources[i].allocated[j]);
            }
        }
        printf("\n");
    }

    printf("Do you want to release any resources? (y/n): ");
    char answer;
    scanf(" %c", &answer);
    if (answer == 'y') {
        release(resources, numResources);
    }

    if (check_deadlock(processes, numProcesses, resources, numResources)) {
        printf("Deadlock detected. Terminating.\n");
        return 1;
    }

    printf("Do you want to allocate any resources? (y/n): ");
    scanf(" %c", &answer);
    if (answer == 'y') {
        create(resources, numResources);
    }

    if (check_deadlock(processes, numProcesses, resources, numResources)) {
        printf("Deadlock detected. Terminating.\n");
        return 1;
    }

    printf("Final Resource Allocation Graph:\n");
    for (i = 0; i < numProcesses; i++) {
        printf("P%d -> ", i+1);
        for (j = 0; j < numResources; j++) {
            if (processes[i].requested[j] > 0) {
                printf("R%d (%d) ", j+1, processes[i].requested[j]);
            }
        }
        printf("\n");
    }

    for (i = 0; i < numResources; i++) {
        printf("R%d -> ", i+1);
        for (j = 0; j < numProcesses; j++) {
            if (resources[i].allocated[j] > 0) {
                printf("P%d (%d) ", j+1, resources[i].allocated[j]);
            }
        }
        printf("\n");
    }

    return 0;
}