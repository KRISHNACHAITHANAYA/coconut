"""
Unit tests for the Agent class.
"""

import unittest
import sys
import os

# Add the src directory to the path for standalone execution
# For production use, install the package with: pip install -e .
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from coconut import Agent


class TestAgent(unittest.TestCase):
    """Test cases for the Agent class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = Agent(name="TestAgent")
    
    def test_agent_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertEqual(self.agent.state, {})
        self.assertIsInstance(self.agent.config, dict)
    
    def test_agent_default_name(self):
        """Test agent with default name."""
        agent = Agent()
        self.assertEqual(agent.name, "Agent")
    
    def test_perceive(self):
        """Test perceive method."""
        result = self.agent.perceive(None)
        self.assertIsInstance(result, dict)
    
    def test_decide(self):
        """Test decide method."""
        result = self.agent.decide()
        self.assertIsInstance(result, dict)
    
    def test_act(self):
        """Test act method."""
        result = self.agent.act({})
        self.assertTrue(result)
    
    def test_run(self):
        """Test run method."""
        result = self.agent.run(max_iterations=5)
        self.assertIn('state', result)
        self.assertIn('iterations', result)
        self.assertLessEqual(result['iterations'], 5)
    
    def test_reset(self):
        """Test reset method."""
        self.agent.state = {"key": "value"}
        self.agent.reset()
        self.assertEqual(self.agent.state, {})
    
    def test_repr(self):
        """Test string representation."""
        repr_str = repr(self.agent)
        self.assertIn("TestAgent", repr_str)


if __name__ == '__main__':
    unittest.main()
