#!/usr/bin/env python3
"""
Tests for Jupyter notebook assignments.
Simple test to verify notebook executes without errors.
"""

import pytest
import os
import sys
import subprocess


def test_notebook_execution():
    """Test that the notebook executes without errors using nbconvert."""
    notebook_path = "assignment.ipynb"

    assert os.path.exists(notebook_path), f"{notebook_path} not found"

    cmd = [
        sys.executable, '-m', 'nbconvert',
        '--to', 'notebook',
        '--execute',
        '--output', 'test_executed.ipynb',
        notebook_path
    ]

    try:
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600,  # 10 minute timeout
            check=True
        )

        # Clean up
        if os.path.exists('test_executed.ipynb'):
            os.remove('test_executed.ipynb')

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Notebook execution failed: {e.stderr}")
    except subprocess.TimeoutExpired:
        pytest.fail("Notebook execution timed out (10 minutes)")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
