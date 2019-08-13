import pymysql
from api.models.revenueModel import RevenueModel
from config.revenueServiceConfig import RevenueServiceConfiguration


class RevenueDAO:

    def __init__(self):
        self.connection: pymysql.Connection = None
        self.revenue_service_configuration: RevenueServiceConfiguration = RevenueServiceConfiguration()

    def create_connection(self) -> pymysql.Connection:
        try:
            if not self.connection:
                self.connection = pymysql.connect(host=self.revenue_service_configuration.instance.HOST,
                                                  user=self.revenue_service_configuration.instance.USER,
                                                  password=self.revenue_service_configuration.instance.PASSWORD,
                                                  db=self.revenue_service_configuration.instance.DB,
                                                  charset=self.revenue_service_configuration.instance.CHARSET,
                                                  cursorclass=pymysql.cursors.DictCursor)
            return self.connection
        except pymysql.MySQLError as err:
            print("revenue service create_connection error : ")
            print(err)
            return None

    def retrieve_revenues(self):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM revenue")
            result = cursor.fetchall()
            return result
        except pymysql.MySQLError as err:
            print("revenue service retrieve_revenues error : ")
            print(err)
            return None

    def retrieve_user_revenues(self, user_id: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM revenue "
                           "WHERE RevenueUserId = %s", (user_id,))
            result = cursor.fetchall()
            return result
        except pymysql.MySQLError as err:
            print("revenue service retrieve_user_revenues error : ")
            print(err)
            return None

    def add_revenue(self, revenue_model: RevenueModel) -> bool:
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("INSERT INTO revenue (Id, RevenueUserId, Category, Name, Amount)"
                           "VALUES(%s,%s,%s,%s,%s)", (revenue_model.id, revenue_model.user_id,
                                                      revenue_model.category, revenue_model.name, revenue_model.amount))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("revenue service add_revenue error : ")
            print(err)
            return False

    def retrieve_revenue(self, revenue_id: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM revenue "
                           "WHERE Id = %s", (revenue_id,))
            result = cursor.fetchone()
            return result
        except pymysql.MySQLError as err:
            print("revenue service retrieve_revenue error : ")
            print(err)
            return None

    def remove_revenue(self, revenue_id: str) -> bool:
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("DELETE FROM revenue "
                           "WHERE Id = %s", (revenue_id,))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("revenue service remove_revenue error : ")
            print(err)
            return False
