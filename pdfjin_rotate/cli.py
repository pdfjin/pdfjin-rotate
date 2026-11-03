import sys
import argparse
from pathlib import Path
try:
    from .core import rotate_pdf
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_rotate.core import rotate_pdf
    from pdfjin_rotate import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="pdfjin-rotate",
        description="Rotate PDF pages by 90, 180, or 270 degrees.",
        epilog="Online web version available at https://pdfjin.com/pages/rotate-pdf.html",
    )
    parser.add_argument("input", metavar="INPUT_PDF", help="Path to the PDF to rotate")
    parser.add_argument("-a", "--angle", type=int, choices=[90, 180, 270], default=90, help="Rotation angle (default: 90)")
    parser.add_argument("-o", "--output", required=True, help="Destination path for rotated PDF")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    try:
        out = rotate_pdf(args.input, angle=args.angle, output=args.output)
        print(f"🔄 PDF successfully rotated by {args.angle}° -> {out}")
    except Exception as e:
        print(f"❌ Rotation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
