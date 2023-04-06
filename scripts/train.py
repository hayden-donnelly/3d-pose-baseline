import tensorflow as tf
import keras
from model import Model

if __name__ == "__main__":
    print(tf.config.list_physical_devices())
    
    model = Model(
        num_blocks = 2, 
        num_sub_blocks = 2, 
        num_keypoints = 17, 
        dense_units = 1024
    )