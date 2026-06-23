#!/usr/bin/env python3

import argparse
import sys

DEFAULT_STAGES = [
    "Build",
    "Test",
    "Deploy",
]


def validate_jenkinsfile(path, expected_stages=None):
    if expected_stages is None:
        expected_stages = DEFAULT_STAGES
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Jenkinsfile not found: {path}")
        return None

    missing_stages = [stage for stage in expected_stages if stage not in content]
    return missing_stages


def main():
    parser = argparse.ArgumentParser(description="Jenkins pipeline test tool")
    parser.add_argument("jenkinsfile", help="Path to the Jenkinsfile to validate")
    parser.add_argument(
        "--stages",
        nargs="+",
        help="Expected pipeline stages to verify",
        default=DEFAULT_STAGES,
    )
    args = parser.parse_args()

    missing = validate_jenkinsfile(args.jenkinsfile, args.stages)
    if missing is None:
        return 2
    if missing:
        print("Missing expected pipeline stages:", ", ".join(missing))
        return 1

    print("Jenkins pipeline test passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
