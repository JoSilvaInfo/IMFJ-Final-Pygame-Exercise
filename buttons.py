import pygame

# Button class
class Button():
	def __init__(self, x, y, image, scale):
		# Get the original width and height of the image
		width = image.get_width()
		height = image.get_height()

		# Scale the image based on the provided scale factor
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		
		# Create a rectangle that encloses the button image
		self.rect = self.image.get_rect()
		# Set the top-left position of the button
		self.rect.topleft = (x, y)
		# Flag to keep track of button click state
		self.clicked = False

	def draw(self, surface):
		# Flag to indicate if the button was clicked
		action = False 
		# Get the current mouse position
		pos = pygame.mouse.get_pos()

		# Check if the mouse is hovering over the button and if the left mouse button is pressed
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				# Set the button click state to True
				self.clicked = True 
				# Set the action flag to indicate a button click
				action = True
		# Check if the left mouse button is released
		if pygame.mouse.get_pressed()[0] == 0:
			# Reset the button click state to False
			self.clicked = False

		# Draws the button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		# Return the action flag indicating if the button was clicked
		return action