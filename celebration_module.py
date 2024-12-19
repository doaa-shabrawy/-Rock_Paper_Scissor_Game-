import pygame
import sys

def celebration_with_image(image_path):
    # Initialize Pygame
    pygame.init()

    # Load the image and sound
    try:
        # Set up the display
        screen = pygame.display.set_mode((800, 600))  # Window size
        pygame.display.set_caption("Celebration!")
        
        # Load and scale the image
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (800, 600))

        # Set up fonts
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        # Text to display
        text1 = "Congratulations!"
        text2 = "You are the winner!"
        
        # Display the celebration until the user closes the window
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the image
            screen.blit(image, (0, 0))

            # Render the text
            text_surface1 = font.render(text1, True, (255, 255, 0))  # Yellow text
            text_surface2 = small_font.render(text2, True, (0, 255, 255))  # Cyan text
            
            # Position the text
            screen.blit(text_surface1, (200, 50))  # Adjust coordinates as needed
            screen.blit(text_surface2, (230, 150))

            # Update the display
            pygame.display.flip()

        pygame.quit()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()

# Replace with the paths to your image and sound files
#celebration_with_image("computer.webp")
