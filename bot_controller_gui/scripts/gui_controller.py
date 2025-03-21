#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

import tkinter as tk


root = tk.Tk()
root.title("Robot Controller")

root.geometry("550x350")
root.minsize(450, 200)

button_style = {
    "font": ("Arial", 14, "bold"),
    "width": 10,
    "fg": "white"
}

frame = tk.Frame(root)
frame.pack(expand=True)


if __name__ == "__main__":
    rospy.init_node("gui_node", anonymous=False)

    battery_label = tk.Label(root, text="Battery: 100%", font=("Arial", 15, "bold"), bg="#ADD8E6", width=40, height=2)
    battery_label.pack(pady=10)

    velocity_label = tk.Label(root, text="Linear: 0.0, Angular: 0.0", font=("Arial", 15, "bold"), bg="#90EE90", width=40, height=2)
    velocity_label.pack(pady=10)

    def data_function(msg):
        msg = list(msg.data)
        battery = msg[0]
        vel_linear = msg[1]
        vel_angular = msg[2]

        battery_label.config(text=f"Battery: {battery:.2f}%", fg="black")
        velocity_label.config(text=f"Linear: {vel_linear:.2f}, Angular: {vel_angular:.2f}", fg="black")

        rospy.loginfo(f"Battery: {battery:.2f}%, Linear: {vel_linear:.2f}, Angular: {vel_angular:.2f}")


    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    sub = rospy.Subscriber("rover_stats", Float32MultiArray, data_function)
    velocity = Twist()

    def move_forward():
        velocity.linear.x = 0.5
        pub.publish(velocity)

    def move_backward():
        velocity.linear.x = -0.5
        pub.publish(velocity)

    def move_right():
        velocity.angular.z = 0.3
        pub.publish(velocity)

    def move_left():
        velocity.angular.z = -0.3
        pub.publish(velocity)

    def stop():
        velocity.linear.x = 0
        velocity.angular.z = 0
        pub.publish(velocity)

    
    forward_button = tk.Button(frame, text="Forward", command=move_forward, bg="#000000", **button_style)
    forward_button.grid(row=0, column=1, pady=10)

    left_button = tk.Button(frame, text="Left", command=move_left, bg="#000000", **button_style)
    left_button.grid(row=1, column=0, padx=10)

    stop_button = tk.Button(frame, text="Stop", command=stop, bg="#E74C3C", **button_style)
    stop_button.grid(row=1, column=1, padx=10, pady=10)

    right_button = tk.Button(frame, text="Right", command=move_right, bg="#000000", **button_style)
    right_button.grid(row=1, column=2, padx=10)

    backward_button = tk.Button(frame, text="Backward", command=move_backward, bg="#000000", **button_style)
    backward_button.grid(row=2, column=1, pady=10)


    root.mainloop()
