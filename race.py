import pygame, simpleGE, time
""" time trial race"""
score = 1
checkp1 = False
checkp2 = False
checkp3 = False
checkp4 = False


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("track copy.xcf")
        
        self.car = Car(self)
        self.timer = simpleGE.Timer()
        
        
        
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        self.bwTrack = simpleGE.Sprite(self)
        self.bwTrack.setImage("trackbw copy.xcf")
        self.bwTrack.position = (320, 240)
        self.bwTrack.hide()
        self.sprites = [self.bwTrack,
                        self.car,
                        self.lblScore,
                        self.lblTime]
        self.setCaption("B for black and white, C for color")
        
    def process(self):
        global score, checkp1, checkp2, checkp3, checkp4
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()
        if(checkp1 and checkp2 and checkp3 and checkp4):
            checkp1 = False
            checkp2 = False
            checkp3 = False
            checkp4 = False
            score += 1
            print (score)
        

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print("B and W")
                self.bwTrack.show()
                
            if event.key == pygame.K_c:
                print("Color")
                self.bwTrack.hide()
    
        
class Car(simpleGE.Sprite,):
    def __init__(self, scene):
        super().__init__(scene)
        #self.colorRect("red", (50, 25))
        self.setImage ("pixil-frame-0 2.png")
        self.setSize(70,70)
        self.moveSpeed = 5
        self.colMap = pygame.image.load("trackBW.png")
        
        
    def process(self):
        global score, checkp1, checkp2, checkp3, checkp4
        if self.isKeyPressed(pygame.K_LEFT):
            self.turnBy(5)
        if self.isKeyPressed(pygame.K_RIGHT):
            self.turnBy(-5)
        if self.isKeyPressed(pygame.K_UP):
            self.forward(self.moveSpeed)
        if self.isKeyPressed(pygame.K_DOWN):
            self.forward(-3)
        colorUnder = self.colMap.get_at((int(self.position[0]),
                                        int(self.position[1])))
        
                
        if colorUnder == (255, 255, 255):
            self.moveSpeed = 1
        else:
            self.moveSpeed = 5
  
        
            
        if self.position[0] > 60 and self.position[0] < 130 and self.position[1] > 208 and self.position[1] < 214:
            checkp1 = True
            print("c1")
        if self.position[0] > 355 and self.position[0] < 365 and self.position[1] > 90 and self.position[1] < 160:
            checkp2 = True
            print("c2")
        if self.position[0] > 380 and self.position[0] < 385 and self.position[1] > 360 and self.position[1] < 440:
            checkp3 = True
            print("c3")
        if self.position[0] > 530 and self.position[0] < 650 and self.position[1] > 235 and self.position[1] < 240:
            checkp4 = True
            print("c4")
            
            
        if(checkp1 and checkp2 and checkp3 and checkp4):
            checkp1 = False
            checkp2 = False
            checkp3 = False
            checkp4 = False
            score += 1
            print (score)
            
        #print(f"{self.position[0]} , {self.position[1]}")
        
class LblScore(simpleGE.Label):
    global score
    def __init__(self):
        self.text = (f"laps: {score}")
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = (f"Time: 10 ")
        self.center = (500, 30)
   
class Instructions (simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("track copy.xcf")

        self.response = "play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "you are a racer",
        "who is trying to qualify for the piston cup.",
        "drive with the right left and",
        "up and down arrow keys",
        "and try to finish with the best time",
        "",
        "Gods speed!"]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)

        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            global start_time
            self.response = "Play"
            start_time = time.time()
            self.stop()
        

            

def main():
    keepGoing = True
    global score
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
                
        if instructions.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
#     game = Game()
#     game.start()
    
if __name__ == "__main__":
    main()