"""
File: RFCodes.py
Author: Chad Hoevenaars
Updated: June 15, 2020
Desc: This file contains the dictionary for all RFCodes used with the Broadlink RM Pro+
Format: Key = Node_Name (this will be used as the MAC address when converted to Hex.
        Value = A List of 3 binary codes (0 = Stop, 1 = Up, -1 or 3 is Down)
"""
RFCodes = {
    "Office_Blind": [
        b'\xb2\x00\xa4\x00\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x19\x18\x0c\x0c\x18\x19\x0c\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x0c\x0c\x19\x18\x00\x01+\xa34\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x19\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x17\r\x18\x0c\x19\x0b\x19\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x17\x18\r\x0c\x19\x17\r\x0c\x18\x18\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x00\xcc\x01\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x18\x0c\r\x18\x18\x0c\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\x18\x00\x01+\xa44\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x19\x0b\x19\x0c\x18\x18\x0c\x18\r\x0c\x18\r\x18\x18\x0c\x0c\x19\x0c\x18\x18\r\x17\r\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x18\r\x0c\x18\r\x17\r\x18\x18\x0c\r\x18\x0c\x18\x0c\x19\x18\x00\x01+\xa44\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x19\x18\x0c\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x18\x0c\r\x17\x19\x0c\r\x17\r\x18\r\x17\x18\r\x0c\x18\r\x18\x0c\x18\x18\x00\x02\x13\xa45\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\r\x0c\x18\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x17\r\x18\x0c\x18\x18\r\x0c\x19\x0c\x18\x0c\x18\x18\x00\x01+\xa44\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x18\r\x18\x0c\x0c\x19\x0c\x18\x18\x0c\x0c\x18\r\x18\x18\x0c\x19\x0c\x0c\x18\r\x18\x0c\x18\x0c\x19\x18\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x18\r\x0c\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\x0c\x19\x17\x00\x01+\xa45\x0c\x18\x0c\x19\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x19\x18\x0c\x18\x0c\x0c\x19\x0c\x18\x18\r\x0c\x18\x0c\x19\x17\r\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x19\x0c\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x19\x0b\x19\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xb2\x00\xf6\x01\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\x19\x0c\r\x17\r\x17\x19\x0c\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\r\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x19\x18\x0c\x0c\x18\x18\r\x0c\x18\r\x17\x19\x0c\x18\x0c\x18\r\x18\x0c\r\x18\x0c\x00\x016\xa54\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\r\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x18\r\x17\r\x18\x0c\x18\r\x17\r\x18\r\x18\x0c\x18\x18\r\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x0c\x18\x0c\x19\x0c\r\x17\r\x00\x016\xa44\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x0c\r\x17\r\x18\x0c\x18\r\x18\x18\x0c\r\x17\r\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x18\x0c\x0c\x18\x19\x0c\x0c\x18\r\x18\x18\x0c\x19\x0c\x18\x0c\x18\x0c\r\x18\x0c\x00\x016\xa54\x0c\x18\x0c\x19\x0c\x18\r\x17\r\x18\x0c\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x19\x18\x0c\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x18\r\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x0c\x18\x0c\x19\x0c\r\x17\r\x00\x016\xa53\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x19\x0b\x19\x0c\r\x17\r\x18\r\x17\r\x17\x19\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x0c\x18\x19\x0c\x0c\x18\x0c\x18\x18\r\x18\x0c\x19\x0c\x18\x0c\r\x18\x0c\x00\x016\xa53\r\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\r\x17\x18\r\x18\x0c\r\x18\r\x17\x19\x0c\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\r\x17\r\x18\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x0c\x18\x0c\x19\x0c\r\x17\r\x00\x05\xdc\x00\x00'],
    "Corner_Blind": [
        b'\xb2\x00\xbe\x01\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0b\r\x17\r\x18\x18\x0b\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x18\x0c\r\x17\x18\x0c\r\x17\x18\x00\x01+\xa34\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x17\r\x17\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\x0c\x18\r\x17\r\x17\x19\x0b\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x17\x19\x0b\r\x17\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x00\x02\x1e\xa43\r\x17\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\r\x17\r\x17\x19\x0b\x19\x0c\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\r\x17\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x17\r\x18\x18\x0c\r\x17\x18\x0c\x0c\x18\x18\x0c\r\x17\x18\x0c\r\x17\x18\x00\x01+\xa43\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0b\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\r\x17\r\x17\x19\x0b\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x0c\x0c\x18\x18\x0c\x0c\x18\x18\x00\x01*\xa52\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\r\x17\x0c\x18\x18\x0c\x19\x0b\r\x17\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x17\r\x17\r\x18\x0c\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x18\x0c\r\x17\x18\x0c\r\x18\x18\x00\x02\x1e\xa43\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\r\x17\r\x18\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xb2\x01\x84\x03\x18\x0c\x0c\x18\r\x17\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x18\x0c\x17\r\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x18\x00\x01*\xa43\x0c\x19\x0b\x19\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\r\x17\r\x0b\x19\x0c\x18\x0c\x17\r\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x19\x0b\x18\x0c\x18\x0c\x19\x0b\x19\x17\x0c\r\x18\x0c\x18\x0c\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x18\x00\x02\x1e\xa43\r\x18\x0c\x17\x0c\x18\r\x17\r\x18\x0b\x18\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\r\x17\x0c\x0c\x18\r\x18\x0c\x18\x0c\x17\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\x0c\x18\r\x18\x17\x0c\x0c\x18\x0c\x18\r\x18\x17\x00\x01+\xa34\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\r\x0b\x18\x0c\x19\x17\r\x17\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x19\x0b\x18\x0c\x18\x0c\x18\x0c\x19\x0c\x17\r\x17\x0c\x19\x0c\x18\x0c\x18\x17\r\x0c\x18\x0b\x19\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x01*\xa43\x0c\x18\x0c\x18\x0c\x19\x0b\x18\r\x18\x0b\x19\x0b\x18\x18\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\x18\r\x0b\x18\r\x17\r\x18\x0c\x18\x0b\x19\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x18\x17\x00\x02\x1f\xa34\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x19\x17\r\x17\r\x0c\x18\x0c\x18\x17\r\x0c\x18\x0b\x19\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x19\x0b\x18\x0c\x18\x18\r\x0b\x18\x0c\x19\x0c\x17\x18\x00\x01+\xa34\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\r\x0b\x18\x0c\x18\x18\x0c\x0c\x19\x0c\x18\x17\r\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x18\x0c\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x18\x00\x01*\xa43\r\x17\x0c\x18\x0c\x19\x0b\x19\x0c\x18\x0c\x18\x0c\x18\x17\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x17\x0c\x18\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\r\x0b\x19\x0b\x18\r\x18\x17\r\x0c\x17\r\x18\x0c\x18\x17\x00\x02\x1f\xa43\x0c\x19\x0b\x18\x0c\x19\x0c\x17\x0c\x18\r\x17\r\x18\x17\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\r\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x19\x17\r\x0b\x18\x0c\x19\x0b\x19\x17\x00\x01+\xa34\x0b\x19\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x19\x0c\x18\x18\x0b\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x19\x0c\x17\r\x18\x17\x0c\r\x18\x0c\x18\x0b\x19\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x01*\xa43\x0c\x18\x0c\x18\x0c\x19\x0b\x18\r\x17\x0c\x19\x0b\x18\x18\r\x17\r\x0c\x18\x0b\x19\x17\r\x0c\x18\x0c\x18\x18\x0c\x17\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x19\x0b\x19\x0b\x19\x0c\x18\x0b\x19\x0b\x18\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x17\r\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x01\x84\x03\x18\x0c\x0c\x18\r\x17\x18\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x17\x19\x0b\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x17\x19\x0b\r\x17\r\x17\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x17\r\x18\x00\x01*\xa43\x0c\x18\x0c\x18\x0c\x18\r\x18\x0b\x18\r\x17\r\x17\x19\x0c\x18\x0b\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x17\x19\x0b\x0c\x18\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x19\x0b\x18\x0c\r\x17\r\x17\x18\x0c\x18\x00\x02\x1e\xa43\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\r\x17\r\x17\x19\x0b\x19\x0b\r\x17\r\x18\x0c\x18\x0c\x17\x19\x0b\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x17\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x00\x01*\xa43\r\x17\r\x18\x0c\x17\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\r\x17\r\x17\x18\x0c\x18\x0c\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x17\r\x17\r\x17\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x00\x01*\xa43\r\x17\r\x18\x0c\x17\r\x18\x0c\x17\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x0c\x18\r\x17\x0c\x18\r\x17\r\x17\x18\r\x0c\x17\r\x18\x18\x0b\x19\x0b\r\x18\x0c\x18\x18\x0c\x18\x00\x02\x1e\xa34\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x17\r\x17\r\x17\x18\x0c\x18\x0c\r\x17\r\x17\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0b\r\x17\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x18\x0c\x19\x0c\x0c\x17\r\x17\x18\r\x18\x00\x01*\xa43\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\x19\x0b\r\x17\r\x17\x19\x0c\x0c\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\r\x17\x0c\x18\x18\x0c\r\x17\r\x17\r\x18\x0c\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\x19\x00\x01)\xa53\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x19\x0b\x18\x0c\r\x17\r\x17\x19\x0c\x0c\x17\r\x17\x19\x0b\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x17\r\x18\x0c\x18\r\x17\x0c\x18\x18\x0c\x0c\x18\r\x17\x18\x0c\x19\x0b\r\x17\r\x18\x17\x0c\x19\x00\x02\x1d\xa43\r\x17\r\x17\r\x17\r\x17\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x18\x0c\x19\x0c\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0b\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x17\x0c\x18\r\x17\r\x18\x0c\x17\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x00\x01*\xa43\r\x17\r\x17\r\x18\x0c\x17\r\x17\r\x17\r\x17\x19\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x17\x19\x0b\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x18\x0c\x19\x0b\r\x18\x0c\x17\x18\x0c\x19\x00\x01*\xa34\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\x0c\x18\x18\r\x17\x0c\x0c\x19\x0c\x17\x19\x0b\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x0c\x18\r\x17\x0c\x19\x0c\x18\x0c\x17\r\x17\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\x18\x00\x05\xdc\x00\x00\x00\x00'],
    "Left_Blind": [
        b'\xb2\x00\x0c\x01\x19\x0c\x0c\x18\x18\x0c\r\x17\x18\r\x0b\x18\x18\x00\x02\x13\xa44\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x19\x0b\x18\x19\x0c\x0c\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\r\x18\x0c\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\x19\x0c\x0c\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x19\x00\x01*\xa34\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x17\r\x18\x18\x0c\x18\r\x0c\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x19\x0c\x17\r\x18\x0c\x17\x19\x0c\x0c\x18\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\r\x0c\x17\r\x18\x18\x0c\x0c\x18\x18\x0c\x0c\x18\x19\x0b\r\x18\x18\x00\x01*\xa43\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x17\r\x18\x0c\x18\x18\r\x17\x0c\r\x18\x0c\x17\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\x19\x0c\x0c\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xb2\x00\x94\x02\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x18\r\x17\r\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\x0c\x18\r\x18\x0c\x18\r\x17\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x0c\x18\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x19\x00\x01)\xa53\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0b\r\x18\x0c\x18\x18\x0c\r\x17\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x17\r\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x02\x13\xa53\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\r\x17\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x19\x0c\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x01*\xa43\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x17\r\x0c\x18\x0c\x17\x19\x0c\x18\x0c\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\r\x17\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x18\x18\x00\x01)\xa54\x0b\x19\x0c\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x19\x0b\x18\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x00\x02\x13\xa44\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\x0c\x19\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\x18\x00\x01+\xa34\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x17\r\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x18\x18\x00\x01)\xa44\r\x17\x0c\x19\x0b\x19\x0c\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x19\x0c\x17\x19\x0c\x0c\x17\r\x18\x18\x0c\x18\r\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x17\x18\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x01\x84\x03\x18\x0c\x0c\x18\r\x17\x19\x0b\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\x18\x0c\x19\x0b\r\x18\x0c\x18\x18\x0c\x18\x00\x01*\xa44\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\r\x17\r\x18\x18\x0b\x19\x0c\r\x17\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\r\x17\x18\x0c\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x00\x02\x13\xa44\x0c\x18\r\x17\r\x17\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x19\x0b\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\x19\x00\x01*\xa34\r\x17\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\r\x17\r\x17\r\x17\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0b\r\x17\r\x18\x18\x0c\x18\x00\x01*\xa43\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x19\x0b\x19\x0b\r\x18\x0c\x18\x18\x0c\r\x17\r\x17\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\r\x17\x19\x0b\x18\x0c\r\x17\r\x18\x18\x0c\x18\x00\x02\x13\xa43\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x19\x0b\x19\x0b\r\x18\x0c\x18\r\x17\r\x17\x18\x0c\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x17\x19\x0c\x18\x00\x01*\xa43\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\x0c\x19\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x17\r\x18\x0c\x17\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0b\r\x17\r\x17\x19\x0c\x18\x00\x01*\xa43\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0b\x19\x0b\r\x18\x0c\x18\x18\x0c\r\x17\r\x17\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x18\x0c\x19\x00\x02\x12\xa44\x0c\x18\r\x17\r\x17\r\x17\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x18\x18\x0c\r\x17\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x19\x00\x01*\xa34\r\x17\r\x17\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0b\x19\x00\x01*\xa43\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0b\x19\x0b\r\x17\r\x18\x18\x0c\r\x17\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\r\x17\x18\r\x18\x0b\r\x17\r\x17\x19\x0c\x18\x00\x05\xdc\x00\x00\x00\x00'],
    "Right_Blind": [
        b'\xb2\x00\xbe\x01\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\r\x0c\x18\x18\x0c\r\x17\x19\x0b\r\x18\x18\x00\x01+\xa43\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\r\x18\x18\x0c\x18\r\x0b\x19\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\r\x17\r\x17\x19\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\r\x17\r\x18\x18\x0c\r\x17\x19\x0b\r\x18\x18\x0c\r\x18\x18\x00\x01*\xa44\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x17\x18\r\x18\x0c\x0c\x18\r\x18\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\x18\r\x0c\x18\x18\x0c\r\x18\x18\x00\x02\x1f\xa53\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x0c\x18\x18\x0c\x0c\x18\x18\r\x0c\x18\x18\x0c\r\x17\x18\x00\x01+\xa44\r\x17\x0c\x18\r\x18\x0c\x18\r\x17\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x17\x0c\x19\x0c\x18\x18\x0c\x0c\x19\x0b\x19\x0c\x18\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x0c\r\x18\x18\x00\x01*\xa44\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x19\x18\x0c\x18\x0c\x0c\x18\r\x17\r\x18\r\x17\x19\x0b\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x17\x19\x0c\r\x17\x19\x0c\x0c\x18\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xb2\x00r\x02\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x0c\x19\x0c\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\r\x17\r\x17\r\x18\x18\x00\x01*\xa44\r\x17\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x18\x19\x0b\x19\x0c\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x00\x02 \xa44\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x19\x0c\x0c\x18\r\x17\x18\x0c\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\r\x17\x19\x0c\r\x17\r\x18\x0c\x18\x18\x00\x01*\xa53\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x00\x01+\xa44\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x17\r\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\r\x17\r\x18\x18\x00\x02 \xa43\r\x18\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x19\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x18\r\x17\x19\x00\x01*\xa44\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x19\x18\x0c\x0c\x18\x0c\x18\x19\x0c\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\r\x17\r\x18\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\r\x18\x0c\x17\r\x18\x18\x00\x01+\xa43\r\x18\x0c\x19\x0c\x17\r\x18\x0c\x18\x0c\x18\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x19\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x17\r\x18\r\x17\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00',
        b'\xb2\x00\xa0\x01\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\r\x17\r\x17\x19\x0c\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x19\x0c\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\x19\x0b\r\x18\x0c\x18\x18\x0c\x18\x00\x01+\xa44\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\x19\x0b\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x19\x0c\x18\x0c\x0c\x18\r\x18\x18\x0c\x18\x00\x02\x1f\xa53\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\r\x17\r\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x19\x0b\x19\x0c\x0c\x18\x0c\x18\x19\x0c\x18\x00\x01*\xa44\x0c\x18\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x17\x19\x0c\x0c\x18\r\x17\x19\x0b\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x17\x18\r\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\r\x17\r\x17\x19\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x00\x01*\xa44\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\r\x17\r\x17\r\x18\r\x18\x0c\x18\x0c\x18\x0c\x19\x0c\x18\x18\x0c\x0c\x18\r\x18\x0c\x18\r\x17\x19\x0c\x18\x0c\x0c\x18\r\x17\x19\x0c\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00\x00\x00'],
    "Padio_Blind": [
        b'\xb2\x00B\x02\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\x18\r\x0c\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x19\x00\x02\t\xa43\r\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\r\x17\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\r\x17\r\x17\x18\x0c\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x19\x0c\x0c\x18\x18\x00\x01+\xa34\r\x17\x0c\x19\x0c\x18\r\x17\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x0c\x18\x0c\x18\x19\x0c\x18\x0c\r\x17\r\x17\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\r\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\x18\x0c\r\x17\x19\x0c\x0c\x18\x18\x0c\r\x17\x19\x00\x01*\xa44\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x19\x0b\x18\r\x0c\x18\x18\x0c\r\x18\x18\x0c\x0c\x18\x19\x0b\r\x17\x19\x00\x02\x08\xa44\x0c\x18\r\x17\r\x18\x0c\x17\r\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\x0c\x18\x0c\x18\x19\x0b\r\x17\r\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x17\x0c\x18\r\x17\x19\x0c\x18\x0c\r\x17\x19\x0b\r\x17\x19\x0c\x0c\x18\x18\x0c\r\x17\x19\x00\x01*\xa44\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x18\x0c\r\x17\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x00\x01*\xa44\r\x17\x0c\x18\r\x17\r\x17\r\x18\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\x0c\x19\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x19\x18\x0b\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x18\x0c\x0c\x18\x18\x0c\r\x17\x19\x0c\x0c\x18\x18\x00\x05\xdc\x00\x00\x00\x00\x00\x00',
        b'\xb2\x00\xa4\x01\xa44\x0c\x19\x0b\x18\r\x18\x0c\x18\x0c\x19\x0c\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\r\x18\x0b\r\x18\x0c\x18\r\x18\x17\x0c\r\x18\x0c\x18\x0c\x18\x18\x00\x01+\xa34\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x0c\x17\x19\x0c\x18\x0c\r\x17\r\x18\x18\x0c\r\x17\r\x17\x19\x0b\x19\x0c\x0c\x18\x0c\x19\x0c\x17\r\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x18\x00\x02\x08\xa53\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\x18\r\x18\x0c\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\r\x17\x0c\x18\x19\x0b\r\x18\x0c\x18\x0c\x18\x19\x00\x01*\xa43\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\x0c\x0c\x19\x0c\x17\x19\x0c\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\r\x18\x0c\x0c\x18\x0c\x18\r\x17\x19\x0c\x0c\x18\x0c\x18\r\x17\x19\x00\x01*\xa34\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x19\x0b\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\x18\r\x0c\x18\r\x18\x0c\x17\x19\x0c\x0c\x18\x0c\x18\r\x18\x18\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x01\x84\x03\x18\x0c\x0c\x18\x0c\x18\x19\x0b\x19\x0c\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x17\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0c\x18\x00\x01*\xa44\x0c\x18\r\x17\r\x17\r\x17\r\x18\r\x17\r\x17\x18\x0c\x19\x0c\x0c\x18\r\x18\x17\r\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0b\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0b\x19\x0c\x0c\x18\x0c\x18\x19\x0b\x19\x00\x02\x08\xa43\r\x17\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x17\r\x18\x18\x0c\x18\x00\x01+\xa34\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\x19\x0b\x19\x0c\x0c\x18\x0c\x18\r\x17\r\x18\x18\x0c\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0c\x18\x00\x01*\xa44\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\x0c\x18\r\x17\x19\x0b\x19\x00\x02\x08\xa44\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\x18\r\x18\x0c\x0c\x18\x0c\x18\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\r\x17\r\x17\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\x19\x0c\x0c\x18\r\x17\x19\x0b\x19\x00\x01*\xa44\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\r\x17\x18\x0c\x18\r\x0c\x18\x0c\x18\x18\x0c\x18\x0c\r\x18\x0c\x18\x18\x0c\x19\x00\x01*\xa34\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\r\x17\x19\x0c\x0c\x18\x0c\x18\x18\r\x17\r\x0c\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x19\x0c\x18\x00\x02\x08\xa44\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x0c\x18\x19\x0c\x18\x0c\x0c\x18\r\x17\x18\x0c\r\x18\x0c\x18\x18\x0c\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\x18\r\x0c\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x18\x0c\x18\x0c\x0c\x18\r\x17\x19\x0c\x18\x0c\x0c\x18\r\x17\x19\x0b\x19\x00\x01*\xa43\r\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\x19\x0c\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x17\x19\x0c\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\x18\r\x18\x0c\x0c\x18\r\x17\x19\x0c\x18\x0c\x0c\x18\x0c\x18\x18\x0c\x19\x00\x01*\xa44\x0c\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x19\x0b\r\x18\x0c\x18\x18\x0c\r\x17\x0c\x18\x19\x0c\x18\x0c\x0c\x18\r\x18\x0c\x18\x0c\x18\x18\x0c\r\x17\r\x18\x0c\x18\x0c\x18\r\x17\r\x17\r\x17\r\x18\x0c\x18\x18\x0c\x18\r\x0c\x18\x0c\x18\x19\x0b\x19\x0c\x0c\x18\x0c\x18\x18\x0c\x18\x00\x05\xdc\x00\x00\x00\x00'],
    "Bedroom_Blind": [
        b'\xb2\x03\x84\x03\x19\x0c\x0c\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\r\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\x0c\x18\x19\x0c\r\x18\x18\x0c\x0c\x19\x18\x0c\x0c\x19\x18\x00\x01+\xa44\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\x19\x0c\r\x17\r\x18\x18\x0c\r\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x17\r\x18\x0c\x18\x19\x0c\x0c\x19\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x19\x18\x0c\x18\x0c\r\x18\r\x17\x18\r\x0c\x18\x19\x0c\x0c\x18\x19\x0c\x0c\x19\x18\x00\x02(\xa44\r\x18\x0c\x18\r\x18\r\x17\r\x18\r\x17\r\x18\x18\r\x18\x0c\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\r\x18\r\x17\r\x18\r\x18\x0c\x18\r\x18\x18\x0c\x18\x0c\r\x18\r\x18\x18\x0c\r\x17\x19\x0c\r\x18\x18\x0c\r\x18\x18\x00\x01+\xa44\r\x18\x0c\x18\r\x18\r\x17\r\x18\r\x17\r\x18\x18\x0c\x19\x0c\r\x18\x0c\x18\x18\r\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\r\x17\r\x18\x0c\x19\x0c\x18\x0c\x19\x0c\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x18\x18\x0c\x0c\x19\x18\x0c\r\x18\x18\x0c\r\x18\x18\x00\x01+\xa45\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\r\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\x0c\x19\x18\x0c\x0c\x18\x19\x0c\r\x17\x19\x0c\r\x17\x19\x00\x02(\xa54\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\r\x17\r\x18\x18\x0c\x19\x0c\r\x18\x0c\x18\x18\r\x0c\x18\r\x18\x18\x0c\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\r\x18\x18\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x00\x01+\xa44\r\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\x18\r\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x18\r\x18\r\x17\r\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\r\x18\x0c\x18\x0c\x18\r\x18\r\x18\x18\x0c\x18\x0c\r\x18\r\x18\x18\x0c\r\x18\x18\r\x0c\x18\x18\r\x0c\x18\x18\x00\x01+\xa45\x0c\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\r\x17\r\x18\x18\x0c\x19\x0c\r\x17\r\x18\x18\x0c\r\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x18\r\x17\r\x18\x18\r\x0c\x18\x0c\x18\r\x18\r\x17\r\x18\r\x17\r\x18\r\x18\x17\r\x18\x0c\r\x18\r\x17\x19\x0c\r\x18\x18\x0c\x0c\x19\x18\r\x0b\x19\x18\x00\x02(\xa54\x0c\x18\r\x17\r\x18\r\x18\x0c\x18\r\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x18\r\x18\x0c\r\x17\r\x18\r\x17\r\x18\x18\r\x0c\x18\x0c\x18\r\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x19\x0c\x18\r\x0c\x18\r\x18\x18\r\x0c\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x00\x01+\xa44\r\x18\x0c\x19\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\x19\x0c\x18\x0c\x0c\x19\x0c\x18\x19\x0c\x0c\x18\r\x18\x18\x0c\x19\x0c\r\x17\r\x18\x0c\x18\r\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\r\x18\x0c\x18\r\x17\r\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x0c\r\x18\x18\x00\x01+\xa44\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\x18\x0c\x19\x0c\r\x17\r\x18\x18\x0c\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x17\x0e\x17\x18\r\x18\x0c\r\x18\x0c\x18\x19\x0c\x0c\x18\x19\x0c\x0c\x18\x19\x0c\r\x17\x19\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x00t\x01\x0c\x18\r\x18\r\x17\r\x18\x0c\x19\x0c\x18\x18\x0c\x19\x0c\x0c\x19\x0c\x19\x0b\x19\x0c\x18\x18\r\x0c\x18\r\x18\x0c\x18\x19\x00\x01*\xa45\x0c\x19\x0b\x19\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x17\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x18\r\x0c\x18\x0c\x19\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\r\x18\x0c\x0c\x19\x0c\x18\x0c\x19\x0c\x18\x18\r\x0c\x18\x0c\x18\r\x18\x18\x00\x02(\xa54\x0c\x19\x0c\x18\x0c\x18\r\x18\r\x17\r\x18\x0c\x19\x18\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\x18\r\x18\r\x0c\x18\x0c\x18\r\x18\r\x18\x17\r\x0c\x18\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\x0c\x18\r\x18\x18\r\x0c\x18\r\x18\x0c\x18\x18\x00\x01+\xa45\x0c\x19\x0c\x18\r\x17\r\x18\x0c\x18\r\x18\x0c\x19\x17\r\x18\r\x0c\x18\r\x17\x19\x0c\r\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x19\x0c\x18\x0c\x18\x18\r\x0c\x18\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\x18\x0c\x19\x0c\x0c\x18\r\x18\x0c\x19\x0c\x18\x18\x0c\r\x18\x0c\x19\x0c\x18\x18\x00\x01+\xa45\x0c\x18\r\x18\x0c\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\x18\x0c\r\x18\r\x18\x18\x0c\x18\r\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\x0c\x19\x0c\x18\x0c\x18\x18\r\x18\x0c\r\x18\r\x18\x0c\x18\x0c\x19\x18\x0c\x0c\x19\x0c\x18\r\x17\x19\x00\x05\xdc\x00\x00\x00\x00',
        b'\xb2\x00\xf6\x01\r\x17\r\x18\x0c\x19\x0c\x18\x0c\x19\x0c\x18\r\x17\x19\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\r\x18\x0c\x18\r\x17\r\x18\x18\r\x18\x0c\r\x18\x0c\x18\r\x18\x18\x0c\x18\r\x18\x0c\x18\r\x0c\x18\r\x00\x016\xa54\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\r\x17\x19\x0c\x0c\x19\x0c\x18\x18\x0c\x19\x0c\r\x17\r\x18\r\x18\x0c\x18\x18\x0c\r\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\x18\r\x0c\x19\x0c\x18\x0c\x18\x18\r\x18\x0c\x19\x0c\x18\r\x0c\x18\x0c\x00\x017\xa44\r\x18\x0c\x18\r\x18\r\x18\x0c\x18\r\x17\r\x18\x18\r\x18\x0c\x0c\x19\x0c\x18\x19\x0c\x0c\x18\r\x18\x18\x0c\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x19\x18\x0c\x18\x0c\r\x18\r\x17\r\x18\x18\r\x18\x0c\x18\r\x18\x0c\r\x18\x0c\x00\x017\xa44\r\x18\x0c\x19\x0c\x18\x0c\x18\r\x18\x0c\x19\x0c\x18\x18\r\x17\r\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\r\x17\r\x18\r\x18\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\r\x17\r\x18\x0c\x18\x19\x0c\x18\x0c\r\x18\x0c\x19\x0c\x18\x18\r\x18\x0c\x18\r\x18\x0c\x0c\x18\r\x00\x016\xa54\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x18\r\x0c\x18\r\x18\x18\x0c\r\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x18\r\x18\x0c\x18\x19\x0c\x0c\x18\r\x18\x0c\x18\r\x18\r\x17\r\x18\x0c\x18\r\x18\x18\r\x18\x0c\x0c\x19\x0c\x18\r\x18\x18\x0c\x18\r\x18\x0c\x19\x0c\x0c\x18\r\x00\x016\xa45\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\r\x18\x0c\x18\x18\r\x18\x0c\r\x18\x0c\x18\x18\r\x0c\x18\r\x18\x18\x0c\x19\x0c\r\x18\x0c\x18\x0c\x18\r\x18\x18\x0c\r\x18\r\x17\r\x18\r\x17\r\x18\x0c\x19\x0c\x18\x0c\x18\x19\x0c\x18\r\x0c\x18\x0c\x19\x0c\x18\x18\x0c\x19\x0c\x18\x0c\x19\x0c\r\x18\x0c\x00\x05\xdc\x00\x00']
    }
