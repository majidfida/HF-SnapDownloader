# HF SnapDownloader

**HF SnapDownloader** is a lightweight, high-speed command-line tool that downloads models from Hugging Face using the `snapshot_download` API along with the `hf_transfer` package for accelerated transfers. The script prompts you to paste one or multiple Hugging Face model links (comma-separated) and downloads each model sequentially into a dedicated folder named after its original repository ID.

## Features

- **High-Speed Downloads:** Leverages the power of `huggingface_hub` and `hf_transfer` to deliver fast download speeds.
- **Multi-Model Support:** Accepts multiple model links and processes them one after the other, saving each model into its own folder.
- **User-Friendly Setup:** Includes batch scripts to create an isolated virtual environment, install dependencies, and start the downloader effortlessly.
- **Automatic Directory Management:** The script automatically creates a `Models` folder (or a subfolder based on repo ID) in the same directory as the script if it does not exist.

## Requirements

- Python (with a system default installation)
- The following Python packages:
  - [huggingface_hub](https://github.com/huggingface/huggingface_hub)
  - [hf_transfer](https://github.com/huggingface/hf_transfer) 

## Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/hf-snapdownloader.git
   cd hf-snapdownloader
   ```

2. **Run the Installer:**

   Double-click the `installer.bat` file (Windows) which will:
   - Create an isolated virtual environment.
   - Upgrade pip and install the required packages.
   - Start the application via `start.bat`.

   Alternatively, you can run it from a command prompt:

   ```bat
   installer.bat
   ```

## How to Use

When you run the script, it will prompt:

```
Please paste one or more Hugging Face model links (separated by commas):
```

Enter the links (e.g., https://huggingface.co/example/model1, https://huggingface.co/example/model2`) and press Enter. The tool will then download the models sequentially, saving each in a folder that replicates the original repository name (with "/" replaced by "_").

## Credits

- **[huggingface_hub](https://github.com/huggingface/huggingface_hub):** Provides the snapshot download functionality.
- **[hf_transfer](https://github.com/huggingface/hf_transfer):** Enhances download speeds by optimizing file transfers.

Special thanks to Hugging Face for the awesome model hosting and their powerful libraries.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
