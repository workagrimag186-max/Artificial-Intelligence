#include <stdio.h>
void main() {
    int i,n;
    int at[10],bt[10],priority[10], tat[10], wt[10],rem[10];
    int timer=0;
    int completed=0;
    int awt=0;
    int atat=0;
    int total_wt=0;
    int total_tat=0;
    printf("Enter total no. of process:");
    scanf("%d", &n);
    for(i=0;i<n;i++){
        printf("Enter Arrival and burst time for process%d: ",i+1);
        scanf("%d %d %d",&at[i],&bt[i], &priority[i]);
        rem[i]=bt[i];
    }
    while(completed<n){
        int highest=-1;
        int min=9999;
        for(i=0;i<n;i++){
            if(rem[i]>0 && priority[i]<min && at[i]<=timer){
                min=priority[i];
                highest=i;
            }
        }
        if(highest==-1){
            timer++;
            continue;
        }
        rem[highest]--;
        timer++;
        if(rem[highest]==0){
            completed++;
            tat[highest]=timer-at[highest];
            wt[highest]=tat[highest]-bt[highest];
            total_wt=total_wt+wt[highest];
            total_tat=total_tat+tat[highest];
        }
    }
    printf("%d",total_tat);
    printf("\n");
    printf("%d",total_wt);
}