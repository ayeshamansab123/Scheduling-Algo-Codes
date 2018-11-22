total_waiting_time=0
total_turnaround_time=0
n= int(input("Enter number of processes :"))
waiting_time=[0]*n
turnaround_time=[0]*n
priority=[0]*n
burst_time=[0]*n
i=0
j=0
p=[0]*n
while i<n:
      p[i]=i
      i+=1
for i in range(n):
    burst_time[i]=int(input("Enter burst time :"))
    priority[i]=int(input("Enter priority:"))
for i in range(n):
    position=i; 
    j=i+1
    for j in range(n):
         if priority[j] < priority[position]:    
             position=j;
    temp=priority[i];
    priority[i]=priority[position];
    priority[position]=temp;
    temp=burst_time[i];
    burst_time[i]=burst_time[position];
    burst_time[position]=temp;
waiting_time[0]=0;
for i in range(n-1):
     j=1
     j+=i
     waiting_time[j]=waiting_time[i] + burst_time[i];
for i in range(n):
    turnaround_time[i]=waiting_time[i]+burst_time[i];  
print('Process No    Burst Time    Waiting Time    Turn Around Time')
for i in range(n):
     print("p[",i,"]","\t\t",(burst_time[i]),"\t\t",(waiting_time[i]),"\t\t",(turnaround_time[i]))
for i in range(n):
    total_waiting_time=total_waiting_time+waiting_time[i];
    total_turnaround_time=total_turnaround_time+turnaround_time[i];
print("Average Waiting Time" ,total_waiting_time/n)
print("Average Turn Arround Time", total_turnaround_time/n)