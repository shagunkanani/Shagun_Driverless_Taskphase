import rclpy
from rclpy.node import Node

from task_one_interfaces.msg import TaskOne


class WheelSubscriber(Node):

    def __init__(self):
        super().__init__('wheel_subscriber')

        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.calculate_speed,
            10
        )

    def calculate_speed(self, message):
        angular_velocity = message.ang_vel
        radius = message.radius

        speed = angular_velocity * radius

        self.get_logger().info(
            f"Angular velocity: {angular_velocity} rad/s"
        )
        self.get_logger().info(f"Wheel radius: {radius} m")
        self.get_logger().info(f"Longitudinal speed: {speed} m/s")


def main(args=None):
    rclpy.init(args=args)

    node = WheelSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
