import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    serial_port = LaunchConfiguration('serial_port', default='/dev/ttyUSB0')
    frame_id = LaunchConfiguration('frame_id', default='laser')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')


    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': serial_port,
                # 'serial_port': '/dev/ttyUSB0',
                'frame_id': frame_id,
                'angle_compensate': angle_compensate,
                'scan_mode': 'Standard'
            }]
        )
    ])