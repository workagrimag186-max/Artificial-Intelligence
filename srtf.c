#include <stdio.h>
void main() {
    int i,n;
    int at[10],bt[10],rem[10], tat[10], wt[10];
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
        scanf("%d %d",&at[i],&bt[i]);
        rem[i]=bt[i];
    }
    while(completed>n){
        int shortest=-1;
        int min=9999;
        for(i=0;i<n;i++){
            if(rem[i]>0 && rem[i]<min && at[i]<timer){
                min=rem[i];
                shortest=i;
            }
        }
        if(shortest==-1){
            timer++;
            continue;
        }
        rem[shortest]--;
        timer++;
        if(rem[shortest]==0){
            completed++;
            tat[shortest]=timer-at[shortest];
            wt[shortest]=tat[shortest]-bt[shortest];
            total_wt=total_wt+wt[shortest];
            total_tat=total_tat+tat[shortest];
        }
    }

}