import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading
import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    window.fill(color = (255, 255, 255))
    pygame.display.flip()
    
    while True:
        pygame.display.update()
        
        font_big = pygame.font.Font('freesansbold.ttf', 30)
        font_instructions = pygame.font.Font('freesansbold.ttf',12)
        font_normal = pygame.font.Font('freesansbold.ttf', 18)
        title = font_big.render('Jarvis v1.0', True, (0,0,0))
        instructions = font_instructions.render("Instructions: Say, 'Open (option).'", True, (0,0,0))
        option1 = font_normal.render('Calculator', True, (0,0,0))
        option2 = font_normal.render('Clock', True, (0,0,0))
        option3 = font_normal.render('Weather', True, (0,0,0))
        option4 = font_normal.render('Internet', True, (0,0,0))
        quit = font_instructions.render("Say, 'Quit' to exit.", True, (0,0,0))
        window.blit(title, (167, 15))
        window.blit(instructions, (155, 50))
        window.blit(option1, (205, 100))
        window.blit(option2, (227, 135))
        window.blit(option3, (217, 170))
        window.blit(option4, (219, 205))
        window.blit(quit, (205, 450))
        
        pygame.time.wait(1)
        
        mic = sr.Microphone()
        r = sr.Recognizer()

        input = None
        with mic as source:
            try:
                pygame.event.get()
                audio = r.record(source, duration=3)
                input = r.recognize_google(audio)
            except:
                pass
        
        if input == 'quit':
            pygame.quit()
            break
    

def calculator():
    pass


def clock():
    pass


def weather():
    pass


def internet():
    pass


main()