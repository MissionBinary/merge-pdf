# Flask PDF Merge API

This API merges multiple PDF files into one, with an option to specify the output filename.

## Deployment on Railway

1. Push to GitHub
2. Deploy using Railway
3. Set environment variable `PORT=5000`

## Usage

### Request (POST `/merge-pdfs`)
- **files** (multipart/form-data): Upload multiple PDFs
- **filename** (form-data, optional): Desired name for the merged file (default: `merged.pdf`)

### Example (cURL)
```sh
curl -X POST -F "files=@file1.pdf" -F "files=@file2.pdf" -F "filename=custom_name.pdf" https://your-railway-url/merge-pdfs --output custom_name.pdf
```

### Response
- Returns the merged PDF as a file download.
- If no `filename` is provided, it defaults to `merged.pdf`.
- Errors:
  ```json
  { "error": "No files uploaded" }
  ```
  