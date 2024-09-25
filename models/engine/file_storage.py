class FileStorage:
    # Existing code...

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()
