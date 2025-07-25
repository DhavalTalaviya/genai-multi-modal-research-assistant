from pathlib import Path
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from langchain.schema import Document
from config.settings import image_dir, processed_captions_dir, caption_model

# Load model & processor once
processor = BlipProcessor.from_pretrained(caption_model)
model     = BlipForConditionalGeneration.from_pretrained(caption_model)

def generate_caption(image_path: str) -> str:
    """Generate a single caption for the given image file."""
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out_ids = model.generate(**inputs)
    return processor.decode(out_ids[0], skip_special_tokens=True)

def load_image_captions(img_dir: str) -> list[Document]:
    """
    Read all images in img_dir, generate captions,
    and return as LangChain Documents.
    """
    docs = []
    for img_path in Path(img_dir).glob("*.*"):
        try:
            caption = generate_caption(str(img_path))
            docs.append(Document(
                page_content=caption,
                metadata={"source": str(img_path)}
            ))
        except Exception as e:
            print(f"⚠️ Skipping {img_path.name}: {e}")
    return docs

if __name__ == "__main__":
    # Load & save captions
    docs = load_image_captions(image_dir)
    print(f"Generated {len(docs)} captions from images in '{image_dir}'.")
    Path(processed_captions_dir).mkdir(parents=True, exist_ok=True)

    for doc in docs:
        src = Path(doc.metadata["source"])
        out = Path(processed_captions_dir) / f"{src.stem}.txt"
        out.write_text(doc.page_content, encoding="utf-8")

    print(f"Saved captions to '{processed_captions_dir}'.")
