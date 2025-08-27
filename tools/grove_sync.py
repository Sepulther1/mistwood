#!/usr/bin/env python3
import json, time, pathlib

ROOT      = pathlib.Path(__file__).resolve().parents[1]
TELEMETRY = ROOT / "web" / "static" / "telemetry"
TELEMETRY.mkdir(parents=True, exist_ok=True)
GRADE     = TELEMETRY / "grade.json"

def ewma(prev, x, alpha=0.35):
    return x if prev is None else (alpha * x + (1 - alpha) * prev)

def calc_score(metrics):
    score = 0
    score += 15 if metrics.get("ci_pass")         else 0
    score += 15 if metrics.get("lint_clean")      else 0
    score += 15 if metrics.get("web_up")          else 0
    score += 15 if metrics.get("telnet_up")       else 0
    score += 15 if metrics.get("timelapse_fresh") else 0
    score += max(0, 25 - min(metrics.get("open_bugs", 0) * 5, 25))
    return max(0, min(100, score))

def letter(score):
    return "FDCBAA"[min(5, score // 20)]

def load_prev():
    if GRADE.exists():
        try:
            return json.loads(GRADE.read_text())
        except Exception:
            pass
    return {"history": [], "block": 0, "trend_ewma": None}

def main():
    prev = load_prev()

    # TODO: replace these with real checks
    metrics = {
        "ci_pass": True,
        "lint_clean": True,
        "web_up": True,
        "telnet_up": True,
        "timelapse_fresh": True,
        "open_bugs": 3,
    }

    score = calc_score(metrics)
    hist  = (prev.get("history") or [])[-19:] + [score]
    trend = ewma(prev.get("trend_ewma"), score)
    block = int(prev.get("block") or 0) + 1

    out = {
        "grade":      letter(score),
        "score":      score,
        "metrics":    metrics,
        "updated":    time.strftime("%Y-%m-%d %H:%M:%S"),
        "block":      block,
        "history":    hist,
        "trend_ewma": trend,
    }
    GRADE.write_text(json.dumps(out, indent=2))
    print("Wrote", GRADE)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import json, time, pathlib

ROOT      = pathlib.Path(__file__).resolve().parents[1]
TELEMETRY = ROOT / "web" / "static" / "telemetry"
TELEMETRY.mkdir(parents=True, exist_ok=True)
GRADE     = TELEMETRY / "grade.json"

def ewma(prev, x, alpha=0.35):
    return x if prev is None else (alpha * x + (1 - alpha) * prev)

def calc_score(metrics: dict) -> int:
    score = 0
    score += 15 if metrics.get("ci_pass")         else 0
    score += 15 if metrics.get("lint_clean")      else 0
    score += 15 if metrics.get("web_up")          else 0
    score += 15 if metrics.get("telnet_up")       else 0
    score += 15 if metrics.get("timelapse_fresh") else 0
    score += max(0, 25 - min(metrics.get("open_bugs", 0) * 5, 25))
    return max(0, min(100, score))

def letter(score: int) -> str:
    return "FDCBAA"[min(5, score // 20)]

def load_prev():
    try:
        return json.loads(GRADE.read_text())
    except Exception:
        return {"history": [], "block": 0, "trend_ewma": None}

def main():
    prev = load_prev()
    # TODO: Replace stubs with real checks
    metrics = {
        "ci_pass": True,
        "lint_clean": True,
        "web_up": True,
        "telnet_up": True,
        "timelapse_fresh": True,
        "open_bugs": 3,
    }
    score = calc_score(metrics)
    hist  = (prev.get("history") or [])[-19:] + [score]
    trend = ewma(prev.get("trend_ewma"), score)
    block = int(prev.get("block") or 0) + 1

    out = {
        "grade":      letter(score),
        "score":      score,
        "metrics":    metrics,
        "updated":    time.strftime("%Y-%m-%d %H:%M:%S"),
        "block":      block,
        "history":    hist,
        "trend_ewma": trend,
    }
    GRADE.write_text(json.dumps(out, indent=2))
    print("Wrote", GRADE)

if __name__ == "__main__":
    main()