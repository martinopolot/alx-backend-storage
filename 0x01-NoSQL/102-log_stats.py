from pymongo import MongoClient

def get_top_10_ips(db_name, collection_name):
    client = MongoClient()
    db = client[db_name]
    collection = db[collection_name]

    pipeline = [
        {"$group": {"_id": "$remote_addr", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips = list(collection.aggregate(pipeline))
    return top_ips

if __name__ == "__main__":
    db_name = "logs"  # Replace with your database name
    collection_name = "nginx"  # Replace with your collection name

    top_ips = get_top_10_ips(db_name, collection_name)

    print("Top 10 IPs:")
    for idx, ip_info in enumerate(top_ips, 1):
        print(f"{idx}. IP: {ip_info['_id']}, Count: {ip_info['count']}")
