import requests
from pathlib import Path

def download_to_local(url: str, out_path: Path, parent_mkdir: bool = True) -> bool:
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib.Path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Check the content type to ensure we are getting the expected file type
        content_type = response.headers.get('Content-Type')
        print(f'Downloading {url} with content type: {content_type}')
        
        if 'text/html' in content_type:
            print(f'Error: URL {url} is serving HTML content instead of the expected file.')
            return False
        
        # Write the file out in binary mode to prevent any newline conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False
