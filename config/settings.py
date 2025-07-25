import yaml
from pathlib import Path

_config_path = Path(__file__).parent / "settings.yaml"

with _config_path.open("r") as f:
    _cfg = yaml.safe_load(f)

pdf_dir                  = _cfg["pdf_dir"]
html_dir                 = _cfg["html_dir"]
image_dir                = _cfg["image_dir"]
processed_text_dir       = _cfg["processed_text_dir"]
processed_captions_dir   = _cfg["processed_captions_dir"]
caption_model            = _cfg["caption_model"]
