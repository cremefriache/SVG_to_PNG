# Save this file as convert_svg_rl_arg.py
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import sys
import os

# Check if the correct number of arguments were provided
if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    script_name = os.path.basename(sys.argv[0])
    print(f"Usage: python {script_name} <input_svg_path> <output_png_path>")
    print(r"Or drag-and-drop the SVG file onto the 'convert_svg.bat' file.")
    sys.exit(1) # Exit the script indicating an error

input_svg_path = sys.argv[1]
output_png_path = sys.argv[2]

try:
    print(f"Input SVG path: {input_svg_path}")
    print(f"Output PNG path: {output_png_path}")

    # Check if the input SVG file exists
    if not os.path.exists(input_svg_path):
        print(f"Error: Input SVG file not found at '{input_svg_path}'")
        sys.exit(1) # Exit the script

    # --- Perform the conversion ---
    print("Reading SVG file using svglib...")
    # Read the SVG file into a ReportLab Drawing object
    drawing = svg2rlg(input_svg_path)

    if drawing is None:
        print("Error: Failed to parse SVG file. It might be invalid or unsupported.")
        sys.exit(1)

    print("Rendering to PNG using reportlab/Pillow...")
    # Render the drawing object to a PNG file
    renderPM.drawToFile(drawing, output_png_path, fmt='PNG')
    # -----------------------------

    print("-" * 20)
    print(f"Successfully created PNG: {output_png_path}")
    print("-" * 20)

except ImportError as e:
    print(f"Error: A required library is not found: {e}")
    print("Please ensure 'svglib', 'reportlab', and 'Pillow' are installed:")
    print("pip install --user svglib reportlab Pillow")
    sys.exit(1)
except FileNotFoundError:
    # Should be caught by os.path.exists, but just in case
    print(f"Error: Could not find the input SVG file: '{input_svg_path}'")
    sys.exit(1)
except Exception as e:
    # Catch other potential errors during parsing or rendering
    print(f"An unexpected error occurred during conversion: {e}")
    # You might see errors here if the SVG uses features svglib/reportlab don't support
    sys.exit(1)