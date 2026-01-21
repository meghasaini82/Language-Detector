n = int(input("Enter number of disk requests: "))

requests = []
print("Enter disk request sequence:")
for i in range(n):
    requests.append(int(input()))

head = int(input("Enter initial head position: "))

total_head_movement = 0
current_position = head

print("\nSequence of head movement:")
for req in requests:
    print(f"{current_position} -> {req}")
    total_head_movement += abs(req - current_position)
    current_position = req

print("\nTotal Head Movement:", total_head_movement)
