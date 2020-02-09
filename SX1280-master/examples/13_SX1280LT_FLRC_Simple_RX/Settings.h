/*
******************************************************************************************************

lora Programs for Arduino

Copyright of the author Stuart Robinson

These programs may be used free of charge for personal, recreational and educational purposes only.

This program, or parts of it, may not be used for or in connection with any commercial purpose without
the explicit permission of the author Stuart Robinson.

The programs are supplied as is, it is up to individual to decide if the programs are suitable for the
intended purpose and free from errors.

Changes:

To Do:

******************************************************************************************************
*/

//*******  Setup hardware pin definitions here ! ***************


#define NSS 10
#define RFBUSY 25
#define NRESET 24
#define LED1 21
#define DIO1 26
#define DIO2 -1                 //not used 
#define DIO3 -1                 //not used                      
#define BUZZER -1 
//*******  Setup LoRa Test Parameters Here ! ***************

//LoRa Modem Parameters
#define Frequency 2445000000                     //frequency of transmissions
#define Offset 0                                 //offset frequency for calibration purposes  
#define Bandwidth LORA_BW_0400                   //LoRa bandwidth
#define SpreadingFactor LORA_SF7                 //LoRa spreading factor
#define CodeRate LORA_CR_4_5                     //LoRa coding rate

const uint8_t TXpower = -18;                     //Start power for transmissions in dBm

#define packet_delay 10                        //mS delay between packets

#define TXBUFFER_SIZE 64
#define RXBUFFER_SIZE 64
