from PIL import Image, ExifTags

def extract_metadata(img_path):
    try:
        img = Image.open(img_path)
        exif_data = img._getexif()
        if not exif_data:
            return "No EXIF metadata found"
        metadata = {}
        for tag_id, value in exif_data.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            metadata[tag] = str(value)
        return f"Camera: {metadata.get('Model', 'Unknown')}, Software: {metadata.get('Software', 'Unknown')}"
    except Exception as e:
        return f"Metadata extraction failed: {str(e)}"