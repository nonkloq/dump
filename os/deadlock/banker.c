#include<stdio.h>

#define N 5 // resource
#define M 3 // process

int main() {
    int available[M] = {3, 3, 2};
    int max[N][M] = {
        {7, 5, 3}, 
        {3, 2, 2}, 
        {9, 0, 2}, 
        {2, 2, 2}, 
        {4, 3, 3}
        };
    int allocation[N][M] = {
        {0, 1, 0}, 
        {2, 0, 0}, 
        {3, 0, 2}, 
        {2, 1, 1}, 
        {0, 0, 2}
        };
        
    int need[N][M]; // need matrix
    int safeSeq[N]; // safe sequence
    int work[M]; // work list 
    int i, j, k;

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    for (i = 0; i < M; i++) {
        work[i] = available[i];
    }

    int finish[N] = {0};

    int count = 0;
    while (count < N) {
        int found = 0;
        for (i = 0; i < N; i++) {
            if (finish[i] == 0) {
                int safe = 1;
                for (j = 0; j < M; j++) {
                    if (need[i][j] > work[j]) {
                        safe = 0;
                        break;
                    }
                }
                if (safe) {
                    for (j = 0; j < M; j++) {
                        work[j] += allocation[i][j];
                    }
                    safeSeq[count] = i;
                    finish[i] = 1;
                    count++;
                    found = 1;
                }
            }
        }
        if (!found) {
            printf("Deadlock detected.\n");
            return -1;
        }
    }

    printf("Safe sequence is: ");
    for (i = 0; i < N; i++) {
        printf("%d ", safeSeq[i]);
    }
    printf("\n");

    return 0;
}
