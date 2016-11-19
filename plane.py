import RPi.GPIO as GPIO

class plane():

    motor1 = 1

    """Will Assign Pin values"""
    def __init__(self):
        print "CONSTRUCTOR"

    """Tests a motor"""
    def test_motor(self):
        print "running"
        pwm=GPIO.PWM(motor1,50)
        pwm.start(5)
        pwm.ChangeDutyCycle(7.5)
        print "DONE"
