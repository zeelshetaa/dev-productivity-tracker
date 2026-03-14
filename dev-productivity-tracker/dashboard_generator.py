import matplotlib.pyplot as plt

def generate_commit_graph(activity):

    dates = list(activity.keys())
    commits = list(activity.values())

    plt.figure(figsize=(10,5))
    plt.plot(dates, commits, marker='o')
    plt.xticks(rotation=45)

    plt.title("Commit Activity")
    plt.xlabel("Date")
    plt.ylabel("Commits")

    plt.tight_layout()
    plt.savefig("commit_activity.png")


def generate_html_dashboard(data):

    html = f"""
    <html>
    <head>
        <title>Developer Productivity Dashboard</title>
        <style>
        body {{
            font-family: Arial;
            margin: 40px;
        }}
        .card {{
            background:#f4f4f4;
            padding:20px;
            margin:10px;
            border-radius:8px;
        }}
        </style>
    </head>

    <body>

    <h1>Developer Productivity Dashboard</h1>

    <div class="card">
        <h2>Commit Statistics</h2>
        <p>Total Commits: {data['commits']}</p>
        <p>Lines Added: {data['lines_added']}</p>
        <p>Lines Removed: {data['lines_removed']}</p>
    </div>

    <div class="card">
        <h2>Developer Activity</h2>
        <p>Estimated Coding Hours: {data['hours']}</p>
        <p>Activity Level: {data['activity_level']}</p>
    </div>

    <div class="card">
        <h2>Commit Graph</h2>
        <img src="commit_activity.png" width="700">
    </div>

    </body>
    </html>
    """

    with open("dashboard.html", "w") as f:
        f.write(html)
