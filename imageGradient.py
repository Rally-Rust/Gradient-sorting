import sys
from pathlib import Path
import numpy as np
from PIL import Image

def make_horizontal_gradient(input_path: str, output_path: str | None = None) -> str:
    src = Path(input_path)
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if output_path is None:
        output_path = str(src.parent / f"{src.stem}_gradient.png")

    img = Image.open(src).convert("RGB")
    arr = np.array(img, dtype=np.float64)

    H, W, _ = arr.shape
    col_avg = arr.mean(axis=0)

    gradient = np.tile(col_avg, (H,1,1))
    gradient = np.clip(gradient, 0, 255).astype(np.uint8)

    out_img = Image.fromarray(gradient, mode="RGB")
    out_img.save(output_path)
    print(f"Gradient saved to: {output_path}")
    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python image_gradient.py <input_image> [output_image]")
        sys.exit(1)
 
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) >= 3 else None
    make_horizontal_gradient(inp, out)

if __name__ == "__main__":
    main()
