total_waiting_time=0
total_turnaround_time=0
n= int(input("Enter number of processes :"))
arrival_time=[0]*n
burst_time=[0]*n
turn_around_time=[0]*n
quantum_time=[0]*n
i=0
p=[0]*n
while i<n:
      p[i]=i
      i+=1
for i in range(n):
    burst_time[i]=int(input("Enter burst time :"))
    arrival_time[i]=int(input("Enter arrival time:"))
quantum_time=int(input("Enter the quantum time:"))
print('Process No      Waiting Time    Turn Around Time')

          
for i in range(n):
    totalwaitingtime=totalwaitingtime+waitingtime[i];
    totalturnarroundtime=totalturnarroundtime+turnarroundtime[i];
print("Average Waiting Time" ,totalwaitingtime/n)
print("Average Turn Arround Time", totalturnarroundtime/n)

