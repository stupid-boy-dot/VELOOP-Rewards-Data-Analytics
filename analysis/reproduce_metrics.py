#!/usr/bin/env python3
"""Reproduce Task 01 snapshot counts from two CSV exports of the supplied workbook.

Usage:
  python reproduce_metrics.py Users_1000_Clean.csv Users_Messy_Audit.csv

CSV input columns must retain the original source headers. Uses only the Python standard library.
"""
import csv, json, sys
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED = {"user_id", "email_verification_status", "onboarding_status", "is_active_7d",
            "is_active_30d", "acquisition_source", "consent_status", "marketing_opt_in",
            "last_login_datetime", "days_since_registration"}

def read(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"No data rows found in {path}")
    missing = REQUIRED - set(rows[0])
    if missing:
        raise ValueError(f"{path} is missing required columns: {sorted(missing)}")
    return rows

def yes_count(rows, field, expected):
    return sum(1 for r in rows if (r.get(field) or "").strip() == expected)

def run(clean, messy):
    n = len(clean)
    ids = [r.get("user_id", "").strip() for r in clean]
    unique_ids = len({x for x in ids if x})
    checks = {
      "clean_rows": n,
      "unique_non_null_user_ids": unique_ids,
      "verified_email_count": yes_count(clean, "email_verification_status", "Verified"),
      "onboarding_completed_count": yes_count(clean, "onboarding_status", "Completed"),
      "active_7d_yes_count": yes_count(clean, "is_active_7d", "Yes"),
      "active_30d_yes_count": yes_count(clean, "is_active_30d", "Yes"),
      "referral_acquisition_count": yes_count(clean, "acquisition_source", "Referral"),
      "consent_accepted_count": yes_count(clean, "consent_status", "Accepted"),
      "marketing_opt_in_yes_count": yes_count(clean, "marketing_opt_in", "Yes"),
      "last_login_null_count": sum(1 for r in clean if not (r.get("last_login_datetime") or "").strip()),
      "negative_days_since_registration_count": sum(1 for r in clean if _negative(r.get("days_since_registration"))),
    }
    for k in ["verified_email_count", "onboarding_completed_count", "active_7d_yes_count", "active_30d_yes_count", "referral_acquisition_count", "consent_accepted_count", "marketing_opt_in_yes_count"]:
        checks[k.replace("_count", "_rate")] = checks[k] / n if n else None
    messy_ids = [r.get("user_id", "").strip() for r in messy if r.get("user_id", "").strip()]
    freq = Counter(messy_ids)
    checks["messy_audit_rows"] = len(messy)
    checks["messy_audit_unique_non_null_ids"] = len(set(messy_ids))
    checks["messy_audit_excess_duplicate_rows"] = len(messy) - len(set(messy_ids))
    checks["messy_audit_ids_appearing_more_than_once"] = sum(1 for v in freq.values() if v > 1)
    groups = defaultdict(lambda: [0, 0])
    for r in clean:
        src = (r.get("acquisition_source") or "(blank)").strip()
        groups[src][0] += 1
        groups[src][1] += ((r.get("onboarding_status") or "").strip() == "Completed")
    by_source = {k: {"users": v[0], "completed": v[1], "completion_rate": v[1]/v[0] if v[0] else None} for k,v in sorted(groups.items())}
    return {"evidence_label":"SIMULATED / FICTIONAL TASK 01 DATA ONLY", "metrics":checks, "onboarding_by_acquisition_source":by_source}

def _negative(v):
    try: return float(str(v).strip()) < 0
    except (ValueError, TypeError): return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python reproduce_metrics.py Users_1000_Clean.csv Users_Messy_Audit.csv")
    result = run(read(sys.argv[1]), read(sys.argv[2]))
    out = Path("reproduced_metrics.json")
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"\nWrote {out.resolve()}")
