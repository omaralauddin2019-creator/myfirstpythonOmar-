files = [
    {"name": "report.pdf", "size_mb": 15},
    {"name": "photo.png", "size_mb": 3},
    {"name": "video.mp4", "size_mb": 120}
]

def size_mb(box):
    total = 0
    for size in box:
        total = total + size["size_mb"]
    return total

for size in files:
    if size["size_mb"] >= 50:
        print(f"{size['name']} is too large")
    else:
        print(f"{size['name']} is fine")

with open("size.txt", "w") as file:
    for size in files:
        file.write(f"{size['name']} and the {size['size_mb']}\n")

try:
    with open("size.txt", "r") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    print("File Doesnt Exist")