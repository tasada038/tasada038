from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    bar30_node = Node(
            package='ms5837_node',
            executable='bar30_node',
    )

    odom_to_base = Node(
            ## Configure the TF of the robot to the origin of the map coordinates
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'odom', 'base_link']
    )

    base_to_bar30 = Node(
            ## Configure the TF of the robot to the origin of the map coordinates
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'base_link', 'bar30_link']
    )

    return LaunchDescription([
        bar30_node,
        odom_to_base,
        base_to_bar30,
    ])
