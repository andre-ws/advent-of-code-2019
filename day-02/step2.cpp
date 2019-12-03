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

int processInputFile(vector<int> &input)
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
	return input[0];
}

int process(int noun, int verb, vector<int> input)
{
	input[1] = noun;
	input[2] = verb;
	return processInputFile(input);
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

	for (auto i = 0; i < 99; i++)
	{
		for (auto j = 0; j < 99; j++)
		{
			cout << "Trying combination " << (i+1)*(j+1) << "\r" << flush;
			if (process(i, j, input) == 19690720)
			{
				cout << "Yay! Combination is " << i << " and " << j << endl;
				return 0;
			}
		}
	}
	cout << "Oops, something is terribly wrong!";
	return 1;
}
