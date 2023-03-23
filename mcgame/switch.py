import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
MOTOR_P = 19
MOTOR_M = 13

SW1_PIN = 4
SW2_PIN = 17
SW3_PIN = 18

SW_PIN_LIST = [SW1_PIN, SW2_PIN, SW3_PIN]

if __name__ == "__main__":
    GPIO.setup(SW_PIN_LIST, GPIO.IN)
    GPIO.setup(MOTOR_P, GPIO.OUT)
    GPIO.setup(MOTOR_M, GPIO.OUT)

    try:
        while (True):
            button_state = []
            for i in SW_PIN_LIST:
                button_state.append(GPIO.input(i))
            if button_state[0] == 0 and button_state[1] == 1 and button_state[2] == 1:
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(MOTOR_P, GPIO.HIGH)
                GPIO.output(MOTOR_M, GPIO.LOW)
            if button_state[1] == 0 and button_state[0] == 1 and button_state[2] == 1:
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.HIGH)
            if button_state[2] == 0:
                GPIO.output(MOTOR_P, GPIO.LOW)
                GPIO.output(MOTOR_M, GPIO.LOW)

    finally:
        GPIO.cleanup