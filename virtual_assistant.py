import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pygame
import keyboard

def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    window.fill(color = (255, 255, 255))
    
    while True:
        pygame.display.update()
        
        font_big = pygame.font.Font('freesansbold.ttf', 29)
        font_instructions = pygame.font.Font('freesansbold.ttf',12)
        font_normal = pygame.font.Font('freesansbold.ttf', 18)
        
        title = font_big.render('Voice Automated Virtual Assistant', True, (0,0,0))
        instructions = font_instructions.render("Instructions: Say, 'Open (option).'", True, (0,0,0))
        option1 = font_normal.render('Calculator', True, (0,0,0))
        option2 = font_normal.render('Clock', True, (0,0,0))
        option3 = font_normal.render('Weather', True, (0,0,0))
        option4 = font_normal.render('Internet', True, (0,0,0))
        quit = font_instructions.render("Say, 'Quit' to exit.", True, (0,0,0))
        
        window.blit(title, (5, 15))
        window.blit(instructions, (155, 50))
        window.blit(option1, (205, 100))
        window.blit(option2, (227, 135))
        window.blit(option3, (217, 170))
        window.blit(option4, (219, 205))
        window.blit(quit, (205, 450))
        
        pygame.display.update()
        
        input = input_method()
        
        if input.lower() == 'calculator':
            calculator(window, font_big, font_instructions, font_normal)
        elif input.lower() == 'clock':
            clock(window, font_big, font_instructions)
        elif input.lower() == 'weather':
            weather(window, font_big, font_instructions, font_normal)
        elif input.lower() == 'internet':
            internet(window, font_big, font_instructions)
        elif input.lower() == 'quit':
            pygame.quit()
        

def input_method():
    pygame.time.wait(1)
    
    mic = sr.Microphone()
    r = sr.Recognizer()

    input = ''
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
        
        pygame.time.wait(2500)
        
        if input == 'exit':
            main()
        
        while True:
            pygame.display.update()
            pygame.event.get()
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
              
                    if input.lower() == 'new equation':
                        new = True
                        break
                    elif input.lower() == 'exit':
                        main()
                    
            except: 
                new = True
                
            if new:
                break


def clock(window, font_big, font_instructions):
    pygame.init()
    window.fill(color=(255,255,255))
    
    while True:
        pygame.display.update()
        
        title = font_big.render("Clock", True, (0,0,0))
        instructions_one = font_instructions.render("To activate timer say, 'timer'.", True, (0,0,0))
        instructions_two = font_instructions.render("To activate stopwatch say, 'stopwatch'", True, (0,0,0))
        quit = font_instructions.render("Say, 'Exit' to exit.", True, (0,0,0))
        
        window.blit(title, (205, 15))
        window.blit(instructions_one, (165,50))
        window.blit(instructions_two, (138,65))
        window.blit(quit, (205, 450))
        
        pygame.display.update()
        
        input = input_method()
        
        while True:
            pygame.event.get()
            
            if input.lower() == 'timer':
                
                timer_instructions = font_instructions.render("To set a time say, '(number) hours, (number) minutes, and (number) seconds.'", True, (0,0,0))
                window.blit(timer_instructions, (30, 100))
                pygame.display.update()
                
                pygame.time.wait(3000)
                input = input_method()
                
                numbers = [int(x) for x in input.split() if x.isnumeric()]
                
                if (numbers[0] < 100) and (numbers[1] < 60) and (numbers[2] < 60):
                    hours, minutes, seconds = numbers[0], numbers[1], numbers[2]

                    while hours > -1:
                        while minutes > -1:
                            while seconds > -1:
                                window.fill(color=(255,255,255))
                                quit = font_instructions.render('Press the spacebar to exit.', True, (0,0,0))
                                quit_rect = quit.get_rect(center=(250,450))
                                window.blit(quit, quit_rect)
                                
                                if (minutes < 10) and (seconds > 10):
                                    time = font_big.render((str(hours) + ':0' + str(minutes) + ":" + str(seconds)), True, (0,0,0))
                                    time_rect = time.get_rect(center=(250,190))
                                    window.blit(time, time_rect)
                                elif (minutes > 10) and (seconds < 10):
                                    time = font_big.render((str(hours) + ':' + str(minutes) + ':0' + str(seconds)), True, (0,0,0))
                                    time_rect = time.get_rect(center=(250,190))
                                    window.blit(time, time_rect)
                                elif (minutes < 10) and (seconds < 10):
                                    time = font_big.render((str(hours) + ':0' + str(minutes) + ':0' + str(seconds)), True, (0,0,0))
                                    time_rect = time.get_rect(center=(250,190))
                                    window.blit(time, time_rect)
                                else:
                                    time = font_big.render((str(hours) + ':' + str(minutes) + ":" + str(seconds)), True, (0,0,0))
                                    time_rect = time.get_rect(center=(250,190))
                                    window.blit(time, time_rect)
                                    
                                if keyboard.is_pressed(' '):
                                    main()
                                    
                                pygame.display.update()
                                pygame.event.get()
                                pygame.time.wait(1000)
                                
                                seconds -= 1
                                
                            minutes -= 1
                            seconds = 59
                            
                        hours -= 1
                        minutes = 59
                        
                main()
                
            if input.lower() == 'stopwatch':
                
                stopwatch_instructions = font_instructions.render("To start the stopwatch say, 'start'.", True, (0,0,0))
                window.blit(stopwatch_instructions, (155, 100))
                pygame.display.update()
                
                pygame.time.wait(3000)
                input = input_method()
                
                seconds, minutes, hours = 0,0,0
                while True:
                    
                    window.fill(color=(255,255,255))
                    quit = font_instructions.render('Press the spacebar to exit.', True, (0,0,0))
                    quit_rect = quit.get_rect(center=(250,450))
                    window.blit(quit, quit_rect)

                    if seconds == 60:
                        minutes +=1
                        seconds = 0
                    if minutes == 60:
                        hours += 1
                        minutes = 0
                    
                    if (minutes < 10) and (seconds > 10):
                        time = font_big.render((str(hours) + ':0' + str(minutes) + ":" + str(seconds)), True, (0,0,0))
                        time_rect = time.get_rect(center=(250,190))
                        window.blit(time,time_rect)
                    elif (minutes > 10) and (seconds < 10):
                        time = font_big.render((str(hours) + ':' + str(minutes) + ':0' + str(seconds)), True, (0,0,0))
                        time_rect = time.get_rect(center=(250,190))
                        window.blit(time,time_rect)
                    elif (minutes < 10) and (seconds < 10):
                        time = font_big.render((str(hours) + ':0' + str(minutes) + ':0' + str(seconds)), True, (0,0,0))
                        time_rect = time.get_rect(center=(250,190))
                        window.blit(time,time_rect)
                    else:
                        time = font_big.render((str(hours) + ':' + str(minutes) + ":" + str(seconds)), True, (0,0,0))
                        time_rect = time.get_rect(center=(250,190))
                        window.blit(time,time_rect)
                        
                    if keyboard.is_pressed(' '):
                        pygame.time.wait(3000)
                        main()
                        
                    pygame.display.update()    
                    pygame.event.get()
                    pygame.time.wait(1000)
                    seconds += 1


def weather(window, font_big, font_instructions, font_normal):
    
    pygame.init()
    window.fill(color = (255, 255, 255))
    
    while True:
        pygame.display.update()
        
        title =  font_big.render('Weather', True, (0,0,0))
        instructions = font_instructions.render("Say, '(City)' to search weather in a city. This may take up to 2 minutes.", True, (0,0,0))
        quit = font_instructions.render("Say, 'Exit' to exit.", True, (0,0,0))
        
        window.blit(title, (185, 15))
        window.blit(instructions, (50, 50))
        window.blit(quit, (205, 450))
        
        pygame.display.update()
        
        pygame.time.wait(3000)
        
        input = input_method()
        new = False
        
        while True:
            
            op = webdriver.ChromeOptions()
            op.add_argument('--headless')
            driver = webdriver.Chrome(options=op)
            
            driver.get("https://weather.com")
            time.sleep(3)
            pygame.event.get()
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/form/div/div[1]/fieldset/input").send_keys(input)
            time.sleep(3)
            pygame.event.get()
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/form/div/div[2]/div[2]/button[1]").click()
            time.sleep(3)
            pygame.event.get()
            
            temp = font_normal.render((driver.find_element(By.XPATH, "//*[@id='WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a']/div/section/div/div/div[2]/div[1]/div[1]/span").text + 'F'), True, (0,0,0))
            pygame.event.get()
            condition = font_instructions.render(driver.find_element(By.XPATH, "//*[@id='WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a']/div/section/div/div/div[2]/div[1]/div[1]/div[1]").text, True, (0,0,0))
            pygame.event.get()
            wind = font_normal.render(("Wind: " + driver.find_element(By.XPATH, "//*[@id='todayDetails']/section/div/div[2]/div[2]/div[2]/span").text), True, (0,0,0))
            pygame.event.get()
            humidity = font_normal.render(("Humidity: " + driver.find_element(By.XPATH, "//*[@id='todayDetails']/section/div/div[2]/div[3]/div[2]/span").text), True, (0,0,0))
            pygame.event.get()
            city_name = font_normal.render(input, True, (0,0,0))
            
            temp_rect = temp.get_rect(center=(250,190))
            condition_rect = condition.get_rect(center=(250,205))
            wind_rect = wind.get_rect(center=(167,250))
            humidity_rect = humidity.get_rect(center=(334,250))
            city_name_rect = city_name.get_rect(center=(250,130))
            
            window.blit(temp, temp_rect)
            window.blit(condition, condition_rect)
            window.blit(wind, wind_rect)
            window.blit(humidity, humidity_rect)
            window.blit(city_name, city_name_rect)
                
            while True:
                pygame.display.update()
                pygame.event.get()
                
                new_city = font_instructions.render("To continue say, 'New City' then give the name of a city.", True, (0,0,0))
                new_city_rect = new_city.get_rect(center=(250, 315))
                window.blit(new_city, new_city_rect)
                
                input = input_method()
            
                if input.lower() == 'new city':
                    new = True
                    window.fill(color=(255,255,255))
                    break
                elif input.lower() == 'exit':
                    main()
                    new = True
                
            if new:
                break


def internet(window, font_big, font_instructions):
    pygame.init()
    window.fill(color=(255,255,255))
    
    while True:
        pygame.display.update()
        
        title = font_big.render('Internet Search', True, (0,0,0))
        instructions = font_instructions.render("To search for a website say, 'Name of website',", True, (0,0,0))
        instructions_two = font_instructions.render("followed by either '.com', '.org', or '.net' etc.", True, (0,0,0))
        
        window.blit(title, (140, 15))
        window.blit(instructions, (115,50))
        window.blit(instructions_two, (130,62))
        
        pygame.display.update()
        
        pygame.time.wait(5000)
        
        input = input_method()
        
        input = input.replace('-', ' ')
        
        if 'com' in input.split():
            input = 'https://' + (input.replace('dot', '.')).replace(' ', '')
        elif 'dotnet' in input:
            input = 'https://' + (input.replace('dotnet', '.net')).replace(' ', '')
        else:
            input = 'https://' + (input.replace('dot', '.')).replace(' ', '')
        
        new = False
        
        while True:
            pygame.display.update()
            
            try:
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)
                page = webdriver.Chrome(options=options, chrome_options=options)
                
                page.get(input)

                new = True
                
            except:
                new = True
            
            if new:
                pygame.quit()
                
            break

if __name__ == "__main__":
    main()