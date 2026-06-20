#!/usr/bin/env python3

import argparse
import sys
import math

DEFAULT_STAGES = [
    "Build",
    "Test",
    "Deploy",
]


def validate_jenkinsfile(path, expected_stages=None):
    expected_stages = expected_stages or DEFAULT_STAGES
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    missing_stages = [stage for stage in expected_stages if stage not in content]
    return missing_stages


def main():
    parser = argparse.ArgumentParser(description="Jenkins pipeline test tool")
    parser.add_argument("jenkinsfile", help="Path to the Jenkinsfile to validate")
    parser.add_argument(
        "--stages",
        nargs="*",
        help="Expected pipeline stages to verify",
        default=DEFAULT_STAGES,
    )
    args = parser.parse_args()

    missing = validate_jenkinsfile(args.jenkinsfile, args.stages)
    if missing:
        print("Missing expected pipeline stages:", ", ".join(missing))
        return 1

    print("Jenkins pipeline test passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
