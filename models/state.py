class State(BaseModel):
    # Existing code...

    def cities(self):
        """Returns the list of City objects linked to the State"""
        return [city for city in storage.all(City).values() if city.state_id == self.id]
