import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
cell_size = 20

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the snake
snake = [(screen_width // 2, screen_height // 2)]
direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
new_segment = False

# Set up the food
food_x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
food_y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size

# Main function
def main():
    global snake, direction, new_segment, food_x, food_y

    clock = pygame.time.Clock()

    rounds = 3
    current_round = 0
    scores = []

    game_over_font = pygame.font.Font(None, 36)
    score_font = pygame.font.Font(None, 24)

    while current_round < rounds:
        current_round += 1
        score = 0

        snake = [(screen_width // 2, screen_height // 2)]
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        new_segment = False

        food_x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
        food_y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size

        while True:
            screen.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"

            # Move the snake
            head_x, head_y = snake[0]
            if direction == "UP":
                head_y -= cell_size
            elif direction == "DOWN":
                head_y += cell_size
            elif direction == "LEFT":
                head_x -= cell_size
            elif direction == "RIGHT":
                head_x += cell_size

            # Check if snake hits the boundary
            if (head_x < 0 or head_x >= screen_width or
                head_y < 0 or head_y >= screen_height):
                break

            # Check if snake eats the food
            if head_x == food_x and head_y == food_y:
                score += 1
                new_segment = True
                food_x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
                food_y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size

            snake.insert(0, (head_x, head_y))
            if not new_segment:
                snake.pop()
            else:
                new_segment = False

            # Draw the snake
            for segment in snake:
                pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))

            # Draw the food
            pygame.draw.rect(screen, red, (food_x, food_y, cell_size, cell_size))

            # Display score
            score_text = score_font.render("Round {}: Score: {}".format(current_round, score), True, white)
            screen.blit(score_text, (10, 10))

            pygame.display.update()
            clock.tick(8)

        scores.append(score)

    # Display final scores
    screen.fill(black)
    final_scores_text = "Final Scores:\n"
    for i, score in enumerate(scores):
        final_scores_text += "Round {}: {}\n".format(i+1, score)
    final_scores_surface = game_over_font.render(final_scores_text, True, white)
    screen.blit(final_scores_surface, (screen_width // 2 - final_scores_surface.get_width() // 2, screen_height // 2 - final_scores_surface.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)  # Delay for 3 seconds before quitting
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
