from datetime import datetime

def print_console_report(data):

    print("\nDeveloper Productivity Report")
    print("-----------------------------------")

    print(f"Report Generated : {datetime.now()}")
    print(f"Total Commits    : {data['commits']}")
    print(f"Lines Added      : {data['lines_added']}")
    print(f"Lines Removed    : {data['lines_removed']}")

    net = data["lines_added"] - data["lines_removed"]

    print(f"Net Code Change  : {net}")
    print(f"Estimated Coding Hours : {data['hours']}")
    print(f"Activity Level   : {data['activity_level']}")

    print("-----------------------------------\n")
