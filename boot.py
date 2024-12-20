import usb_hid
import usb_midi
import supervisor
import board
import usb_cdc
# Set the USB serial device name
#usb_cdc.console.serial = "LoveFrenchFries"
import board
import usb_cdc
import time
from adafruit_hid import find_device
import usb_hid
import usb_hid

# IMPORTANT !!!!!!!!! IF YOU CHANGE YOU NEED A HARD RESET TO RECOGNIZE THE DEVICE
# TURN OFF THE DEVICE THEN GO IN BOOT MODE THEN COME BACK TO NORMAL MODE
# This is an updated example of a gamepad report descriptor with 32 buttons.
GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,        # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,        # Usage (Game Pad)
    0xA1, 0x01,        # Collection (Application)
    0x85, 0x04,        #   Report ID (4)
    
    # Buttons (32 buttons)
    0x05, 0x09,        #   Usage Page (Button)
    0x19, 0x01,        #   Usage Minimum (Button 1)
    0x29, 0x20,        #   Usage Maximum (Button 32)
    0x15, 0x00,        #   Logical Minimum (0)
    0x25, 0x01,        #   Logical Maximum (1)
    0x75, 0x01,        #   Report Size (1)
    0x95, 0x20,        #   Report Count (32)
    0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    # Axes (X, Y, Z, Rz)
    0x05, 0x01,        #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x81,        #   Logical Minimum (-127)
    0x25, 0x7F,        #   Logical Maximum (127)
    0x09, 0x30,        #   Usage (X)
    0x09, 0x31,        #   Usage (Y)
    0x09, 0x32,        #   Usage (Z)
    0x09, 0x35,        #   Usage (Rz)
    0x75, 0x08,        #   Report Size (8)
    0x95, 0x04,        #   Report Count (4)
    0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    # Triggers (Rx, Ry)
    0x09, 0x33,        #   Usage (Rx) - Left Trigger
    0x09, 0x34,        #   Usage (Ry) - Right Trigger
    0x15, 0x00,        #   Logical Minimum (0)
    0x25, 0xFF,        #   Logical Maximum (255)
    0x75, 0x08,        #   Report Size (8)
    0x95, 0x02,        #   Report Count (2)
    0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    0xC0               # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(10,),    # This gamepad sends 10 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     usb_hid.Device.CONSUMER_CONTROL,
     gamepad)
)
usb_midi.enable()
