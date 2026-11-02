"""Compatibility entry point for the bilingual document generator."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("render_bilingual.py")), run_name="__main__")
