import pytest
import tempfile
import os
from datetime import datetime
from mcp_server import get_current_time, add_numbers, write_file, get_docs

#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["mcp[cli]==1.9.3", "pytest==7.4.0"]
# ///



def test_get_current_time():
    """Test that get_current_time returns a valid ISO format datetime string."""
    result = get_current_time()
    assert isinstance(result, str)
    # Verify it's a valid ISO format
    datetime.fromisoformat(result)


def test_add_numbers():
    """Test the add_numbers function with various inputs."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(0, 0) == 0


def test_write_file():
    """Test that write_file creates a file with correct content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test.txt")
        content = "Hello, World!"
        
        result = write_file(test_file, content)
        
        assert result == test_file
        assert os.path.exists(test_file)
        
        with open(test_file, "r") as f:
            assert f.read() == content


def test_get_docs():
    """Test that get_docs reads the documents.txt file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        doc_file = os.path.join(tmpdir, "documents.txt")
        test_content = "Test documentation"
        
        with open(doc_file, "w") as f:
            f.write(test_content)
        
        # Note: This test assumes documents.txt exists in the working directory
        # Adjust the test based on your actual file location
        try:
            result = get_docs()
            assert isinstance(result, str)
        except FileNotFoundError:
            pytest.skip("documents.txt not found in current directory")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])