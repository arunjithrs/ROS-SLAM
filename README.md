# SLAM

### Static Transform Publisher

```rosrun tf static_transform_publisher 1 2 3 0.1 0.2 0.3 frame_a frame_b 10```

 1 2 3 - translation vector, x y z
 0.1 0.2 0.3 - rotation angles yaw roll pitch
 frame_a - parent frame
 frame_b - child frame
 10 - publish 10 times in a second, broadcast freequencey
 
```rostopic list```
```
/rosout
/rosout_agg
/tf
```

```rostopic echo /tf```

``` 
transforms: 
    -
    header: 
      seq: 0
      stamp: 
        secs: 1670092897
        nsecs: 281896695
      frame_id: "frame_a"
    child_frame_id: "frame_b"
    transform: 
      translation: 
        x: 1.0
        y: 2.0
        z: 3.0
      rotation: 
        x: 0.14357217502739192
        y: 0.10602051106179562
        z: 0.03427079855048211
        w: 0.9833474432563558
```

### Generate frams

```rosrun tf2_tools view_frames.py```

### run the frame using launch file
create a package
```
cd catkin_ws/src ```
catkin_create_pkg ros_slam_test rospy roscpp turtlesim 
```

create a file inside ros_slam_test src ``static_transform_publisher.launch`` with below content
```
<launch>
    <node pkg="tf" type="static_transform_publisher" name="frame_a_to_frame_b" args="1 2 3 0.1 0.2 0.3 frame_a frame_b 10" />
</launch>
```

give permiossion
```
chmod 777 static_transform_publisher.launch
```






