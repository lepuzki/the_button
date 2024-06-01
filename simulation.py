import random
import time
import sys
import os
import keyboard
from collections import deque
from colorama import Fore
from utils import human_readable_format

def simulate_button_press(number_format='human'):
    points, total_tries, max_points = 0, 0, 0
    probability_of_loss, animation_index = 0.0, 0
    start_time = time.time()
    tries_queue = deque(maxlen=10)
    animation_frames = ["[ / ]", "[ - ]", "[ \\ ]", "[ | ]"]

    try:
        while True:
            if keyboard.is_pressed('q'):
                break

            for _ in range(1000):
                total_tries += 1
                points += 1
                probability_of_loss += 0.01

                if points > max_points:
                    max_points = points

                if random.random() < probability_of_loss:
                    points, probability_of_loss = 0, 0.0

            current_time = time.time()
            tries_queue.append((total_tries, current_time))
            
            if len(tries_queue) == 10:
                time_diff = tries_queue[-1][1] - tries_queue[0][1]
                if time_diff > 0:
                    tries_per_minute = ((tries_queue[-1][0] - tries_queue[0][0]) / time_diff) * 60
                else:
                    tries_per_minute = 0
            else:
                tries_per_minute = 0

            if current_time - start_time >= 1:
                animation_frame = animation_frames[animation_index]
                animation_index = (animation_index + 1) % len(animation_frames)
                total_tries_str = human_readable_format(total_tries) if number_format == 'human' else f"{total_tries:,}"
                max_points_str = f"{max_points:,}"
                tries_per_minute_str = human_readable_format(tries_per_minute) if number_format == 'human' else f"{tries_per_minute:,.2f}"

                clear_console()
                sys.stdout.write(f"{Fore.RED}Exit (Q)\n")
                sys.stdout.write(f"{Fore.YELLOW}Total tries:    {total_tries_str}\n")
                sys.stdout.write(f"{Fore.GREEN}Max points:     {max_points_str}\n")
                sys.stdout.write(f"{Fore.CYAN}Tries per minute: {tries_per_minute_str}\n")
                sys.stdout.write(f"{Fore.MAGENTA}{animation_frame}\n")
                sys.stdout.flush()
                start_time = current_time

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Simulation ended. {Fore.GREEN}Maximum points achieved: {max_points}")
        print(f"{Fore.YELLOW}Total tries: {total_tries}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
