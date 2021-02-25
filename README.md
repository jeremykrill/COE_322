This directory contains my homework02 files. It has a file called "generate_animals.py" that creates a list of animals according to the homework01 instructions. The file "read_animals.py" outputs two random animals from the generated animals list and ensures that they have different types of heads. Finally, the "test_read_animals.py" file is a unit tester that works to check if the "read_animals.py" code runs correctly. The directory also has a Dockerfile that's used to build an image of the Python files.

To download and run the scripts directly, simply pull the files from Github and run in any IDE. Run the "generate_animals.py" file first so that a separate JSON file with the animals is created. Then, you can run either (or both) the unit tester or the "read_animals.py" file, which will access whatever JSON file you created- just make sure that you reference the file in the command to run.

To build an image with the Dockerfile, use the command docker build -t jeremykrill/hmwk2:1.1. Use docker images to inspect the image and check if it's been built. To run the scripts inside a container, use the following commands:
	docker run --rm -it username/json-parser:1.0 /bin/bash
	cd /home
	generate_animals.py <filename>.json
	read_animals.py <filename>.json
	test_read_animals.py
The last command will run the unit test. It checks the function check_animals in "read_animals.py" to make sure that the animals selected have different heads, and will output "OK" if the code works correctly.
