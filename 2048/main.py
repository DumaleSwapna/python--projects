import pygame
import random
import math 

pygame.init()
# this will initialise all the different features that we need

#now find/define all the different constants 

FPS = 60   # frames per sec

# FPS allows use to dictate how quickly the game is quikly the game is running and regulating the speed on different devices

WIDTH, HEIGHT = 600, 600  # because we need a squre u can also make changes for complex projects
ROWS = 4
COLS = 4

# now determine how long a tile is going to be or one of the rectangle is going to be inside our grid,so that we do that

RECT_HEIGHT = HEIGHT // ROWS     # 800/4 = 200.so each tile have 200 pixels
# similar do for coloums
RECT_WIDTH = WIDTH // COLS

# the reason we are doing integer division  is so that we get an integer rather than a floating point value

# Now colours are going to identify,we are goning to define what we need right now

OUTLINE_COLOR = (187,173,160)
# THIS COLOR GOING TO BE be equal to the color of nice grey,now we have already founf this RGB colors so that we copy them

# IMP : when ever we are definign the colour in pygame ,you have an option to use RGB which stands for red,green,blue --> this values can be range from 0-255 ---> (0,0,0) = black and (255,255,255) = white

# now we do outline_thickness

OUTLINE_THICKNESS = 10    # we can adjucst its value also

# now background colour to be grey

BACKGROUND_COLOR = (205,192,180)    #grey

# don't worry about the colours you can adjust them 

FONT_COLOUR = (119,110,101)   # blackish greyish shade

# so now we have created some constrains which help us eto create a pygame window
# so when ever we are coding in pygame ,we have a window,the window --> where we can draw objects and its really representing the canvas of our screen

# creating PYGAME WINDOW
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# title of the window
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans ", 60 , bold=True) # font = (font name, size, bold beacuse we wnat bold version of the function)

#variable defining which we use it later

MOV_VEL = 20  # moving velocity this is the speed at which the tiles will move and I'm gng with 20 pixels per second

# GAME LOOP
# So the first step is to working with the pygame is we create something known as main loop
# Now the main loop is the event loop that gng to run  constantly and check for things like BUTTONS, PRESSES, EXITING THE SCREEN.its essentially what will run the game okay, its the main loop that handling all the different events

#       so usually we put that inside of a function so we will simply say define main function




# define functions



# draw_grid function

def draw_grid(window):

    #rows
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    #cols
    for col in range(1,COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
    

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

# draw function


def draw(window):
    window.fill(BACKGROUND_COLOR)

    draw_grid(window)

    pygame.display.update()


 # main function
def main(window):   # we are taking window as an parameter
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window)
    
    pygame.quit()

# callthis function
# this define where we wana run this game --> on the window
if __name__ == "__main__":  # this define-->we are runing only this fun if we run ths file directly
    main(WINDOW)

# the code inside the if block is only executed when the script is run directly
# Inside the if __name__ == "__main__": block, it calls the main function and passes a variable WINDOW as an argument. 
# inside the  main we have to create a loop that't going to continue to run
# inside a main we have to create a loop that going to run
# the first thing we are going to do is set up a clock object this will allow us to regulate the speed of the loop,so as we going to pygame.time.clock.
# then we are going to have a variable called run = true --> which will set to false when we want to exit the loop
# then we will say clock.tick --> we go to tick based on the frames per second which is FPS which we have already declared
# now this tick will make it so this wall loop is only going to run at most one time every 60 sec.it could run less than that but the reason we put this here is so that people that are running on different of computers don't have the game running at the different spped.
# if you don't have this clock here what will happen is you'll simply run the loop at what ever the fastest speed is you can run it at which means someone on a really powerful computer is going to see the game a lot faste than someone on a slow computer.so always good idea to have this clock
# now we have  a clock what we gona do means is to create a simple event loop that's just going to listen for all of the different key presses
# in for loop the events that could occur so to do that we're going to say for event 
# "for event in pygame.event.get():" --> this will loop through all of the events that have occured and
# we can then check the event and handle it so we're going to say  "if event.type == pygame.QUIT:" -->"run = False"--> we'll break out of this loop now
# now what that's going to do is simply say okay if we press the exit button that's what this quit event is we are going to set run equal to false.so this loop will stop running we are going to break immediately out of this event loop so we don't handle it and then what will happen is we'll come outside of the loop and we will run the command "pygame.quit()" --> which will simply quit the pygame window for us so that is now main loop and what should happen is if we run this code we should acually see a window appearing and 
# if we press the x button we should be able to cleanly exit so let's go ahead and try that and you can see we get 2048 we get the window of our size 800800 and I can click exit and I cleanly exit the code all right so now that we have that let's move on to doing some drawing operations so that we can acually see some stuff up here appearing on the screen now I typically like to seperate the drawing from the event handling

# DRAWING
# lets do some drawing operations so that we can do some stuffs appearing on the screen
# now i typically like to seperate the drawing from the event so that it's a little bit clear/cleaner so the way I'll do that is define a function here called draw -->"def draw():" --> you will notice that in my code I'll write a lot of functions just to make sure everything is clean readable and easy to debug and we can quickly figure out where somethings going wrong by just isolating it to a specific fuction. this is good practice and something you can kind of take note of while I'm coding
# in the draw function I'm going to take a window-->"def draw(window):"
# what i'll do for now is simply set the background colour and update the screen
# "window.fill()" --> this allow you to fill the window completely with a background code.so we are writing
# "window.fill(BACKGROUND_COLOR)" --> so we're essencially just kind painting the entire window this color(initially declared).now we do
# "pygame.display.update()"--> now the way pygame works is we do all of these drawing or paint events and then as soon as an update is called we'll acually apply all of those on onto the sreceen int he order in which we wrote them.so what that means is that we're always going to fill screen first --> because what that will typically do is it will actually overide what ever was on the screen by before sorry by painting over top of it then we'll do any other operations to draw the updated screen and then we'll update and then when we do the updat. we'll acually see that being performed on the screen I know it's a little bit abstract right now,but it's just like we do all of there paint operations then we update then they're all applied at once rather than happening one at a time.
# so now we just need to call that function so inside of this loop
# while run:
#       clock.tick(FPS)

 #       for event in pygame.event.get():
 #             if event.type == pygame.QUIT:
#                run = False
#               break
#         draw(window)
# make sure you're inside of the whilel loop here at he bottom we are going to say draw and we are going to pass that window object.now we should be getting the background color on our screen 
# now you can see colour on your screen with the background color

# we have done that we want to start drawing the grid so to draw the grid we're going to write a different function and just say --> "def draw_grid(window):" --> inside of here we will take the window object again 
# okay so for drawing the grid what we will need to do is we will need to draw horizontal and vertical lines to represent the seperation between tiles and we want to draw kind of a border around the entire screen so that we get that nice border effect so let's begin with the border.
# to draw the border we can simply draw a rectangle that's positioned at the edge of the screen
# so to draw a rectangle pygame --> "pygame.draw.rect(window,OUTLINE_COLOR,())" --> for that we need to pass where we want to draw it.so we want to draw it on the window,we need to pass the colour so we like to draw it you can see auto complete.so we want the outline colour and then we need to pass a rectangle that represents where we should draw the rectangle. so the way we pass the rectangle is we give the x coordinate,y coordinate and width,height of the rectangle
# now the x and y represents the top lefthand corner where we want to start drawing the rectangle from now this will get into the pygame coordinate system which we will discuss in a second. but let's go
#"pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT))" --> now as well as that we have the optin to either have the rectangle be filled completely in or to be an outline. so in our case we want it to just be an outline.we don't want it to fill in entirely we don't want to draw a solid rectangle.we want one that's hollow so what we'll do is pass what's known as thew width or the thickness. so I'm going to say width and then this is going to be the outline thickness which in our case I belive is 10 pixels
# now lets draw it--> draw the background we are going to say draw grid -->"draw_grid(window)"--> we are going to pass the window and run it and you see a outline background color
# imp : one thing when we are talking about coordinates and x,y values in pygame we always start with 0,0 ehich is the top left corner of the screen.so rather than starting at the middle which is typically 0,0 it's the top left meaning as you go to the right your x value increases and as you go down your y value increses so if we look at the bottom right hand corner that would be 800,800 in terms of the coorrdinate grid in pygame so just keep that in mind.you will see as we go through here how we kind of do the positioning.okay so we have drawn that now we actually want to draw the grid line
# so start by drawing in draw_grid function--> we start drawing the horizontal lines so we can say -->
#  "for row in range(ROWS):" --> we are going to draw a line for every single row that we have and what we need to do here is simply calculate the y coordinate of the row of the line that want to draw so we are going to say
#  "y = row * RECT_HEIGHT" --> now the way this work is we will start with row being eaqual to zero and then it'll become 123 and then it will not be equal to what ever the last row is which is fine and in fact we can actually do one comma rows because we don't need to draw the very top line because that will already have been drawn by the rectangular outline that we drew
# anyways what we are going to do here is draw a line the line will go from the x coordinate 0 to the width of the screen and then what we will do is adjust the y  - coordinate so we are moving the line down every time the loop happens so we take whatever the height of one tilw is and we multiply that by the current row and that tells us the y - coordinate for this line so we are going to say
# "pygame.draw.line(window, OUTLINE_COLOR, (0, y),(WIDTH, y), OUTLINE_THICKNESS)" --> we pass window,outline color,0,y where y is our dynamic value and when we draw a line we pass  the starting position and the ending position so tje two points essentially for the line to be drawn between so we can say (width,y)--> so we are constantly always going to have the line starting at 0 =x and width=x.so that way we are filling the entire screen horizontally and we are just adjusting the y-coordinate so vertically swhere that line is going to be drawn again we need to specidy the the outline_thickness here also known as thw width of that line so now if we actually go here and and refresh u see rows in window
# similarly copy the code and make cols in window by making some changes like row = col and x = y etc. here where we make that changes is with call and the rectangular width versus row and the rectangular height,where rect heidht and rect width are same. however they could be different which is why I'm doing this in two loops because we wanted to have actual rectangles not squares then this code would adjust to that appropriately
# now run you will get the grid
# so now we have 4*4 grid what we want to start doing is actually representing tiles in those grids and then drawing thr tiles on the screen once we are able to draw the tiles on the screen then we can start moving them on the screen again as i said this a bit more complicated