# Human Pose Annotation Tool
![Example image_1](https://github.com/aimagelab/human-pose-annotation-tool/blob/master/img/example_1.png)

We aim to create a simple yet effective tool for create and modify annotation for Body Pose Estimation over depth images.
The vast majority of available datasets are not precisely noted, usually annotations are obtained using the [Kinect SDK](https://www.microsoft.com/en-us/research/project/human-pose-estimation-for-kinect/ "Microsoft Page"), which is supposed to works in a limited environment, returning incorrect annotation for general case-of-use.

![Example image_4](https://github.com/aimagelab/human-pose-annotation-tool/blob/master/img/example_4.png)

Our tool takes into account pre-existing annotations, plotting Body Joints over depth frames, for using such informations as a starting point. The RGB frame is also shown, to allow an easier reference.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. There's not much to do, just install prerequisites and download all the files.

### Prerequisites
Things you need to install to run the tool:

```
Python >= 3.6.7
pip install numpy
pip install opencv-python
pip install scipy
```

For running our test and to use our code without modifying a line, install PyTorch to use Dataset class.
```
pip install pytorch
```

## Running the tests
To run the simple test, just execute:
```
python Noter.py --data_dir ./test
```
This will open up one sequence of the [Watch-N-Patch](http://watchnpatch.cs.cornell.edu/ "WnP Page") dataset, in which the 2 frames shown above came from. The sequence is stored in the test directory.

## Features
- **Functionality**
  - **Move Joints**
  - **Delete Joints**
  - **Add not noted Joints**
  - **Reset action**
- **Input**
- **Output**
- **OS**

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
