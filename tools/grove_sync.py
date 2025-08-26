#!/usr/bin/env python3
import json, os, time, subprocess

def calc_grade(metrics):
    score = 0
    score += 15 if metrics["ci_pass"] else 0
    score += 15 if metrics["lint_clean"] else 0
    score += 15 if metrics["web_up"] else 0
    score += 15 if metrics["telnet_up"] else 0
    score += 15 if metrics["timelapse_fresh"] else 0
    score += max(0, 25 - min(metrics["open_bugs"]*5, 25))
    return ("FDCBAA"[min(5, score // 20)], score)

def main():
    metrics = {
        "ci_pass": True,            # pull from GH checks
        "lint_clean": True,         # parse CI logs or run locally
        "web_up": True,             # simple curl
        "telnet_up": True,          # simple nc
        "timelapse_fresh": False,   # mtime < 24h
        "open_bugs": 3,             # from GitHub Issues label=bug
    }
    letter, score = calc_grade(metrics)
    out = {"grade": letter, "score": score, "metrics": metrics, "updated": time.ctime()}
    dst = os.path.join(os.path.dirname(__file__), "..", "web", "static", "telemetry", "grade.json")
    with open(os.path.abspath(dst), "w") as f:
        json.dump(out, f, indent=2)
    print("Wrote", dst)

if __name__ == "__main__":
    main()