import sys
import os
from urllib.parse import urlparse
from huggingface_hub import snapshot_download
import hf_transfer  # Ensures high-speed transfer is enabled

def ensure_models_folder_exists():
    """
    Ensure that the 'Models' folder exists in the same directory as this script.
    If it doesn't exist, create it.
    """
    models_folder = os.path.join(os.getcwd(), "Models")
    if not os.path.exists(models_folder):
        os.makedirs(models_folder)
    return models_folder

def parse_repo_id(link):
    """
    Parse the repo ID from a pasted Hugging Face model link.
    For example, if the user pastes:
      https://huggingface.co/canopylabs/orpheus-3b-0.1-ft
    this function returns:
      canopylabs/orpheus-3b-0.1-ft
    If the link does not start with 'http', it is assumed to be a valid repo ID.
    """
    if link.startswith("http"):
        parsed = urlparse(link)
        # Remove any trailing slashes and spaces
        repo_id = parsed.path.strip("/")
        return repo_id
    else:
        return link.strip()

def get_folder_name_from_repo(repo_id):
    """
    Convert a Hugging Face repo ID (e.g., 'canopylabs/orpheus-3b-0.1-ft')
    into a folder name by replacing "/" with "_".
    For instance, 'canopylabs/orpheus-3b-0.1-ft' becomes 'canopylabs_orpheus-3b-0.1-ft'.
    """
    return repo_id.replace("/", "_")

def main():
    # Ensure the Models folder exists
    models_folder = ensure_models_folder_exists()

    # Ask the user to paste one or more Hugging Face model links (comma-separated)
    model_links_input = input("Please paste one or more Hugging Face model links (separated by commas): ").strip()
    if not model_links_input:
        print("No model links provided. Exiting.")
        sys.exit(1)

    # Process each provided link in the order given
    model_links = [link.strip() for link in model_links_input.split(",") if link.strip()]
    
    for link in model_links:
        repo_id = parse_repo_id(link)
        folder_name = get_folder_name_from_repo(repo_id)
        local_dir = os.path.join(models_folder, folder_name)
        print(f"Downloading model from '{repo_id}' into '{local_dir}' ...")
        snapshot_download(repo_id=repo_id, local_dir=local_dir)
        print(f"Download complete for model '{repo_id}'.\n")
    
    print("All downloads complete.")

if __name__ == "__main__":
    main()
