import rclpy
from rclpy.node import Node
from task_one_interfaces.msg import RT2String
from std_msgs.msg import Int32, String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.last_input = None

        self.result_publisher = self.create_publisher(
            Int32, '/palindrome_result', 10
        )

        self.response_subscription = self.create_subscription(
            String,
            '/palindrome_response',
            self.receive_response,
            10
        )

        self.input_subscription = self.create_subscription(
            RT2String,
            '/input_string',
            self.check_palindrome,
            10
        )

    def check_palindrome(self, message):
        text = message.data

        if text == self.last_input:
            return

        self.last_input = text
        normalized_text = text.replace(" ", "").lower()

        result = Int32()
        result.data = int(
            normalized_text == normalized_text[::-1]
        )

        self.result_publisher.publish(result)

        self.get_logger().info(
            f"Input: {text}; palindrome result: {result.data}"
        )

    def receive_response(self, message):
        self.get_logger().info(
            f"Response received: {message.data}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

