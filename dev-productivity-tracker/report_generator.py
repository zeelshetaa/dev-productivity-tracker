from datetime import datetime


def generate_report(data):

    print("\n-----------------------------------")
    print("Developer Productivity Report")
    print("-----------------------------------")

    print(f"Report Time      : {datetime.now()}")
    print(f"Total Commits    : {data['commits']}")
    print(f"Files Modified   : {data['files_changed']}")
    print(f"Lines Added      : {data['lines_added']}")
    print(f"Lines Removed    : {data['lines_removed']}")

    net = data["lines_added"] - data["lines_removed"]

    print(f"Net Code Change  : {net}")

    if net > 500:
        productivity = "High"
    elif net > 100:
        productivity = "Moderate"
    else:
        productivity = "Low"

    print(f"Productivity Level : {productivity}")

    print("-----------------------------------\n")