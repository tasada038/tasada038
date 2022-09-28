# https://automaticaddison.com/how-to-write-a-ros2-publisher-and-subscriber-python-foxy/

from math import fabs
from operator import truediv
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64


class ImuDataPubSub(Node):

  def __init__(self):

    # Initiate the Node class's constructor and give it a name
    super().__init__('imu_data_pubsub')

    # Create subscriber(s)    
    self.sub_bar30 = self.create_subscription(
        Float64,
        '/bar30/depth',
        self.pub_sub_callback,
        10
    )
    self.sub_bar30


    # Create publisher(s)  
    self.publisher_depth_data = self.create_publisher(
        Float64, 
        '/depth_data',
        10
    )




    self.msg = Float64()


  def pub_sub_callback(self, msg_data):
           
    self.msg.data = msg_data.data
    self.publish_depht(self.msg.data)



  def publish_depht(self, msg_data):
      #msg = Imu()m
      msg_data = Float64()
      msg_data.data = -1*self.msg.data

      self.publisher_depth_data.publish(msg_data)


def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create the node
  publishing_subscriber = ImuDataPubSub()
 
  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  # Publish any pending messages to the topics.
  rclpy.spin(publishing_subscriber)
 
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  publishing_subscriber.destroy_node()
 
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()
