<<<<<<< HEAD
from typing import Any
=======
from abc import ABC
from typing import List
>>>>>>> a0b5b9ad09dbd8be0f2c094aae5dc8759bd5272e
from superagi.tools.base_tool import BaseTool
import pika
import os
import logging
import datetime
import json
<<<<<<< HEAD
from rabbitmq_connection import RabbitMQConnection

class RabbitMQTool(BaseTool):  # RabbitMQTool should only inherit from BaseTool
    name = "RabbitMQ Tool"
    description = "A tool for interacting with RabbitMQ"
    rabbitmq_server: str
    rabbitmq_username: str
    rabbitmq_password: str
    connection_params: Any
    logger: Any
    base_tool: BaseTool

    def __init__(self):
        self.base_tool = BaseTool()  # Initialize the BaseTool instance
=======
from superagi.tools.rabbitmq.rabbitmq_connection import RabbitMQConnection

class RabbitMQTool(BaseTool, ABC):
    name = "RabbitMQ Tool"
    description = "A tool for interacting with RabbitMQ"

    def __init__(self):
>>>>>>> a0b5b9ad09dbd8be0f2c094aae5dc8759bd5272e
        self.rabbitmq_server = os.getenv('RABBITMQ_SERVER', 'localhost')
        self.rabbitmq_username = os.getenv('RABBITMQ_USERNAME', 'guest')
        self.rabbitmq_password = os.getenv('RABBITMQ_PASSWORD', 'guest')
        self.connection_params = pika.ConnectionParameters(
            host=self.rabbitmq_server,
            credentials=pika.PlainCredentials(self.rabbitmq_username, self.rabbitmq_password)
        )
        self.logger = logging.getLogger(__name__)

<<<<<<< HEAD
    def _execute(self, action, queue_name, message=None, msg_type="text", priority=0):
        if action == "send":
            self.send_natural_language_message(queue_name, message, msg_type, priority)
        elif action == "receive":
            return self.receive_natural_language_message(queue_name)
        else:
            raise ValueError(f"Unsupported action: {action}")

    def execute(self, action, queue_name, message=None, persistent=False, priority=0, callback=None, consumer_tag=None, delivery_tag=None):
        connection = RabbitMQConnection(self.connection_params, action, queue_name, message, persistent, priority, callback, consumer_tag, delivery_tag)
        return connection.run()

    def send_natural_language_message(self, receiver, content, msg_type="text", priority=0):
=======
    def execute(self, action, queue_name, message=None, persistent=False, priority=0, callback=None, consumer_tag=None, delivery_tag=None):
        """
        Execute a RabbitMQ operation.
        
        The operation can be either "send", "receive", "create_queue", "delete_queue", "add_consumer", "remove_consumer", or "send_ack". 
        """
        connection = RabbitMQConnection(self.connection_params, action, queue_name, message, persistent, priority, callback, consumer_tag, delivery_tag)
        connection.run()

    def send_natural_language_message(self, receiver, content, msg_type="text", priority=0):
        """
        Send a natural language message to a specified queue (receiver).
        """
>>>>>>> a0b5b9ad09dbd8be0f2c094aae5dc8759bd5272e
        message = {
            "sender": self.name,
            "receiver": receiver,
            "timestamp": datetime.datetime.now().isoformat(),
            "type": msg_type,
            "content": content
        }
        self.execute("send", receiver, json.dumps(message), priority=priority)

    def receive_natural_language_message(self, queue_name):
<<<<<<< HEAD
=======
        """
        Receive a natural language message from a specified queue.
        """
>>>>>>> a0b5b9ad09dbd8be0f2c094aae5dc8759bd5272e
        raw_message = self.execute("receive", queue_name)
        message = json.loads(raw_message)
        return message["content"]
