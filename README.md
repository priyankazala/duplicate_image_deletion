# Image Deduplication Web Application

This web application allows users to upload a folder containing images and removes duplicate images, even if they have different resolutions or sizes. The application uses Flask for the backend and a simple HTML form for the frontend.

## Features

- Upload a folder containing images.
- Automatically remove duplicate images based on visual similarity.
- Download the processed folder with duplicates removed.

## Installation

### Prerequisites

- Python 3.6+
- Pip (Python package installer)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/image-deduplication-webapp.git
    cd image-deduplication-webapp
    ```
    

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install Flask Pillow
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Open the application in your web browser.**
2. **Use the form to upload a folder containing images.**
3. **The application will process the folder, removing any duplicate images.**
4. **Download the processed folder as a zip file.**

## File Structure

image-deduplication-webapp/
│
├── app.py # Flask application
├── templates/
│ └── index.html # HTML template for the upload form
├── uploads/ # Directory to store uploaded folders
├── processed/ # Directory to store processed folders
├── venv/ # Virtual environment directory
└── README.md # This README file

## How It Works

1. **Upload Folder**: Users upload a folder containing images using the web form.
2. **Image Processing**: The application processes the images, resizing them to a common resolution and comparing their pixel values to identify duplicates.
3. **Remove Duplicates**: Duplicate images are removed from the uploaded folder.
4. **Download Processed Folder**: The processed folder, with duplicates removed, is zipped and made available for download.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of Flask and Pillow for providing the tools necessary for this project.

## Contact

If you have any questions or feedback, feel free to reach out to [Priyanka Zala](mailto:priyankazala01@gmail.com).
