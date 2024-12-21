import pytest
import os
@pytest.fixture
def setup_fixture():
    # Setup code: This runs before the test
    resource = open("test_file.txt", "w")
    resource.write("This is a test.")
    resource.close()

    # Yield indicates where the test will run
    yield

    # Teardown code: This runs after the test
    os.remove("test_file.txt")  # Clean up the test file

def test_example(setup_teardown):
    # Test code that runs between setup and teardown
    with open("test_file.txt", "r") as resource:
        content = resource.read()
        assert content == "This is a test."
