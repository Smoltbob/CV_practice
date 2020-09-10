#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

/* TODO
 * Echantilloner Environ 15 couleurs pour entrainer modele
 * Tester une prédiction avec input RGB
 */

int main(int argc, char** argv)
{
	auto X = cv::Mat::zeros(400,2,CV_32F); // 400 lignes, 2 colonnes
	auto Y = cv::Mat::ones(400,1,CV_32S);
	cv::Mat preds;

	//cv::Ptr<cv::ml::TrainData> data = cv::ml::TrainData::create(X, 0, Y);
	cv::Ptr<cv::ml::TrainData> data = cv::ml::TrainData::loadFromCSV(
			"satfaces_lite.csv", 
			1,
			-1,
			-1,
			"ord[0-2]cat[3]");

	//cout << data->getTrainSamples() << endl;
	//cout << data->getTrainResponses() << endl;

	
       	data->setTrainTestSplitRatio(0.2, true);
	//auto trainData = data->getTrainSamples();
	//auto trainLabels = data->getTrainResponses();
	// SatModel is a pure virtual class
	// Methods are accessed through pointers
	cv::Ptr<cv::ml::KNearest> model = cv::ml::KNearest::create(); 
	model->train(data);
	cout << model->isTrained() << endl;

	auto err = model->calcError(data, true, preds);
	cout << err << endl;

	vector<string> labels;
	data->getNames(labels);
	for (auto label: labels){
		cout << label << endl;
	}

	float pixel[3] = {255,0,190};
	auto sample = cv::Mat(1,3, CV_32F, pixel);
	cv::Mat pred;
	//auto sample = (cv::Mat_<int>(1,3) << 0, -1, 0 );
	    cout << "C = " << endl << " " << sample << endl << endl;

	model->predict(sample, pred, 0);
	cout << labels[pred.at<float>(0)] << endl;
	waitKey();
	
}
