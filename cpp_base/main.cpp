#include <iostream>
#include <vector>
#include <string>

class Calculator
{
	std::string session_name;
	
	public:
		using number_t = int; // this is a nested type alias

		std::vector<number_t> m_resultHistory{};

		void set_session(std::string name)
		{
			session_name = name;
		}

		void print_session()
		{
			std::cout << "Session: " << session_name << '\n';
			for (Calculator::number_t result : m_resultHistory)
			{
				std::cout << result << '\n';
			}
		}


		number_t add(number_t a, number_t b)
		{
			auto result{ a + b };

			m_resultHistory.push_back(result);

			return result;
		}
};
int main()
{
	Calculator calculator{};
	calculator.set_session("Study");

	std::cout << calculator.add(3, 4) << '\n'; // 7
	std::cout << calculator.add(99, 24) << '\n'; // 123

	calculator.print_session();

	return 0;
}
