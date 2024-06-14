library(magick)

join_images <- function(image_left_path, image_right_path, separation = 0, border = 0, 
                        new_width_left = NULL, new_height_left = NULL, 
                        new_width_right = NULL, new_height_right = NULL, 
                        background = 'none') {
  
  # Load images
  image_left <- image_read(image_left_path)
  image_right <- image_read(image_right_path)
  
  # Resize images if dimensions are provided
  if (!is.null(new_width_left) & !is.null(new_height_left)) {
    image_left <- image_resize(image_left, paste0(new_width_left, "x", new_height_left, "!"))
  }
  if (!is.null(new_width_right) & !is.null(new_height_right)) {
    image_right <- image_resize(image_right, paste0(new_width_right, "x", new_height_right, "!"))
  }
  
  # Create a blank image for the background
  total_width <- image_info(image_left)$width + image_info(image_right)$width + separation + 2 * border
  max_height <- max(image_info(image_left)$height, image_info(image_right)$height) + 2 * border
  
  if (background == 'black') {
    bg_color <- "black"
  } else if (background == 'white') {
    bg_color <- "white"
  } else {  # 'none'
    bg_color <- "none"
  }
  
  new_img <- image_blank(width = total_width, height = max_height, color = bg_color)
  
  # Composite the images onto the new image
  new_img <- image_composite(new_img, image_left, offset = paste0("+", border, "+", border))
  new_img <- image_composite(new_img, image_right, offset = paste0("+", (image_info(image_left)$width + separation + border), "+", border))
  
  return(new_img)
}

# Example usage
image_left <- "./images_to_join/plot1a.png"
image_right <- "./images_to_join/plot1b.png"
result <- join_images(image_left, image_right, separation = 50, border = 20, background = 'white')
image_write(result, './joined_images/joined_image.png')
