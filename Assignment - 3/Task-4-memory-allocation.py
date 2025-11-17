# memory_allocation.py

def first_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
    return allocation


def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        best_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if best_index == -1 or block_size[j] < block_size[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]
    return allocation


def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        worst_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if worst_index == -1 or block_size[j] > block_size[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_size[worst_index] -= process_size[i]
    return allocation


def display_result(strategy_name, allocation, process_size):
    print(f"\n{strategy_name} Allocation Results:")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_size)):
        if allocation[i] != -1:
            print(f"{i + 1}\t\t{process_size[i]}\t\t{allocation[i] + 1}")
        else:
            print(f"{i + 1}\t\t{process_size[i]}\t\tNot Allocated")


if __name__ == "__main__":
    # Example input
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]

    print("Memory Blocks:", block_size)
    print("Process Sizes:", process_size)

    ff_alloc = first_fit(block_size.copy(), process_size)
    bf_alloc = best_fit(block_size.copy(), process_size)
    wf_alloc = worst_fit(block_size.copy(), process_size)

    display_result("First Fit", ff_alloc, process_size)
    display_result("Best Fit", bf_alloc, process_size)
    display_result("Worst Fit", wf_alloc, process_size)
