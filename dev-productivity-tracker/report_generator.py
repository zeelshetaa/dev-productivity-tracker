from datetime import datetime


def generate_report(data, score, level, insights, recommendations):

    print("\n===================================")
    print("AI Developer Productivity Report")
    print("===================================")

    print(f"Time                : {datetime.now()}")
    print(f"Total Commits       : {data['commits']}")
    print(f"Files Changed       : {data['files_changed']}")
    print(f"Lines Added         : {data['lines_added']}")
    print(f"Lines Removed       : {data['lines_removed']}")

    print(f"\nProductivity Score  : {score}")
    print(f"Productivity Level  : {level}")

    print("\nInsights:")
    for k, v in insights.items():
        print(f"- {k}: {v}")

    print("\nAI Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")

    print("===================================\n")
