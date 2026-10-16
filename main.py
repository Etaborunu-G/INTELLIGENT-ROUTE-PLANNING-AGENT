"""Owner: Member 4. Application entry point."""
import argparse
from ui import launch_app


def main() -> None:
    parser = argparse.ArgumentParser(description="Intelligent Route-Planning Agent")
    parser.add_argument("--status", action="store_true", help="Show scaffold status")
    args = parser.parse_args()
    if args.status:
        print("Starter scaffold ready. Algorithms, maps and UI are TODO.")
        return
    try:
        launch_app()
    except NotImplementedError as error:
        parser.exit(2, f"Not implemented yet: {error}\n")


if __name__ == "__main__":
    main()
