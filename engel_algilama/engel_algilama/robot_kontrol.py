import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data 
from geometry_msgs.msg import Twist      # Hız mesaj tipi 
from sensor_msgs.msg import LaserScan    # Lidar mesaj tipi 

class EngelAlgilayici(Node): 
    def __init__(self):
        super().__init__('robot_kontrol_node') # Node'un sistemdeki adı
        
        # Publisher
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscriber
        # Veri gelince self.lidar_verisi_geldi fonksiyonunu çalıştır
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_verisi_geldi,
            qos_profile_sensor_data
        )
        self.get_logger().info('Robot hazır.')

    # Lidar'dan her veri geldiğinde çalışır
    def lidar_verisi_geldi(self, msg):

        # Robotun tam önü
        mesafe = msg.ranges[0]
        
        # Lidar'dan inf verisi dönerse güvenli bir mesafeye ayarla
        if mesafe == float('inf'):
             mesafe = 999.0 
             
        # Aksiyon Kararı: Twist mesajı oluşturup içini dolduracağız.
        hiz_mesaji = Twist()
        
        # Mesafe 0.5'ten küçükse dur ve logla
        if mesafe < 0.5: 
            # DUR [cite: 41]
            hiz_mesaji.linear.x = 0.0
            hiz_mesaji.angular.z = 0.0
            self.get_logger().warning(f'ENGEL VAR! Mesafe: {mesafe}m. DURUYORUM.')
        # Hareket et
        else:
            hiz_mesaji.linear.x = 0.5  
            hiz_mesaji.angular.z = 0.5 # Sola dön
            
        # Kararı yayınla
        self.publisher_.publish(hiz_mesaji)

def main():
    rclpy.init(args=args)      # ROS 2 iletişimini başlat
    node = EngelAlgilayici()   # Engel algılayıcı objesi üret
    rclpy.spin(node)           # Node'u canlı tut
    node.destroy_node()
    rclpy.shutdown()           # Kapat

if __name__ == '__main__':
    main()
