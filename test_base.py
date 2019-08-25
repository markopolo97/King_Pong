# CECS 490 Project King Pong

# Syntax for Main loop

# Make 2D for set of cups(10x4)

# While(done != true)

#  Run Sensor and Camera Functions
#  Returns Index Value for which Cup(X) and PWM Value(Y)
#  PWM is entered by user input 
#  Run Stepper Motor Code to Move Base to Index(X value)
#  Run DC Fan Code that will start the fan with Y value
#  Use timer to have a delay
#  Run Loading Code to load ball into pipe with fan on at desired
#  PWM
#  Use timer for delay in making sure ball is in cup and cup is taken out
#  Set index = 4(intial)
#  Run Stepper Motor Function to reset index 
#  Set done = TRUE

# End of While Loop

# Set done = FALSE outside of while loop in main()
# To continue loop
# GPIO for Stepper Motor
import RPi.GPIO as GPIO
# Setup for DC Fan
import wiringpi 
import time

# Setup PWM for DC Fan
wiringpi.pwmSetMode(0) # PWM_MODE_MS = 0

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, 2)  # PWM output ONLY works on GPIO port 18

wiringpi.pwmSetClock(6)  # this parameters correspond to 25 KHz
wiringpi.pwmSetRange(128)


# Setup for Stepper Motor
GPIO.setmode(GPIO.BOARD) #this cmd is for user to specify pin as number of the board.
control_pins = [7,11,13,15] 

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfstep_forward = [
   [1,0,0,0],
   [1,1,0,0],
   [0,1,0,0],
   [0,1,1,0],
   [0,0,1,0],
   [0,0,1,1],
   [0,0,0,1],
   [1,0,0,1]
]

halfstep_reverse = [
   [1,0,0,1],
   [0,0,0,1],
   [0,0,1,1],
   [0,0,1,0],
   [0,1,1,0],
   [0,1,0,0],
   [1,1,0,0],
   [1,0,0,0]
]

#_-__-_________--___--_--_ultra sonic sensor code _______-_----__--___-__-
#Specify by pin number not by GPIO number
TRIG = 16
ECHO = 18

print"Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

print"Waiting For Sensor To Settle"

#after 5 unit time then output
time.sleep(5)
GPIO.output(TRIG, True)

time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
 
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
    
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)

print "Distance:" ,distance,"cm"





def main():
    
    print "Welcome to King Pong!"
    
    while(DONE==false)
        if (20 < distance < 30):
            system_trigger = TRUE
            new_x = input() #determine the unit difference to move, for examplle 1 unit = 10 steps
            pwm_y = input()
            
            if (0 <= new_x < 4):
                direction = ccw
            elif (4 > new_x < 9):
                direction = cw
                
                
            motor_steps = difference_x * 32;
            stepperMotorBase(motor_steps, direction)
            DCFan(pwm_value)
            #delay for fan up to full speed5 units
            #delay for ball ball to get loaded in the slot
            
            #delay for ball to be shot, or in cup
            #delay for cup taking out
            #remove the cup from the arrays, update total amonut of cups left
            #reset to cen ter position
            stepperMotorBase(motor_step, ~direction)
            
            #send a done back to the while loop
            
        #receive x and y
        #run sensor to return a distance to trigger the system 50
        #flag to determine if there's a cup present within the 50 - 70, then send a flag to trigger the system
        #which x, new position using user input, to get the difference. 
        #which y, user input
        



# Constants for x and y 
position_array = [0,1,2,3,4,5,6,7,8]
pwm_array = [0,1,2,3]  #associate with a pwm %

#pwm function, case statements, 0 - 50%, 1- 60%, 2-70%, 3-80%


two_d_array[][] = [position_array][pwm_array]

INITIAL = 4
current_x  = 4
previous_x = 4
new_x = 0
difference_x = new_x - current_x

delay_sensor = 10
delay_fan = 5
delay_shoot = 12





def main():
    
    print "Welcome to King Pong!"
    
    while(DONE==false)
        
    
    
    
    #stepperMotorBase(64, 1)  # 90 degrees
    while (20 < distance < 30):
        DCfan(input()) # max RPM
    #stepperMotorBase(16, -1) # 90 degrees other way
    
    GPIO.cleanup()

# 2 dimensional array to control the time and the amount of steps to step for the motors
def stepperMotorBase(x, dir): # 0.03 = 30 ms
    
    print("Stepper Motor from Base is Turning!")
    
    if (dir ==1):
        for i in range(x): # 90 degrees
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(control_pins[pin], halfstep_forward[halfstep][pin])
                time.sleep(0.03)

    if(dir ==-1):
        for i in range(x): # 90 degrees
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(control_pins[pin], halfstep_reverse[halfstep][pin])
                time.sleep(0.03)

    for pin in control_pins:
        GPIO.output(pin, 0)
        
    print("Finished Stepper Motor")
    
    
# Incorporate the fan into the main code running in parallel
# insert a delay waiting for the fan at full speeds

def DCfan(pwm):
    
    
    print("Fan is turning on in 3 seconds")
    print"3"
    time.sleep(1)
    print"2"
    time.sleep(1)
    print"1"
    time.sleep(1)
    
    wiringpi.pwmWrite(18, 0)   # minimum RPM
    print("PWM: 0")
    #there needs to be an assertion of delay for the fan to be ready operating at full speed


    #100% test
    print("PWM: 128 100% for 5") 
    wiringpi.pwmWrite(18, 90)  # maximum RPM
    time.sleep(10)
    
    print("sleep for 20")
    wiringpi.pwmWrite(18, 0)  # maximum RPM
    time.sleep(10)
    
    
   #90% test 
    print("PWM: 115 90% for 5") 
    wiringpi.pwmWrite(18, 90)  # maximum RPM
    time.sleep(10)
    
    
    print("sleep for 20")
    wiringpi.pwmWrite(18, 0)  # maximum RPM
    time.sleep(10)
    print("Finished Fan")
    
   #90% test 
    print("PWM: 100 80% for 5") 
    wiringpi.pwmWrite(18, 90)  # maximum RPM
    time.sleep(10)
    
    
    print("sleep for 20")
    wiringpi.pwmWrite(18, 0)  # maximum RPM
    time.sleep(10)


   #70% test 
    print("PWM: 90 70% for 5") 
    wiringpi.pwmWrite(18, 90)  # maximum RPM
    time.sleep(10)
    
    
    print("sleep for 20")
    wiringpi.pwmWrite(18, 0)  # maximum RPM
    time.sleep(10)
    
    #60% test 
    print("PWM: 77 60% for 10") 
    wiringpi.pwmWrite(18, 90)  # maximum RPM
    time.sleep(10)
    
    
    print("sleep for 5")
    wiringpi.pwmWrite(18, 0)  # maximum RPM
    time.sleep(5)
    print("Finished Fan")
    
    
    wiringpi.pwmWrite(18, 0)  # maximum RPM
main()

