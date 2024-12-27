"""
Chapter 1: Automata and Logic Tutorial
This module demonstrates the practical implementation of automata concepts
combined with logical reasoning through two main examples:
1. Weather Prediction Automaton
2. String Recognition DFA (Deterministic Finite Automaton)
"""

from typing import Dict, Set, Tuple, List
from enum import Enum

# Weather Prediction Example
class WeatherState(Enum):
    """Weather states representation"""
    SUNNY = "Sunny"
    CLOUDY = "Cloudy"
    RAINY = "Rainy"

class WeatherInput(Enum):
    """Weather input factors"""
    HIGH_PRESSURE = "high pressure"
    LOW_PRESSURE = "low pressure"
    HUMIDITY = "humidity"

class WeatherAutomaton:
    """
    Weather prediction automaton that combines automata structure with logical rules
    to predict weather transitions.
    """
    def __init__(self):
        # Define states and inputs
        self.states = set(WeatherState)
        self.inputs = set(WeatherInput)
        self.current_state = WeatherState.SUNNY
        
        # Define transition rules
        self.transitions = {
            (WeatherState.SUNNY, WeatherInput.LOW_PRESSURE): WeatherState.CLOUDY,
            (WeatherState.CLOUDY, WeatherInput.HUMIDITY): WeatherState.RAINY,
            (WeatherState.RAINY, WeatherInput.HIGH_PRESSURE): WeatherState.CLOUDY,
            (WeatherState.CLOUDY, WeatherInput.HIGH_PRESSURE): WeatherState.SUNNY,
        }
    
    def transition(self, input_symbol: WeatherInput) -> WeatherState:
        """
        Process a weather input and return the new state based on transition rules.
        """
        if (self.current_state, input_symbol) in self.transitions:
            self.current_state = self.transitions[(self.current_state, input_symbol)]
        return self.current_state

    def predict_rain(self, inputs: List[WeatherInput]) -> bool:
        """
        Logical prediction rule: If humidity and low pressure are observed,
        rain is likely in the sequence.
        """
        return (WeatherInput.HUMIDITY in inputs and 
                WeatherInput.LOW_PRESSURE in inputs)

# DFA Example for strings ending with "ab"
class DFA:
    """
    Deterministic Finite Automaton implementation that recognizes
    strings ending with "ab".
    """
    def __init__(self):
        # Define DFA components
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.final_states = {'q2'}
        self.current_state = self.start_state
        
        # Define transition function
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q0',
        }
    
    def transition(self, symbol: str) -> str:
        """Process an input symbol and return the new state."""
        if (self.current_state, symbol) in self.transitions:
            self.current_state = self.transitions[(self.current_state, symbol)]
        return self.current_state
    
    def process_string(self, input_string: str) -> bool:
        """
        Process an entire string and determine if it's accepted.
        Returns True if the string ends in the final state.
        """
        self.current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            self.transition(symbol)
        return self.current_state in self.final_states
