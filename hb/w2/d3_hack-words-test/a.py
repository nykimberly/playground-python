class FileNotFoundError(BaseException):
	"""A class to indicate file wasn't found."""


def get_file_fail(filename):
	raise FileNotFoundError

def get_file_pass(filename):
	return ["apple", "berry", "cherry"]


# in setUp for fileDoesNotExist test
get_file = get_file_fail

# in setUp for fileExists test
get_file = get_file_pass




