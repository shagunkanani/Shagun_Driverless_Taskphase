import rclpy
from rclpy.node import Node
from task_one_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')

        self.publisher = self.create_publisher(
            RT2String, '/input_string', 10
        )

        self.text = input("Enter a string: ")

        self.message = RT2String()
        self.message.data = self.text

        self.published = False
        self.timer = self.create_timer(
            1.0, self.publish_string
        )

    def publish_string(self):
        if not self.published:
            self.publisher.publish(self.message)

            self.get_logger().info(
                f"Published string: {self.message.data}"
            )

            self.published = True


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

