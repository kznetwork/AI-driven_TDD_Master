class EmailService:
  def send(self, message):
    return f"Email sent: {message}"


class Notification:
  def __init__(self):
    self.message_service = EmailService()

  def notify(self, message):
    return self.message_service.send(message)


if __name__ == "__main__":
  notification = Notification()
  print(notification.notify("Your order has shipped."))
