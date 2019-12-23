/*
	How to install FLTK: http://www.c-jump.com/bcc/common/Talk2/Cxx/FltkInstallVC/FltkInstallVC.html
	Made by: Magnus S. Aarnes 2019/2020 (i take no responsibility of shitty code as that obviously was written by my evil twin)
	FLTK 1.3.5 doc: https://www.fltk.org/doc-1.3/index.html 
*/

#include <FL/Fl.H>
#include <FL/Fl_Box.H>
#include <FL/Fl_Window.H>

int main(int argc, char **argv) {
	
	Fl_Window *window = new Fl_Window(340, 180);
	
	Fl_Box *box = new Fl_Box(20, 40, 300, 100, "Hello, World!");
	box->box(FL_UP_BOX);
	box->labelfont(FL_BOLD + FL_ITALIC);
	box->labelsize(36);
	box->labeltype(FL_SHADOW_LABEL);
	window->end();
	window->show(argc, argv);
	return Fl::run();
}