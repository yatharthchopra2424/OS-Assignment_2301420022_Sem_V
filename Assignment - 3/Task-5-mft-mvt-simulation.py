# mft_mvt_simulation.py

def mft(memory_size, partition_size, process_sizes):
    num_partitions = memory_size // partition_size
    print(f"\nTotal Memory: {memory_size} KB")
    print(f"Partition Size: {partition_size} KB")
    print(f"Number of Partitions: {num_partitions}\n")

    internal_frag = 0
    allocated = [False] * num_partitions

    print("MFT (Fixed Partition) Allocation:")
    for i, process in enumerate(process_sizes):
        allocated_flag = False
        for j in range(num_partitions):
            if not allocated[j] and process <= partition_size:
                allocated[j] = True
                internal_frag += (partition_size - process)
                print(f"Process {i+1} ({process} KB) -> Partition {j+1}")
                allocated_flag = True
                break
        if not allocated_flag:
            print(f"Process {i+1} ({process} KB) -> Not Allocated (No Free Partition)")

    print(f"\nTotal Internal Fragmentation: {internal_frag} KB\n")


def mvt(memory_size, process_sizes):
    print(f"\nTotal Memory: {memory_size} KB")
    used_memory = 0
    external_frag = 0

    print("MVT (Variable Partition) Allocation:")
    for i, process in enumerate(process_sizes):
        if used_memory + process <= memory_size:
            print(f"Process {i+1} ({process} KB) -> Allocated")
            used_memory += process
        else:
            external_frag = memory_size - used_memory
            print(f"Process {i+1} ({process} KB) -> Not Allocated (Insufficient Memory)")
            break

    print(f"\nTotal Used Memory: {used_memory} KB")
    print(f"Total External Fragmentation: {external_frag} KB\n")


if __name__ == "__main__":
    # Example input
    total_memory = 1000  # in KB
    partition_size = 300  # for MFT
    process_sizes = [212, 417, 112, 426]

    print("Memory Management Simulation\n")
    mft(total_memory, partition_size, process_sizes)
    mvt(total_memory, process_sizes)
