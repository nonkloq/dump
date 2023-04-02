#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>

int main(){
    key_t pvt = ftok("shared_mem_key", 'A');
    int shmid = shmget(pvt, sizeof(int), 0666|IPC_CREAT);

    int *shared_memory = (int *)shmat(shmid, NULL, 0);
    printf("Shared Memory: ID[%d] Location[%p]\n",shmid,shared_memory);



    printf("Read from PA: %d\n",*shared_memory);
    printf("Enter Number: ");
    scanf("%d",shared_memory);
    printf("Write from PA: %d\n",*shared_memory);
    
    if (*shared_memory ==-69){ // destroy SHM
        printf("\nDestroying Shared Memory...\n");
        shmctl(shmid,IPC_RMID,NULL); 
        return 0;
    }
    shmdt(shared_memory);

    return 0;
}
