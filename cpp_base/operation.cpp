class Operation
{
	private:
		auto op1;
		auto op2;

	public:
		auto add()
		{
			if (op1 < 0 || op2 < 0)
			{
				return -1;
			}
			else
			{
				return op1 + op2;
			}
		}
};
