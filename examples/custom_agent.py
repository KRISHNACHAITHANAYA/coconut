"""
Example: Custom Agent

This example shows how to create a custom agent by subclassing the base Agent.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from coconut import Agent


class CustomAgent(Agent):
    """
    A custom agent that implements specific behavior.
    """
    
    def __init__(self, name="CustomAgent", goal=None):
        super().__init__(name=name)
        self.goal = goal
        self.steps_taken = 0
    
    def perceive(self, environment):
        """Custom perception logic."""
        self.steps_taken += 1
        return {"step": self.steps_taken}
    
    def decide(self):
        """Custom decision logic."""
        if self.steps_taken < 3:
            return {"action": "explore"}
        else:
            return {"action": "complete"}
    
    def act(self, action):
        """Custom action execution."""
        print(f"  Step {self.steps_taken}: {action.get('action', 'unknown')}")
        
        if action.get('action') == 'complete':
            print(f"  Goal reached: {self.goal}")
            return False  # Stop execution
        
        return True


def main():
    """Run a custom agent example."""
    print("=" * 50)
    print("Custom Agent Example")
    print("=" * 50)
    print()
    
    # Create a custom agent
    agent = CustomAgent(name="MyCustomAgent", goal="Complete the task")
    print(f"Created agent: {agent}")
    print(f"Goal: {agent.goal}")
    print()
    
    # Run the agent
    print("Running custom agent...")
    result = agent.run(max_iterations=10)
    print()
    
    # Display results
    print("Results:")
    print(f"  Steps taken: {agent.steps_taken}")
    print(f"  Iterations: {result['iterations']}")
    print()
    
    print("=" * 50)
    print("Example completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
