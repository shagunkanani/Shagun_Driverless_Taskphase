import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class ResponseNode(Node):
    def __init__(self):
        super().__init__('response_node')

        self.response_publisher = self.create_publisher(
            String, '/palindrome_response', 10
        )

        self.result_subscription = self.create_subscription(
            Int32,
            '/palindrome_result',
            self.process_result,
            10
        )

    def process_result(self, message):
        response = String()

        if message.data == 1:
            response.data = 'Yes'
        else:
            response.data = 'No'

        self.response_publisher.publish(response)
        self.get_logger().info(f"Sent response: {response.data}")


def main(args=None):
    rclpy.init(args=args)
    node = ResponseNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
