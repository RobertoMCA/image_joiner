library(magick)
library(testthat)

test_join_images <- function() {
  test_that("join_images works correctly", {
    # Create test images
    image_left_path <- "./test_images/test_left.png"
    image_right_path <- "./test_images/test_right.png"
    
    # Create a temporary directory for test images
    dir.create('./test_images', showWarnings = FALSE)
    
    # Create some test images
    image_left <- image_blank(width = 100, height = 100, color = "red")
    image_right <- image_blank(width = 100, height = 100, color = "blue")
    
    image_write(image_left, path = image_left_path)
    image_write(image_right, path = image_right_path)
    
    # Run the join_images function
    result <- join_images(image_left_path, image_right_path, separation = 10, border = 5, background = 'white')
    
    # Save the result
    image_write(result, './test_images/joined_test_image.png')
    
    # Check the resulting image size
    expect_equal(image_info(result)$width, 220)  # 100 + 100 + 10 + 2 * 5
    expect_equal(image_info(result)$height, 110)  # 100 + 2 * 5
    
    # Clean up test images
    unlink('./test_images', recursive = TRUE)
  })
}

# Run the test
test_join_images()
