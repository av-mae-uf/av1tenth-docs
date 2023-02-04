import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    example_node = Node(
        package="",
        executable="",
        parameters=[{"param1": value, "param2": value}],
    )
    example_node2 = Node(
        package="",
        executable="",
        parameters=[{"param1": value, "param2": value}],
    )
    ld.add_action(example_node)
    ld.add_action(example_node2)
    return ld
