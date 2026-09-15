from abc import ABC, abstractmethod


class MessageService(ABC):
  @abstractmethod
  def send(self, message):
    pass


class EmailService(MessageService):
  def send(self, message):
    return f"Email sent: {message}"


class SMSService(MessageService):
  def send(self, message):
    return f"SMS sent: {message}"


class Notification:
  def __init__(self, message_service):
    self.message_service = message_service

  def notify(self, message):
    return self.message_service.send(message)


if __name__ == "__main__":
  email_notification = Notification(EmailService())
  sms_notification = Notification(SMSService())

  print(email_notification.notify("Your order has shipped."))
  print(sms_notification.notify("Your verification code is 1234."))
