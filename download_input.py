#!/usr/bin/env python3
"""
Download Advent of Code input for a specific day.

Requires AOC_SESSION environment variable or .aoc_session file.
Usage:
    python download_input.py 1      # Download day 1 input for current year
    python download_input.py 5 2024 # Download day 5 input for 2024
"""

import sys
import os
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional
from datetime import datetime
import argparse


def get_current_year() -> int:
    """Get the current year."""
    return datetime.now().year


def get_current_day() -> int:
    """Get the current day in December, or 25 if not December."""
    today = datetime.now()
    if today.month == 12:
        return min(today.day, 25)
    return 25


def get_session_cookie() -> Optional[str]:
    """
    Get AOC session cookie from environment or .aoc_session file.

    Returns:
        Session cookie string or None
    """
    # Try environment variable first
    session = os.getenv("AOC_SESSION")
    if session:
        return session

    # Try .aoc_session file
    session_file = Path(__file__).parent / ".aoc_session"
    if session_file.exists():
        return session_file.read_text().strip()

    return None


def download_input(day: int, year: Optional[int] = None) -> Optional[str]:
    """
    Download AoC input for a specific day.

    Args:
        day: Day number (1-25)
        year: Year (default: current year)

    Returns:
        Input data as string, or None if download fails
    """
    if year is None:
        year = get_current_year()

    if not 1 <= day <= 25:
        print(f"❌ Error: Day must be between 1 and 25, got {day}")
        return None

    session_cookie = get_session_cookie()
    if not session_cookie:
        print("❌ Error: AOC session cookie not found!")
        print("   Set AOC_SESSION environment variable or create .aoc_session file")
        print("   See README.md for instructions on getting your session cookie")
        return None

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    try:
        headers = {
            "User-Agent": "aoc-client (https://github.com/user/Advent-of-Code-2025)",
            "Cookie": f"session={session_cookie}"
        }

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8").strip()

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Error: Day {day} not found (advent not started yet?)")
        elif e.code == 401:
            print(f"❌ Error: Invalid session cookie")
        else:
            print(f"❌ HTTP Error {e.code}: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Error downloading input: {e}")
        return None


def save_input(day: int, content: str, year: Optional[int] = None) -> bool:
    """
    Save input to day folder.

    Args:
        day: Day number
        content: Input content
        year: Year (default: current year)

    Returns:
        True if successful, False otherwise
    """
    if year is None:
        year = get_current_year()

    day_folder = Path(__file__).parent / f"aoc{year}" / f"day{day}"
    input_file = day_folder / "input.txt"

    if not day_folder.exists():
        print(f"❌ Error: day{day} folder not found")
        print(f"   Create it first with: python main.py create {day} --year {year}")
        return False

    try:
        input_file.write_text(content)
        print(f"✅ Downloaded input for {year} day {day}")
        print(f"   Saved to: {input_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving input: {e}")
        return False


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download Advent of Code input for a specific day",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python download_input.py 5              # Download day 5 for current year
  python download_input.py 5 2024         # Download day 5 for 2024
  python download_input.py 5 -y 2024      # Download day 5 for 2024 (short form)
        """
    )

    parser.add_argument("day", type=int, help="Day number (1-25)")
    parser.add_argument("year", nargs="?", type=int, default=None,
                       help="Year (default: current year)")
    parser.add_argument("-y", "--year-flag", type=int, default=None, dest="year_flag",
                       help="Year using -y flag (overrides positional year)")

    args = parser.parse_args()

    # Use year_flag if provided, otherwise use positional year argument
    year = args.year_flag if args.year_flag is not None else args.year
    if year is None:
        year = get_current_year()

    print(f"📥 Downloading input for Day {args.day} ({year})...")
    content = download_input(args.day, year)

    if content is not None:
        if save_input(args.day, content, year):
            sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
