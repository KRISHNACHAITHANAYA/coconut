"""
Example: Basic Agent Usage

This example demonstrates how to create and use a simple agent.
"""

import sys
import os

# Add the src directory to the path for standalone execution
# For production use, install the package with: pip install -e .
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from coconut import Agent


def main():
    """Run a basic agent example."""
    print("=" * 50)
    print("Coconut Agent Example")
    print("=" * 50)
    print()
    
    # Create an agent
    agent = Agent(name="ExampleAgent")
    print(f"Created agent: {agent}")
    print()
    
    # Run the agent
    print("Running agent...")
    result = agent.run(max_iterations=5)
    print()
    
    # Display results
    print("Results:")
    print(f"  Final state: {result['state']}")
    print(f"  Iterations: {result['iterations']}")
    print()
    
    print("=" * 50)
    print("Example completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
