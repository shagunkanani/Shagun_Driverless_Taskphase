import rclpy
from rclpy.node import Node
from task_one_interfaces.msg import TaskOne


class WheelPublisher(Node):

    def __init__(self):
        super().__init__('wheel_publisher')

        self.publisher = self.create_publisher(
            TaskOne,
            '/taskone',
            10
        )

    def publish_wheel_data(self):
        angular_velocity = float(input("Enter angular velocity (rad/s): "))
        radius = float(input("Enter wheel radius (m): "))

        message = TaskOne()
        message.ang_vel = angular_velocity
        message.radius = radius

        self.publisher.publish(message)

        self.get_logger().info(
            f"Published: angular velocity = {angular_velocity} rad/s, "
            f"radius = {radius} m"
        )


def main(args=None):
    rclpy.init(args=args)

    node = WheelPublisher()

    try:
        node.publish_wheel_data()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
