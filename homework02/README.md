This contains generate_animals.py, test_read_animals.py, and read_animals.py. generate_animals.py creates a list of animals based on the parameters discussed in homework01, while read_animals.py randomly selects and prints two animals from this list with different "heads." The list of animals is stored as a JSON file (typically named animals.JSON, but can be named whatever). test_read_animals.py contains a unit tester to ensure that the code in read_animals.py works correctly in selecting two animals with different heads. The directory also contains a Dockerfile.

To download and run the scripts directly, simply git pull and run in any Python environment. Run generate_animals.py first, and then you can run either (or both) read_animals.py or test_read_animals.py. To build an image with the Dockerfile, run the following command: 
  docker build -t jeremykrill/hmwk:1.1 .
(Very important to include the period at the end.) You can check that the image was built by using docker images or docker inspect.

To run the scripts inside a container, use the following commands:
  docker run --rm -it jeremykrill/hmwk:1.1 /bin/bash
  cd /home
  generate_animals.py <filename>.json
  test_read_animals.py
  read_animals.py <filename>.json

The "test_read_animals.py" command will run the unit test described above.
