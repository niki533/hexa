import time
from adafruit_pca9685 import PCA9685
import board
import busio

# Create the I2C bus interface
i2c_bus = busio.I2C(board.SCL, board.SDA)

# Create a simple PCA9685 class instance
pca = PCA9685(i2c_bus)
pca.frequency = 50

# Define the servo channels for the hexapod
# Assume each leg has 2 servos: hip (channels 0-5) and knee (channels 6-11)
servo_hip_channels = [0, 1, 2, 3, 4, 5]
servo_knee_channels = [6, 7, 8, 9, 10, 11]

# Define the servo pulse lengths for neutral positions
NEUTRAL_HIP = 307  # Adjust based on your servo calibration
NEUTRAL_KNEE = 307  # Adjust based on your servo calibration

# Define the movement pulse lengths
FORWARD_HIP = [330, 330, 330, 280, 280, 280]
FORWARD_KNEE = [300, 300, 300, 320, 320, 320]

BACKWARD_HIP = [280, 280, 280, 330, 330, 330]
BACKWARD_KNEE = [320, 320, 320, 300, 300, 300]

LEFT_HIP = [330, 330, 300, 280, 280, 320]
LEFT_KNEE = [310, 310, 330, 310, 310, 330]

RIGHT_HIP = [280, 280, 320, 330, 330, 300]
RIGHT_KNEE = [310, 310, 330, 310, 310, 330]

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 50       # 50 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pca.channels[channel].duty_cycle = pulse

def move_hip(positions):
    for i, pos in enumerate(positions):
        set_servo_pulse(servo_hip_channels[i], pos)

def move_knee(positions):
    for i, pos in enumerate(positions):
        set_servo_pulse(servo_knee_channels[i], pos)

def move_forward():
    move_hip(FORWARD_HIP)
    move_knee(FORWARD_KNEE)
    time.sleep(1)
    reset_position()

def move_backward():
    move_hip(BACKWARD_HIP)
    move_knee(BACKWARD_KNEE)
    time.sleep(1)
    reset_position()

def move_left():
    move_hip(LEFT_HIP)
    move_knee(LEFT_KNEE)
    time.sleep(1)
    reset_position()

def move_right():
    move_hip(RIGHT_HIP)
    move_knee(RIGHT_KNEE)
    time.sleep(1)
    reset_position()

def reset_position():
    for channel in servo_hip_channels + servo_knee_channels:
        set_servo_pulse(channel, NEUTRAL_HIP if channel < 6 else NEUTRAL_KNEE)
    time.sleep(1)

# Main loop to test movements
try:
    while True:
        move_forward()
        time.sleep(2)
        move_backward()
        time.sleep(2)
        move_left()
        time.sleep(2)
        move_right()
        time.sleep(2)
except KeyboardInterrupt:
    reset_position()
    pca.deinit()
    print("Program terminated")
