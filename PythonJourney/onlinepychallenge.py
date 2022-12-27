
def online_count(statuses):
    count = 0
    for key, value in statuses.items():
        if value == "online":
            count += 1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
