#include <iostream>
#include <opencv2/opencv.hpp>
 
using namespace cv;
using namespace std;
 
int main(int argc, char** argv)
{
    //Mat imgtest = imread(argv[1], IMREAD_COLOR);
    Mat imgtest = imread(argv[1], IMREAD_COLOR);
    imshow("image", imgtest);
    waitKey();
}
