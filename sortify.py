import pygame
import random
import time
import numpy as np
from typing import List, Tuple

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BAR_WIDTH = 30
SPACING = 2
MAX_BAR_HEIGHT = 600
BACKGROUND_COLOR = (10, 10, 30)  # Dark space blue
BAR_COLOR = (100, 200, 255)  # Light blue
COMPARISON_COLOR = (255, 165, 0)  # Orange
SORTED_COLOR = (0, 255, 0)  # Green
TEXT_COLOR = (255, 255, 255)  # White

class Sortify:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sortify - Space Sorting Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Initialize array
        self.array = []
        self.array_size = 20
        self.generate_new_array()
        
        # Algorithm stats
        self.comparisons = 0
        self.swaps = 0
        self.start_time = 0
        self.current_algorithm = "Bubble Sort"
        self.sorting = False
        self.paused = False
        
        # Button properties
        self.buttons = {
            "Generate": pygame.Rect(50, 700, 150, 40),
            "Bubble Sort": pygame.Rect(250, 700, 150, 40),
            "Merge Sort": pygame.Rect(450, 700, 150, 40),
            "Quick Sort": pygame.Rect(650, 700, 150, 40),
            "Pause": pygame.Rect(850, 700, 150, 40)
        }

    def generate_new_array(self):
        self.array = [random.randint(10, MAX_BAR_HEIGHT) for _ in range(self.array_size)]
        self.comparisons = 0
        self.swaps = 0
        self.sorting = False

    def draw_array(self, comparing_indices: List[int] = None, sorted_indices: List[int] = None):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw stars in background
        for _ in range(50):
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT - 100)
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        # Draw bars
        for i, height in enumerate(self.array):
            x = 50 + i * (BAR_WIDTH + SPACING)
            y = WINDOW_HEIGHT - 100 - height
            
            if comparing_indices and i in comparing_indices:
                color = COMPARISON_COLOR
            elif sorted_indices and i in sorted_indices:
                color = SORTED_COLOR
            else:
                color = BAR_COLOR
                
            pygame.draw.rect(self.screen, color, (x, y, BAR_WIDTH, height))

        # Draw buttons
        for text, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 100), rect)
            text_surface = self.font.render(text, True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

        # Draw stats
        stats = [
            f"Algorithm: {self.current_algorithm}",
            f"Comparisons: {self.comparisons}",
            f"Swaps: {self.swaps}",
            f"Time: {time.time() - self.start_time:.2f}s" if self.sorting else "Time: 0.00s"
        ]
        
        for i, stat in enumerate(stats):
            text = self.small_font.render(stat, True, TEXT_COLOR)
            self.screen.blit(text, (50, 50 + i * 30))

        pygame.display.flip()

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if self.array[j] > self.array[j + 1]:
                    self.swaps += 1
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array([j, j + 1], list(range(n - i, n)))
                    yield
                if self.paused:
                    while self.paused:
                        yield

    def merge_sort(self, arr=None, start_idx=0):
        if arr is None:
            arr = self.array.copy()
            self.start_time = time.time()
            
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid], start_idx)
        right = self.merge_sort(arr[mid:], start_idx + mid)

        return self.merge(left, right, start_idx)

    def merge(self, left, right, start_idx):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                self.swaps += 1
            
            # Update visualization
            temp_array = self.array.copy()
            temp_array[start_idx:start_idx + len(result)] = result
            self.array = temp_array
            self.draw_array([start_idx + i, start_idx + j])
            yield
            
            if self.paused:
                while self.paused:
                    yield

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self, low=None, high=None):
        if low is None:
            low = 0
            high = len(self.array) - 1
            self.start_time = time.time()

        if low < high:
            pivot_idx = yield from self.partition(low, high)
            yield from self.quick_sort(low, pivot_idx - 1)
            yield from self.quick_sort(pivot_idx + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            self.comparisons += 1
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.swaps += 1
                self.draw_array([i, j, high])
                yield
                if self.paused:
                    while self.paused:
                        yield

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.swaps += 1
        self.draw_array([i + 1, high])
        yield
        return i + 1

    def run(self):
        sorting_generator = None
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    for text, rect in self.buttons.items():
                        if rect.collidepoint(mouse_pos):
                            if text == "Generate":
                                self.generate_new_array()
                                self.sorting = False
                            elif text == "Bubble Sort":
                                self.current_algorithm = "Bubble Sort"
                                self.sorting = True
                                self.start_time = time.time()
                                sorting_generator = self.bubble_sort()
                            elif text == "Merge Sort":
                                self.current_algorithm = "Merge Sort"
                                self.sorting = True
                                self.start_time = time.time()
                                sorting_generator = self.merge_sort()
                            elif text == "Quick Sort":
                                self.current_algorithm = "Quick Sort"
                                self.sorting = True
                                self.start_time = time.time()
                                sorting_generator = self.quick_sort()
                            elif text == "Pause":
                                self.paused = not self.paused
                                self.buttons["Pause"] = pygame.Rect(850, 700, 150, 40)
                                self.buttons["Pause"] = pygame.Rect(850, 700, 150, 40)

            if self.sorting and sorting_generator:
                try:
                    next(sorting_generator)
                except StopIteration:
                    self.sorting = False
                    self.draw_array(sorted_indices=list(range(len(self.array))))

            if not self.sorting:
                self.draw_array()

            self.clock.tick(60)

if __name__ == "__main__":
    app = Sortify()
    app.run() 