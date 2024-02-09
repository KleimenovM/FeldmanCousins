std::vector<float> aRandomVector(double maxValue, int n)
{
    std::vector<float> result;
    std::srand(std::time(nullptr)); // use current time as seed for random generator
    int random_value = std::rand();
    for (int i = 0; i < n; i++)
    {
        result.emplace_back(std::rand() / (RAND_MAX + 1u) * maxValue);
    }
    return result;
}

void fc()
{
	auto observed = aRandomVector(5.0, 1000);
	auto background = aRandomVector(10.0, 1000);

	auto fc = new TFeldmanCousins();
	fc->SetCL(.9);
    fc->SetMuMax(50);
    fc->SetMuStep(0.0005);

    std::time_t result1 = std::time(nullptr);

	for (int i = 0; i < 1000; i++)
	{
        fc->CalculateUpperLimit(observed[i], background[i]);
	}

	std::time_t result2 = std::time(nullptr);

	std::cout << result2 - result1 << std::endl;
}
