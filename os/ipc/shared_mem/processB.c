#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>

int main() {
    key_t pvt = ftok("shared_mem_key", 'A'); // private key
    int shmid = shmget(pvt, sizeof(int), 0666); // it only gets not create

    if (shmid == -1) { perror("shmget");return 1;}
    
    int *shared_memory = (int *)shmat(shmid, NULL, 0);
    printf("Shared Memory: ID[%d] Location[%p]\n",shmid,shared_memory);


    
    printf("Read from PB: %d\n",*shared_memory);
    *shared_memory = *shared_memory*2;
    printf("Write from PB: %d\n",*shared_memory);
    
    shmdt(shared_memory);

    return 0;
}
