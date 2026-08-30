#include <stdio.h>
void main() {
    int i,n,quantum;
    int at[10],bt[10], tat[10], wt[10],rem[10];
    int timer=0;
    int completed=0;
    int awt=0;
    int atat=0;
    int total_wt=0;
    int total_tat=0;
    printf("Enter total no. of process and quantum:");
    scanf("%d %d", &n, &quantum);
    for(i=0;i<n;i++){
        printf("Enter Arrival and burst time for process%d: ",i+1);
        scanf("%d %d",&at[i],&bt[i]);
        rem[i]=bt[i];
    }
    while(completed<n){
        int executed=0;
        for(i=0;i<n;i++){
            if(rem[i]>0 && at[i]<=timer){
                executed=1;
                if(rem[i]>quantum){
                    rem[i]=rem[i]-quantum;
                    timer=timer+quantum;
                }
                else{
                    timer=timer+rem[i];
                    rem[i]=0;
                    completed++;
                    tat[i]=timer-at[i];
                    wt[i]=tat[i]-bt[i];
                    total_wt=total_wt+wt[i];
                    total_tat=total_tat+tat[i];
                }
            }
        }
        if(executed==0){
            timer++;
        }
    }
    printf("%d",total_tat);
    printf("\n");
    printf("%d",total_wt);
}