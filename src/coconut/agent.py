"""
Base Agent class for Coconut framework.

This module provides the core Agent class that serves as the foundation
for building intelligent agents.
"""


class Agent:
    """
    Base Agent class for creating AI agents.
    
    This class provides the basic structure for an agent that can perceive
    its environment, make decisions, and take actions.
    
    Attributes:
        name (str): The name of the agent
        state (dict): The current state of the agent
    
    Example:
        >>> agent = Agent(name="MyAgent")
        >>> agent.run()
    """
    
    def __init__(self, name="Agent", **kwargs):
        """
        Initialize an Agent.
        
        Args:
            name (str): The name of the agent
            **kwargs: Additional configuration parameters
        """
        self.name = name
        self.state = {}
        self.config = kwargs
    
    def perceive(self, environment):
        """
        Perceive the environment and update internal state.
        
        Args:
            environment: The environment to perceive
            
        Returns:
            dict: Perceived information from the environment
        """
        # Placeholder for perception logic
        return {}
    
    def decide(self):
        """
        Make a decision based on current state.
        
        Returns:
            dict: The decision made by the agent
        """
        # Placeholder for decision logic
        return {}
    
    def act(self, action):
        """
        Execute an action in the environment.
        
        Args:
            action: The action to execute
            
        Returns:
            bool: True if action was successful, False otherwise
        """
        # Placeholder for action execution
        return True
    
    def run(self, environment=None, max_iterations=100):
        """
        Run the agent's main loop.
        
        Args:
            environment: The environment for the agent to interact with
            max_iterations (int): Maximum number of iterations to run
            
        Returns:
            dict: Final state and results
        """
        print(f"{self.name} is running...")
        
        for iteration in range(max_iterations):
            # Perceive
            perception = self.perceive(environment)
            
            # Decide
            decision = self.decide()
            
            # Act
            success = self.act(decision)
            
            if not success:
                break
        
        print(f"{self.name} completed execution.")
        return {"state": self.state, "iterations": iteration + 1}
    
    def reset(self):
        """Reset the agent to its initial state."""
        self.state = {}
    
    def __repr__(self):
        """String representation of the agent."""
        return f"Agent(name='{self.name}')"
