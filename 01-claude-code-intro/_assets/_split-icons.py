"""Split downloaded 2x2 grid PNGs into 8 individual icons for slide 7."""
from PIL import Image
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"
OUT = Path(__file__).parent

# Mapping: (source file, position TL/TR/BL/BR) -> output filename
MAP = {
    "use-learn.png":      ("gpt-icons-batch-A.png", "TL"),  # 開いた本+輝き
    "use-comm.png":       ("gpt-icons-batch-A.png", "TR"),  # チャット吹き出し
    "use-code.png":       ("gpt-icons-batch-A.png", "BR"),  # ノートPC+コード
    "use-research.png":   ("gpt-icons-batch-B.png", "TR"),  # 書類+虫眼鏡
    "use-slide.png":      ("gpt-icons-batch-B.png", "BR"),  # プレゼン板
    "use-doc.png":        ("gpt-icons-batch-D.png", "TL"),  # ペーパー+テキスト
    "use-automation.png": ("gpt-icons-batch-D.png", "TR"),  # 歯車+コンベア
    "use-creative.png":   ("gpt-icons-batch-D.png", "BL"),  # カメラ+絵筆
}

def crop(img, pos):
    w, h = img.size
    half_w, half_h = w // 2, h // 2
    boxes = {
        "TL": (0, 0, half_w, half_h),
        "TR": (half_w, 0, w, half_h),
        "BL": (0, half_h, half_w, h),
        "BR": (half_w, half_h, w, h),
    }
    return img.crop(boxes[pos])

for out_name, (src_name, pos) in MAP.items():
    src = DOWNLOADS / src_name
    img = Image.open(src)
    cropped = crop(img, pos)
    # Resize to a reasonable icon size to keep slide assets light
    cropped = cropped.resize((360, 360), Image.LANCZOS)
    out_path = OUT / out_name
    cropped.save(out_path, optimize=True)
    print(f"OK  {out_name}  <- {src_name} {pos}  ({out_path.stat().st_size} bytes)")
