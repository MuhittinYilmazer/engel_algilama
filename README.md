# Kurulum ve Çalıştırma

Bu proje ROS 2 Humble ve TurtleBot3 simülasyonu gerektirir.

### 1. Gerekli Paketlerin Kurulumu
```bash
sudo apt update
sudo apt install ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-simulations

# Workspace oluşturma ve projeyi indirme
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone [https://github.com/KULLANICI_ADINIZ/engel_algilama.git](https://github.com/KULLANICI_ADINIZ/engel_algilama.git)

# Derleme
cd ~/ros2_ws
colcon build --packages-select engel_algilama

# Kurulumu tanıtma
source install/setup.bash

# Terminal 1 (simülasyon)
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py

# Terminal 2 (sürüş programı)
source ~/ros2_ws/install/setup.bash
ros2 run engel_algilama baslat
