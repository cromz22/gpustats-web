def main():
    servers = ["server1", "server2"]
    server_info = {
        "server1": [
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
        ],
        "server2": [
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1", "user2"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "23542 GiB",
                "utilization": "45 %",
                "user": ["user1", "user2"],
            },
            {
                "timestamp": "2023/09/01 00:00:00.000",
                "name": "Tesla V100",
                "total memory": "32768 GiB",
                "used memory": "0 GiB",
                "utilization": "0 %",
                "user": [""],
            },
        ],
    }

    header = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPU Monitoring</title>
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <div class="container">
        <h1>GPU Monitoring</h1>
"""

    table = """
        <table class="table">
            <thead>
                <tr>
                    <th>Hostname</th>"""

    max_n_gpu_cards_per_machine = 8

    for i in range(max_n_gpu_cards_per_machine):
        table += f"""
                    <th>{i}</th>"""

    table += """
                </tr>
            </thead>
            <tbody>"""

    for server in servers:
        table += f"""
                <tr>
                    <td>{server}</td>"""

        counter = 0
        for info in server_info[server]:
            if info["user"] == [""]:
                color = "bg-success"
            else:
                color = "bg-danger"
            info_box = ""
            for k, v in info.items():
                if k == "user":
                    info_box += f"{k}: {', '.join(info['user'])}"
                else:
                    info_box += f"{k}: {v}<br>"
            table += f"""
                    <td>
                        <div class="circle {color}" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="bottom" title="{info_box}"></div>
                    </td>"""
            counter += 1

        if counter != max_n_gpu_cards_per_machine:
            for _ in range(max_n_gpu_cards_per_machine - counter):
                table += """
                    <td></td>"""

        table += """
                </tr>"""

    table += """
            </tbody>
        </table>
    """

    footer = """
    </div>
	<script>
		var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
		var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
		  return new bootstrap.Tooltip(tooltipTriggerEl)
		})
	</script>
</body>
</html>
"""

    html = header + table + footer
    with open("index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
