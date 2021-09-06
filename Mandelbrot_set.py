import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mandelbrot set")


def fractal():
    for y in range(400):  # image size
        for x in range(400):  # image size
            zx, zy = cx, cy = -2 + 2.5 * x / 400.0, -1.25 + 2.5 * y / 400.0  # image scaling
            for i in range(25):  # iterations
                zx, zy = zx * zx - zy * zy + cx, 2 * zx * zy + cy
                if zx * zx + zy * zy > 4:  # magnitude check
                    break
                screen.set_at((x, y), ((250 - 25 * i) * 0x10101))  # pixel draw (hex color)
                pygame.display.update()  # showing pixel by pixel


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))

        fractal()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
