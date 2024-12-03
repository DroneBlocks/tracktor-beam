from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    return LaunchDescription([
        # Run bridge nodes directly without screen
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge', '/camera@sensor_msgs/msg/Image@gz.msgs.Image'],
            name='image_bridge_process',
            output='screen',
        ),
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge', '/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'],
            name='camera_info_bridge_process',
            output='screen',
        ),
        Node(
            package='precision_land_april_tag',
            executable='precision_land_april_tag',
            name='precision_land_at',
            output='screen',
            parameters=[
                PathJoinSubstitution([FindPackageShare('precision_land_april_tag'), 'cfg', 'params.yaml'])
            ]
        ),
    ])
