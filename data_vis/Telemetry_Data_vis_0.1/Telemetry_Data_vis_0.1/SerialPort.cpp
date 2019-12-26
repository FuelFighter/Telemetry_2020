#include "SerialPort.h"

/* Zain Ul Mustafa 2017 */

//Rules:
/*
1. Check if connection with Arduino is made
2. If Arduino is connected then take input from user in a String
3. Make a char array of the size of string + 1
4. Copy the whole string into the char array
5. Add escape sequence \n because this represents the end of a line in Serial Comm port
6. Write the whole char array into the buffer (a buffer takes the info forward to the Serial Comm Port)
7. Read from the Arduino if data is received successfully or if the action is taken as per needed
*/

//Connect with me:
/*	Twitter: http://www.twitter.com/ZainsOfficial/
	Facebook: http://www.facebook.com/ZainsOfficial/
	Github: http://github.com/ZainUlMustafa/
*/

/* This software is allowed for any user to copy, modify, merge, and distribute in any of his/her project.
Complete repository for this project is available on github. If you find this project anywhere except github, it
is to be noted that it is not made by me and not distributed by me.
Please follow this link to get to the original repository of github for this project
Github shortened link (no spam and no ads): http://bit.ly/2vGkinQ
*/

/* PC 2 Arduino */



SerialPort::SerialPort(char *portName)
{
	this->connected = false;

	this->handler = CreateFileA(static_cast<LPCSTR>(portName),
		GENERIC_READ | GENERIC_WRITE,
		0,
		NULL,
		OPEN_EXISTING,
		FILE_ATTRIBUTE_NORMAL,
		NULL);
	if (this->handler == INVALID_HANDLE_VALUE) {
		if (GetLastError() == ERROR_FILE_NOT_FOUND) {
			printf("ERROR: Handle was not attached. Reason: %s not available\n", portName);
		}
		else
		{
			printf("ERROR!!!");
		}
	}
	else {
		DCB dcbSerialParameters = { 0 };

		if (!GetCommState(this->handler, &dcbSerialParameters)) {
			printf("failed to get current serial parameters");
		}
		else {
			dcbSerialParameters.BaudRate = CBR_9600;
			dcbSerialParameters.ByteSize = 8;
			dcbSerialParameters.StopBits = ONESTOPBIT;
			dcbSerialParameters.Parity = NOPARITY;
			dcbSerialParameters.fDtrControl = DTR_CONTROL_ENABLE;

			if (!SetCommState(handler, &dcbSerialParameters))
			{
				printf("ALERT: could not set Serial port parameters\n");
			}
			else {
				this->connected = true;
				PurgeComm(this->handler, PURGE_RXCLEAR | PURGE_TXCLEAR);
				Sleep(ARDUINO_WAIT_TIME);
			}
		}
	}
}

SerialPort::~SerialPort()
{
	if (this->connected) {
		this->connected = false;
		CloseHandle(this->handler);
	}
}

int SerialPort::readSerialPort(char *buffer, unsigned int buf_size)
{
	DWORD bytesRead;
	unsigned int toRead = 0;

	ClearCommError(this->handler, &this->errors, &this->status);

	if (this->status.cbInQue > 0) {
		if (this->status.cbInQue > buf_size) {
			toRead = buf_size;
		}
		else toRead = this->status.cbInQue;
	}

	if (ReadFile(this->handler, buffer, toRead, &bytesRead, NULL)) return bytesRead;

	return 0;
}

bool SerialPort::writeSerialPort(char *buffer, unsigned int buf_size)
{
	DWORD bytesSend;

	if (!WriteFile(this->handler, (void*)buffer, buf_size, &bytesSend, 0)) {
		ClearCommError(this->handler, &this->errors, &this->status);
		return false;
	}
	else return true;
}

bool SerialPort::isConnected()
{
	return this->connected;
}

string SerialPort::readDataTillSign(char* data)
{
	string dataString;
	for (int i = 0; i < MAX_DATA_LENGTH; i++) {
		if (data[i] == '\n') {
			break;
		}
		dataString += data[i];
	}
	return dataString;
}


