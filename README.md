# Image Joiner

A script to join two images side by side with optional resizing, borders, and background colors. Available in both Python and R.

## Features

- Joins two images side by side
- Optional resizing of images
- Customizable separation between images
- Optional border around images
- Customizable background color (black, white, or transparent)

## Installation

### Python

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image_joiner.git
    cd image_joiner
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r Python/requirements.txt
    ```

### R

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image_joiner.git
    cd image_joiner
    ```

2. Install the required R packages:
    ```R
    install.packages("magick")
    install.packages("testthat")
    ```

## Usage

### Python

1. To join two images, use the `join_images` function:

    ```python
    from image_joiner import join_images

    image_left = "./images_to_join/plot1a.png"
    image_right = "./images_to_join/plot1b.png"
    result = join_images(image_left, image_right, separation=50, border=20, background='white')
    result.save('./joined_images/joined_image.png')
    result.show()
    ```

2. To run the tests:

    ```bash
    python -m unittest Python/test_image_joiner.py
    ```

### R

1. To join two images, use the `join_images` function:

    ```R
    source("R/image_joiner.R")

    image_left <- "./images_to_join/plot1a.png"
    image_right <- "./images_to_join/plot1b.png"
    result <- join_images(image_left, image_right, separation = 50, border = 20, background = 'white')
    image_write(result, './joined_images/joined_image.png')
    ```

2. To run the tests:

    ```R
    source("R/test_image_joiner.R")
    ```

## Project Structure

image_joiner/
├── R/
│ ├── image_joiner.R
│ ├── test_image_joiner.R
├── Python/
│ ├── init.py
│ ├── image_joiner.py
│ ├── test_image_joiner.py
│ ├── requirements.txt
├── images_to_join/
│ ├── plot1a.png
│ ├── plot1b.png
├── joined_images/
│ ├── joined_image.png
├── .gitignore
├── README.md


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
