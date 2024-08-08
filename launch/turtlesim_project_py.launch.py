from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    turtle_spawner_node = Node(
        package="turtlesim_project_py",
        executable="turtle_spawner",
        parameters=[
            {"spawn_frequency": 1.0},
            {"turtle_name_prefix": "turtle"}
        ]
    )

    turtle_controller_node = Node(
        package="turtlesim_project_py",
        executable="turtle_controller",
        parameters=[
            {"catch_closest_turtle_first": True},
            {"P_controller_linear_coeff": 2},
            {"P_controller_angular_coeff": 6}
        ]
    )

    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld