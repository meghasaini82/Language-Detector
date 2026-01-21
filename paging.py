memory_size = int(input("Enter total memory size (in KB): "))
page_size = int(input("Enter page size (in KB): "))

num_pages = memory_size // page_size
print(f"\nTotal number of pages in memory: {num_pages}")


process_size = int(input("\nEnter process size (in KB): "))
pages_required = process_size // page_size
if process_size % page_size != 0:
    pages_required += 1

print(f"Pages required by process: {pages_required}")

if pages_required > num_pages:
    print("Error: Not enough memory to allocate pages.")
    exit()


page_table = []

print("\nEnter the frame number for each page:")
for i in range(pages_required):
    frame = int(input(f"Page {i} -> Frame: "))
    page_table.append(frame)


print("\n------ PAGE TABLE ------")
print("Page No.\tFrame No.")
for i in range(pages_required):
    print(f"{i}\t\t{page_table[i]}")

print("\nPaging Simulation Completed Successfully.")
