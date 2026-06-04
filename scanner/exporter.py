import json


def save_json_report(target, results):
    report = {
        "target": target,
        "results": results
    }

    with open("reports/scan_results.json", "w") as file:
        json.dump(report, file, indent=4)