import os
from crewai import Crew
from textwrap import dedent
from agents import Tr
from tasks import CustomTasks


class TripCrew:
    def __init__(self,origin,cities,date_range,interests):
        self.origin = origin
        self.cities=cities
        self.date_range=date_range
        self.interests=interests 
    
