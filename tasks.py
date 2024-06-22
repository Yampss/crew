from crewai import Task
from textwrap import dedent
from datetime import date


class TripTasks():

  def plan_itinerary(self, agent,city, travel_dates, interests):
    return Task(
        description=dedent(f"""
        **Task**: develop a 7 day itinerary        
        **Description**:** Description **: Expand the city guide into a full 7-day travel itinerary with detailed
            per-day plans, including weather forecasts, places to eat, packing suggestions,
            and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
            and actual restaurants to go to. This itinerary should cover all aspects of the trip,
            from arrival to departure, integrating the city quide information with practical travel logistics.
        **Parameters**:                   
        City: {city}
        Trip Date: {travel_dates}
        Traveler Interests: {interests}
      """),
                agent=agent,
    )

  def identify_city(self, agent,origin,cities, travel_dates, interests):
    return Task(
        description=dedent(f"""
        **Task**: Select the best city to travel to        
        **Description**: Analyze and select the best city for the trip based on specific
                            criteria such as weather patterns, seasonal events, and travel costs.
                            This task involves comparing multiple cities, considering factors like current weather
                            conditions, upcoming cultural or seasonal events, and overall travel expenses.
                            Your final answer must be a detailed report on the chosen city,
                            including actual flight costs, weather forecast, and attractions.
        **Parameters**:  
        Origin: {origin}                 
        Cities: {cities}
        Travel Date: {travel_dates}
        Interests: {interests}
      """),
                agent=agent,
    )

 def gather_city_information(self, agent,city, travel_dates, interests):
    return Task(
        description=dedent(f"""
        **Task**:gather in detail city guide information        
        **Description**: Compile an in-depth guide for the selected city, gathering information about
                        key attractions, local customs, special events, and daily activity recommendations.
                        This guide should provide a thorough overview of what the city has to offer, including
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level cost
        **Parameters**:                   
        Cities: {city}
        Travel Date: {travel_dates}
        Interests: {interests}
      """),
                agent=agent,
    )