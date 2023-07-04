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
        
        pygame.display.update()
        
        input = input_method()
        
        if input == 'calculator':
            calculator(window, font_big, font_instructions, font_normal)
        elif input == 'quit':
            pygame.quit()
            break
        

def input_method():
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
    
    return input
    

def calculator(window, font_big, font_instructions, font_normal):
    pygame.init()
    window = pygame.display.set_mode((500,500))
    window.fill(color = (255, 255, 255))
    
    while True:
        
        pygame.display.update()
        
        title = font_big.render('Calculator', True, (0,0,0))
        instructions = font_instructions.render('Instrucitons: Give equation', True, (0,0,0))
        quit = font_instructions.render("Say, 'Exit' to exit.", True, (0,0,0))
        
        window.blit(title, (170, 15))
        window.blit(instructions, (173,50))
        window.blit(quit, (205, 450))
        
        input = input_method()
        new = False
        
        while True:
            pygame.display.update()
            try:
                pygame.display.update()
                answer = font_normal.render(str(eval(input)), True, (0,0,0))
                new_equation = font_instructions.render("Say, 'new equation' to start over.", True, (0,0,0))
                
                center_equation = answer.get_rect(center=(250, 250))
                center_new = new_equation.get_rect(center=(250, 280))
                
                window.blit(answer, center_equation)
                window.blit(new_equation, center_new)
                
                while True:
                    pygame.display.update()
                    input = input_method()
              
                    if input == 'new equation':
                        new = True
                        break
                    elif input == 'exit':
                        pygame.quit()
                        new = True
                        break
                    
            except:
                if input == 'exit':
                    pygame.quit()
                    break
                new = True
                
            if new == True:
                break


def clock():
    pass


def weather():
    pass


def internet():
    pass


main()