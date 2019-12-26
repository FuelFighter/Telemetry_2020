/*
	How to install FLTK: http://www.c-jump.com/bcc/common/Talk2/Cxx/FltkInstallVC/FltkInstallVC.html
	Made by: Magnus S. Aarnes 2019/2020 (i take no responsibility of shitty code as that obviously was written by my evil twin)
	FLTK 1.3.5 doc: https://www.fltk.org/doc-1.3/index.html 
*/

#include<iostream>
using namespace std;
#include<string>
#include<stdlib.h>
#include"SerialPort.h"


#include <FL/Fl.H>
#include <FL/Fl_Box.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Multiline_Output.H>


int main() {
	Fl_Window *window = new Fl_Window(340, 180);

	Fl_Multiline_Output *outputBox = new Fl_Multiline_Output(40, 40, 100, 100, "Yo");
	outputBox->insert("test\n", 5);
	outputBox->insert("Test 2", 6);
	outputBox->box(FL_THIN_DOWN_BOX);

	/*Fl_Box *box = new Fl_Box(20, 40, 300, 100, "Hello, World!");
	box->box(FL_UP_BOX);
	box->labelfont(FL_BOLD + FL_ITALIC);
	box->labelsize(36);
	box->labeltype(FL_SHADOW_LABEL); */

	window->end();
	window->show();
	
	while (window->shown()) {
		outputBox->insert("k", 1);
		
		Fl::check();
		Fl::redraw();

		Sleep(16);
		
		//std::this_thread::sleep_until(next);
		//next += std::chrono::microseconds(1000000 / 60);
	}
	return 0;
}


// char output[MAX_DATA_LENGTH];
char incomingData[MAX_DATA_LENGTH];

// change the name of the port with the port name of your computer
// must remember that the backslashes are essential so do not remove them
char portArray[12] = "\\\\.\\COM8";
char *port = portArray;



/*
int main() {
	SerialPort arduino(port);
	if (arduino.isConnected()) {
		cout << "Connection made" << endl << endl;
	}
	
	else {
		cout << "Error in port name" << endl << endl;
		string yeet;
		cin >> yeet;
	}
	

	while (arduino.isConnected()) {

		cout << "Enter your command: " << endl;
		string data;
		cin >> data;

		char *charArray = new char[data.size() + 1];
		copy(data.begin(), data.end(), charArray);
		charArray[data.size()] = '\n';

		arduino.writeSerialPort(charArray, MAX_DATA_LENGTH);
		Sleep(100);



		char *outputData = new char[MAX_DATA_LENGTH];

		arduino.readSerialPort(outputData, MAX_DATA_LENGTH);

		Sleep(100);
		cout << readDataTillSign(outputData) << endl;
		//cout << outputData << endl;
		delete[] outputData;

		
		if (outputData[0] == 'N')
		{
			cout << readDataTillSign(outputData) << endl;
			//cout << outputData << endl;
			delete[] outputData;
		}
		if (outputData[0] == 'S')
		{
			cout << readDataTillSign(outputData) << endl;
			//cout << outputData << endl;
			delete[] outputData;
		}
		
		
		else {
			cout << ">> " << readDataTillSign(outputData) << endl;
			delete[] outputData;
		}
		

	}
	return 0;
}

*/