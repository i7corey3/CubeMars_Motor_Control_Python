import rclpy
from rclpy.node import Node
import can
import time
 
 
class AkDriver(Node):
	def __init__(self):
		super().__init__('control')

		self.declare_parameters(
			namespace="",
			parameters=[

			]
		)
 
		self.sim_time = self.get_parameter("use_sim_time").get_parameter_value().bool_value

		self.get_logger().info(f"sim_time is set to {self.sim_time}")
        







	time.sleep(1)
 
 
 
def main(args=None):
   rclpy.init(args=args)
 
   ak_driver = AkDriver()
 
   rate = ak_driver.create_rate(20)
   while rclpy.ok():
      rclpy.spin_once(ak_driver)

   ak_driver.destroy_node()
   rclpy.shutdown()
