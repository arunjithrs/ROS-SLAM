#!/usr/bin/env python3

import roslib
import rospy
import tf
import time
import math

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_broadcaster_node')

    time.sleep(2)

    transform_boradcaster = tf.TransformBroadcaster()
    
    while(not rospy.is_shutdown()):
        rotation_quaternion = tf.transformations.quaternion_from_euler(0.2, 0.3, 0.4);

        translation_vector = (1.0, 2.0, 3.0)

        current_time = rospy.Time.now()

        transform_boradcaster.sendTransform(
            translation_vector,
            rotation_quaternion,
            current_time,
            "frame_a", "frame_b"
        )

        time.sleep(0.5)
    
    rospy.spin()
