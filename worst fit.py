
block_count = int(input("Enter number of memory blocks: "))
block_size = []
block_allocated = [0] * block_count

print("Enter size of each block:")
for i in range(block_count):
    block_size.append(int(input()))


process_count = int(input("\nEnter number of processes: "))
process_size = []
allocation = [-1] * process_count

print("Enter size of each process:")
for i in range(process_count):
    process_size.append(int(input()))


for i in range(process_count):
    worst_index = -1

    for j in range(block_count):
        if block_allocated[j] == 0 and block_size[j] >= process_size[i]:
            if worst_index == -1 or block_size[j] > block_size[worst_index]:
                worst_index = j

    if worst_index != -1:
        allocation[i] = worst_index
        block_allocated[worst_index] = 1


print("\nProcess No.\tProcess Size\tBlock Allocated")
for i in range(process_count):
    print(f"{i+1}\t\t{process_size[i]}\t\t", end="")
    if allocation[i] != -1:
        print(allocation[i] + 1)
    else:
        print("Not Allocated")
