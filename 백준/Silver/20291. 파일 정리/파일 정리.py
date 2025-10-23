N = int(input())
extension_counts = {}

for _ in range(N):
    fileName = input()
    extensionName = fileName.split(".")[1]
    if extensionName in extension_counts:
        extension_counts[extensionName] += 1
    else:
        extension_counts[extensionName] = 1

extension_list = list(extension_counts.keys())
extension_list = sorted(extension_list)

for e in extension_list:
    print(f"{e} {extension_counts[e]}")