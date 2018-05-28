//Compile with: g++ -o helloworld helloworld.cpp -std=c++11
//Run with ./helloworld

//Library required for writing to stdout
#include <iostream>

int main(int argc, char *argv[])
{
	//Stdout stream, << streaming operator, and a newline character
	std::cout << "Hello World!" << std::endl;
	
	/* Show that the program was successful. 
	This value can be read from commandline */
	return 123;
}

