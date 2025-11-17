# Scheduling Algorithms: Priority and Round Robin

def priority_scheduling(processes):
    # Sort by priority (lower number = higher priority)
    processes.sort(key=lambda x: x[2])

    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    for i in range(len(processes)):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    avg_wait = sum(waiting_time) / len(processes)
    avg_tat = sum(turnaround_time) / len(processes)

    print("\nPriority Scheduling Results:")
    print("PID\tBurst\tPriority\tWaiting\tTurnaround")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def round_robin(processes, quantum):
    n = len(processes)
    remaining = [p[1] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    t = 0

    while True:
        done = True
        for i in range(n):
            if remaining[i] > 0:
                done = False
                if remaining[i] > quantum:
                    t += quantum
                    remaining[i] -= quantum
                else:
                    t += remaining[i]
                    waiting_time[i] = t - processes[i][1]
                    remaining[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    avg_wait = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\nRound Robin Scheduling Results:")
    print("PID\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{waiting_time[i]}\t{turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def main():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        pid = int(input(f"Enter process ID for process {i+1}: "))
        burst = int(input(f"Enter burst time for process {i+1}: "))
        priority = int(input(f"Enter priority for process {i+1}: "))
        processes.append([pid, burst, priority])

    priority_scheduling(processes)

    quantum = int(input("\nEnter time quantum for Round Robin: "))
    round_robin(processes, quantum)


if __name__ == "__main__":
    main()
