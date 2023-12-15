class Database:

    def insert_data(self, data):
        pass

    def update_data(self, data):
        pass

    def delete_data(self, data):
        pass


class DatabaseFacade:

    def __init__(self, database):
        self.database = database

    def insert_data(self, data):
        self.database.insert_data(data)

    def update_data(self, data):
        self.database.update_data(data)

    def delete_data(self, data):
        self.database.delete_data(data)


database = Database()
facade = DatabaseFacade(database)

facade.insert_data({"id": 1, "name": "John Doe"})
facade.update_data({"id": 1, "name": "Jane Doe"})
facade.delete_data({"id": 1})
