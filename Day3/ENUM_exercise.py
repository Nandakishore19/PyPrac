from enum import Enum

class Status(Enum):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    PREPARING = 'Preparing'
    OUTFORDELIVERY = 'OutForDelivery'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'



class Order:
    def __init__(self,id) -> None:
        self.order_id = id
        self.status = Status.PENDING
    def confirm(self):
        if self.status == Status.PENDING:
            self.status = Status.CONFIRMED
            print("Order {} Confirmed".format(self.order_id))
        else:
            print("Cannot Confirm the Order {0}, Status = {1}".format(self.order_id,self.status.value))

    def prepare(self):
        if self.status == Status.CONFIRMED:
            self.status = Status.PREPARING
            print("Order {} is currently being prepared".format(self.order_id))
        else:
            print("Order {0} cannot be Prepared, Status = {1}".format(self.order_id,self.status.value))
    def deliver(self):
        if self.status == Status.PREPARING:
            self.status = Status.OUTFORDELIVERY
            print("Order {} is Out for Delivery".format(self.order_id))
        else:
            print("Order {0} cannot be Delivered, Status = {1}".format(self.order_id,self.status.value))
    def drop(self):
        if self.status == Status.OUTFORDELIVERY:
            self.status = Status.DELIVERED
            print("Order {} is Delivered!!".format(self.order_id))
        else:
            print("Order {0} cannot be Delivered, Status = {1}".format(self.order_id,self.status.value))
    def cancel(self):
        if self.status != Status.DELIVERED:
            self.status = Status.CANCELLED
            print("Order {} is Cancelled ".format(self.order_id))
        else:
            print("Order {0} cannot be Cancelled its already Delivered, Status = {1}".format(self.order_id,self.status.value))

order_1 = Order(1)
order_1.confirm()
order_1.prepare()
order_1.deliver()
order_1.drop()


order_2 = Order(2)
order_2.confirm()
order_2.prepare()
order_2.cancel()
order_2.drop()
# stat = 'Pending'
# print(Status(stat))