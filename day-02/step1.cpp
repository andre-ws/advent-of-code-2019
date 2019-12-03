#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

constexpr int Addition = 1;
constexpr int Multiplication = 2;
constexpr int Eof = 99;

bool isEof(int value)
{
	return value == Eof;
}

void Add(vector<int>::iterator it, vector<int> &input)
{
	input[*(it+3)] = input[*(it+1)] + input[*(it+2)];
}

void Multiply(vector<int>::iterator it, vector<int> &input)
{
	input[*(it+3)] = input[*(it+1)] * input[*(it+2)];
}

vector<int>::iterator Next(vector<int>::iterator it)
{
	return it + 4;
}

void process(vector<int> &input)
{
	for (auto it = input.begin(); it != input.end() && !isEof(*it);)
	{
		auto value = *it;
		switch (value)
		{
		case Addition:
			Add(it, input);
			it = Next(it);
			break;
		case Multiplication:
			Multiply(it, input);
			it = Next(it);
			break;
		default:
			++it;
			break;
		}
	}
	
}

int main(int argc, char* argv[])
{
	string temp;
	vector<int> input;
	ifstream inputFile("input.txt");
	while (getline(inputFile, temp, ','))
	{
		auto token = atoi(temp.c_str());
		input.push_back(token);
	}

	input[1] = 12;
	input[2] = 2;
	process(input);

	cout << input[0];	
	return 0;
}
